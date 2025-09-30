# Napíš program, kt. má na vstupe dve čísla a vypíše hodnotu väčšieho z nich. Ak sú čísla rovnaké, vypíše text, “sú rovnaké”
a = float(input("Zadaj 1. číslo "))
b = float(input("Zadaj 2. číslo "))
if a>b:
    print(a)
if b>a:
    print(b)
if a==b:
    print("sú rovnaké")