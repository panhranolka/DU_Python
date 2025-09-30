# 1. Napíš program, ktorý vypíše, ak súčin dvoch ľubovoľných čísel “presiahol 100”  
# a ak nepresiahol, tak vypíše “nepresiiahol 100”
a = float(input("Zadaj 1. číslo "))
b = float(input("Zadaj 2. číslo "))
if a*b>100:
    print ("presiahol 100")
if a*b<=100:
    print ("nepresiahol 100")