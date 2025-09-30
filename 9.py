# Napíš program, kt. zistí, či je v danom reťazci dané písmeno.
retazec = input("Napíš reťazec ")
pismeno = input("Napíš písmeno ")
if pismeno in retazec:
    print ("je v reťazci")
else:
    print ("nie je v reťazci")