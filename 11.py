# Napíš funkciu, kde na vstupe sú tri čísla a funkcia vráti hodnotu najväčšieho z nich
a = float(input("Zadaj 1. číslo "))
b = float(input("Zadaj 2. číslo "))
c = float(input("Zadaj 3. číslo "))
def najvacsie(a,b,c):
    return max(a,b,c)
print (najvacsie(a,b,c))