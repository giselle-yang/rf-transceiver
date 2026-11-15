import numpy as np

def fspl_db(f_mhz, d_km):
    return 32.45 + 20*np.log10(f_mhz) + 20*np.log10(d_km)

def log_distance_pl_db(f_mhz, d_m, n, d0_m=1.0):
    pl_d0 = fspl_db(f_mhz, d0_m/1000)          # free-space loss at reference distance
    return pl_d0 + 10*n*np.log10(d_m/d0_m)

def sensitivity_dbm(bw_hz, nf_db, snr_db):
    return -174 + 10*np.log10(bw_hz) + nf_db + snr_db

def link(p_tx, g_tx, g_rx, path_loss, sens, l_tx=0, l_rx=0):
    p_rx = p_tx + g_tx - l_tx + g_rx - l_rx - path_loss
    return p_rx, p_rx - sens

if __name__ == "__main__":
    f = 915
    sens = sensitivity_dbm(20e3, 6, 10)
    print(f"Sensitivity (GFSK 10 kbps): {sens:.1f} dBm")

    pl = fspl_db(f, 1.0)
    p_rx, m = link(20, 2, 2, pl, sens)
    print(f"Free space, 1 km: PL={pl:.1f} dB  Prx={p_rx:.1f} dBm  margin={m:.1f} dB")

    pl = log_distance_pl_db(f, 1000, n=3)
    p_rx, m = link(20, 2, 2, pl, sens)
    print(f"n=3, 1 km:        PL={pl:.1f} dB  Prx={p_rx:.1f} dBm  margin={m:.1f} dB")