import numpy as np

def dbm_to_mw(dbm):  return 10 ** (dbm / 10)
def mw_to_dbm(mw):   return 10 * np.log10(mw)

def gamma(zl, z0=50):          return (zl - z0) / (zl + z0)
def return_loss_db(g):         return -20 * np.log10(abs(g))
def vswr(g):                   return (1 + abs(g)) / (1 - abs(g))
def mismatch_loss_db(g):       return -10 * np.log10(1 - abs(g) ** 2)

def l_match(r_low, r_high, f_hz):
    q = np.sqrt(r_high / r_low - 1)
    w = 2 * np.pi * f_hz
    return q, q * r_low / w, q / (w * r_high)   # Q, L (H), C (F)

if __name__ == "__main__":
    g = gamma(75)
    print(return_loss_db(g), vswr(g), mismatch_loss_db(g))
    q, L, C = l_match(20, 50, 915e6)
    print(f"Q={q:.3f}  L={L*1e9:.2f} nH  C={C*1e12:.2f} pF")