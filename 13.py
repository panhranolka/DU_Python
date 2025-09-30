# Napíš funkciu, ktorá má na vstupe tri koeficienty a,b,c, ktoré sú koeficientami kvadratickej rovnice. 
# Funkcia vypíše hodnoty korenov kvadratickej funkcie ax2+bx+c=0 , ak existujú
import math
a = float(input("Zadaj 1. číslo "))
b = float(input("Zadaj 2. číslo "))
c = float(input("Zadaj 3. číslo "))

def rovnica(a, b, c):
    D = b**2 - 4*a*c

    if D > 0:
        x1 = (-b + D) / (2*a)
        x2 = (-b - D) / (2*a)
        return  x1,x2 
    if D == 0:
        x = -b / (2*a)
        return x
    else:
        return "Nemá riešenie"
print (rovnica(a,b,c))