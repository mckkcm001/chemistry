import decimal

def sigfig(n,s=3):
    decimal.getcontext().prec = s
    return decimal.Decimal(n).normalize().to_eng_string()
