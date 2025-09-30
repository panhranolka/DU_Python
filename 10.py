# Naprogramuj funkciu, ktorá zistí, či je dané číslo párne.
x = int(input("Zadaj číslo "))
def parne(x):
    if x % 2 == 0:
        return "číslo je párne"
    else:
        return "číslo je nepárne"
print (parne(x))