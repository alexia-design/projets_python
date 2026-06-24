import string

print()
print("---CE PROGRAMME CONSISTE A CONVERTIR UNE DEVISE EN UNE AUTRE---")

print()
print("Les devises disponibles sont L'Euro, le Dollar et le Franc CFA")

print()
print("---Devise à convertir---")
devise1=str(input("Entrez la devise que vous voulez convertir (Euro - Dollar - Francs CFA) : "))
while devise1!="Euro" and devise1!="Dollar" and devise1!="Francs CFA" :
    print("ERREUR")
    devise1=str(input("Entrez la devise que vous voulez convertir (Euro - Dollar - Francs CFA) : "))

print()
print("---Devise de conversion---")
devise2=str(input("Entrez la devise dans laquelle vous voulez convertir (Euro - Dollar - Francs CFA) : "))
while (devise2!="Euro" and devise2!="Dollar" and devise2!="Francs CFA") :
    print("ERREUR")
    devise2=str(input("Entrez la devise dans laquelle vous voulez convertir (Euro - Dollar - Francs CFA) : "))


print()
print("---Montant à convertir---")
montant=int(input("Entrez le montant que vous voulez convertir : "))

print()
if (devise1=="Euro" and devise2=="Dollar"):
    conversion1=montant*1.07
    print(f"Le montant converti est de : {conversion1} dollars.")

    print()
elif (devise1=="Euro" and devise2=="Francs CFA"):
    conversion2=montant*655.957
    print(f"Le montant converti est de : {conversion2} francs CFA.")

    print()
elif (devise1=="Dollar" and devise2=="Euro"):
    conversion3=montant*0.85
    print(f"Le montant converti est de : {conversion3} euros.")

    print()
elif (devise1=="Dollar" and devise2=="Francs CFA"):
    conversion4=montant*560.04
    print(f"Le montant converti est de : {conversion4} francs CFA.")

    print()
elif (devise1=="Francs CFA" and devise2=="Euro"):
    conversion5=montant*0.0015
    print(f"Le montant converti est de : {conversion5} euros.")

    print()
elif (devise1=="Francs CFA" and devise2=="Dollar"):
    conversion6=montant*0.0018
    print(f"Le montant converti est de : {conversion6} dollars.")
    
print()
