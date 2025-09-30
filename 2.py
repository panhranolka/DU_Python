# Napíš program, ktorý vráti prevrátenú hodnotu daného čísla. / t.j. 1/x
x = float(input("Zadaj číslo "))
Vysledok = 1/x
if x==0:
    print("Nulou sa nedá deliť")
else:
    print("Výsledok je", Vysledok)