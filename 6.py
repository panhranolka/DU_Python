# Napíš program, kt. zistí, či je číslo delitelné štyrmi alebo siedmimi alebo nie je
x = int(input("Zadaj číslo "))
# % znamena zvyšok pri delení, aj je nula tak je delitelné
if x % 4==0:
    print("je delitelné štyrmi")
if x % 7==0:
    print("je delitelné siedmimi")
if x % 4>0 and x % 7>0:
    print("nie je delitelne siedmimi ani štyrmi")