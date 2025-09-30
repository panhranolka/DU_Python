# Napíš program, ktorý zistí, či dané číslo x patrí do intervalu <a,b>
x = float(input("Zadaj číslo "))
a = float(input("Zadaj 1. čislo intervalu "))
b = float(input("Zadaj 2. čislo intervalu "))
if x>=a and x<=b:
    print("patrí do intervalu")