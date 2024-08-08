# Write a menu driven program - 1.cm to ft  2.kl to miles  3.usd to inr  4.exit

def cm_ft(s):
    ans = (s) / 30
    return ans,"ft"

def kl_ml(s):
    ans = s * 0.62
    return ans,"miles"

def usd_inr(s):
    ans = s * 80
    return ans,"inr"

print(cm_ft(15))
print(kl_ml(1))
print(usd_inr(1))
