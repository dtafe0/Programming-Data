payrate = 42
hours = 37.5
taxrate = 0.15


grosspay = payrate * hours
withtax = grosspay*taxrate

netpay = grosspay - withtax

print("grosspay:", grosspay)
print("withholding tax:", withtax)
print("netpay:", netpay)