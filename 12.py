# Napíš funkciu, kde a vstupe sú 3 čísla. Funkcia vypíše “je to trojuholnik” 
# ak tieto čísla môžu byť stranami trojuholníka a a ak áno, tak akého (pravouhlého, rovnoramenného, rovnostranného ap.) 
# funkcia vypíše “nie je to trojuholník” , ak strany nie sú stranami troj.(neplatí trojuholníková nerovnosť)
a = float(input("Zadaj prvu stranu trojuholnika v cm "))
b = float(input("Zadaj druhu stranu trojuholnika v cm "))
c = float(input("Zadaj tretiu stranu trojuholnika v cm "))
def trojuholnik(a,b,c):
    if a+c<=b or a+c<=b or b+c<=a:
        return "nie je to trojuholník"
    if a+c>b or a+c>b or b+c>a:
        print("je to trojuholník")
    if (a**2+b**2==c**2) or (a**2+c**2==b**2) or (c**2+b**2==a**2):
        return "je to pravouhly trojuholnik"
    if(a==b==c):
        return "trojuholnik je rovnostranny"
    if(a==b and a!=c) or (a==c and b!=c) or (b==c and a!=c):
        return "je to rovnoramenny trojuholnik"
print (trojuholnik(a,b,c))