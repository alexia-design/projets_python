print()
print("---CE PRGRAMME CONSISTE A RESOUDRE UNE EQUATION DU SECOND DEGRE ET A LA FACTORISER---")
print()
a=int(input("Entrez votre reel a (a non nul) : "))
while (a==0) :
    print("ERREUR. Veuillez entrer un reel a différent de 0.")
    a=int(input("Entrez votre reel a (a non nul) : "))
b=int(input("Entrez votre reel b : "))
c=int(input("Entrez votre reel c : "))

print()
print(f"Votre equation du second degre est : {a}x² + {b}x + {c} = 0")

print()
print("---Calcul du discriminant---")
d= b**2-(4*a*c)
print(f"Le discrimant est : {d}")

print()
print("---Possibilite de solutions---")
if (d<0):
    print("Pas de solutions")
elif (d==0):
    print("L'equation possede une et une seule solution")
    print("---Calcul de la solution---")
    x0=(-b)/(2*a)
    print(f"La solution est : {x0}")
else:
    print("L'equation possede des solutions")
    print()
    print("---Calcul des solutions---")
    x1=(-b-d**0.5)/(2*a)
    x2=(-b+d**0.5)/(2*a)
    print(f"Les solutions sont : {x1} et {x2}")
print()
print("---Factorisation du polynôme---")
if (d<0):
    print("Pas de factorisation")
    print()
elif (d==0):
    print(f"L'equation factorisée est : (x - {x0})²")
else:
    print(f"L'equation factorisée est : (x - {x1})(x - {x2})")
    print()