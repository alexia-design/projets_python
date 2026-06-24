print() 
print("--- VOUS ENTREREZ 5 NOTES DE QUATRES MATIERES DIFFERENTES ET LE PROGRAMME CALCULERA LA MOYENNE TRIMESTRIELLE DE L'ÉLÈVE ---") 
 
def appreciation(moyenne): 
    if moyenne >= 16: 
        return "Très bien" 
    elif moyenne >= 14: 
        return "Bien" 
    elif moyenne >= 12: 
        return "Assez bien" 
    elif moyenne >= 10: 
        return "Suffisant" 
    else: 
        return "Insuffisant" 

print() 
print("--- MATHEMATIQUES ---") 

print() 
print("Veuillez entrer les notes d'interrogations de la matière MATHEMATIQUES : ") 
print()
m1 = float(input("Interrogation 1 : "))
while (m1 < 0 or m1 > 20) :
        print("ERREUR. Ecrire une note entre 0 et 20.")
        m1 = float(input("Interrogation 1 : "))
m2 = float(input("Interrogation 2 : "))
while (m2 < 0 or m2 > 20) :
        print("ERREUR. Ecrire une note entre 0 et 20.")
        m2 = float(input("Interrogation 2 : "))


print()
print("Veuillez entrer les notes de devoirs de la matière MATHEMATIQUES : ") 
m3 = float(input("Devoir 1 : ")) 
while (m3 < 0 or m3 > 20) :
    print("ERREUR. Ecrire une note entre 0 et 20.")
    m3 = float(input("Devoir 1 : "))
m4 = float(input("Devoir 2 : ")) 
while (m4 < 0 or m4 > 20) :
    print("ERREUR. Ecrire une note entre 0 et 20.")
    m4 = float(input("Devoir 2 : "))
 
print() 
print("Veuillez entrer la note d'examen de la matière MATHEMATIQUES : ") 
m5 = float(input("Examen : ")) 
while (m5 < 0 or m5 > 20) :
    print("ERREUR. Ecrire une note entre 0 et 20.")
    m5 = float(input("Examen : ")) 
 
print() 
print("---Calcul de la moyenne de la matière MATHEMATIQUES---") 
moyenne_maths = (m1 + m2 + (m3*2) + (m4*2) + (m5*2)) / 8 
print("La moyenne de la matière MATHEMATIQUES est : ", moyenne_maths) 
 
print() 
print("Appréciation de la matière MATHEMATIQUES : ") 
print(appreciation(moyenne_maths)) 

 
print() 
print("---PHYSIQUE---") 
 
print() 
print("Veuillez entrer les notes d'interrogations de la matière PHYSIQUE : ") 
p1 = float(input("Interrogation 1 : ")) 
while (p1 < 0 or p1 > 20) :
    print("ERREUR. Ecrire une note entre 0 et 20.")
    p1 = float(input("Interrogation 1 : "))
p2 = float(input("Interrogation 2 : ")) 
while (p2 < 0 or p2 > 20) :
    print("ERREUR. Ecrire une note entre 0 et 20.")
    p2 = float(input("Interrogation 2 : "))
 
print() 
print("Veuillez entrer les notes de devoirs de la matière PHYSIQUE : ") 
p3 = float(input("Devoir 3 : ")) 
p4 = float(input("Devoir 4 : ")) 
 
print() 
print("Veuillez entrer la note d'examen de la matière PHYSIQUE : ") 
p5 = float(input("Examen 5 : ")) 
while (p5 < 0 or p5 > 20) :
    print("ERREUR. Ecrire une note entre 0 et 20.")
    p5 = float(input("Examen 5 : ")) 
 
print() 
print("---Calcul de la moyenne de la matière PHYSIQUE---") 
moyenne_physique = (p1 + p2 + (p3*2) + (p4*2) + (p5*2)) / 8 
print("La moyenne de la matière PHYSIQUE est : ", moyenne_physique  ) 
 
print() 
print("Appréciation de la matière PHYSIQUE : ") 
print(appreciation(moyenne_physique)) 
 
print() 
print("---FRANCAIS---") 
print() 
print("Veuillez entrer les notes d'interrogations de la matière FRANCAIS : ") 
f1 = float(input("Interrogation 1 : ")) 
while (f1 < 0 or f1 > 20) :
    print("ERREUR. Ecrire une note entre 0 et 20.")
    f1 = float(input("Interrogation 1 : "))
f2 = float(input("Interrogation 2 : ")) 
while (f2 < 0 or f2 > 20) :
    print("ERREUR. Ecrire une note entre 0 et 20.")
    f2 = float(input("Interrogation 2 : "))
 
print() 
print("Veuillez entrer les notes de devoirs de la matière FRANCAIS : ") 
f3 = float(input("Devoir 3 : ")) 
while (f3 < 0 or f3 > 20) :
    print("ERREUR. Ecrire une note entre 0 et 20.")
    f3 = float(input("Devoir 3 : "))
f4 = float(input("Devoir 4 : ")) 
while (f4 < 0 or f4 > 20) :
    print("ERREUR. Ecrire une note entre 0 et 20.")
    f4 = float(input("Devoir 4 : "))
 
print() 
print("Veuillez entrer la note d'examen de la matière FRANCAIS : ") 
f5 = float(input("Examen 5 : ")) 
while (f5 < 0 or f5 > 20) :
    print("ERREUR. Ecrire une note entre 0 et 20.")
    f5 = float(input("Examen 5 : "))
 
print() 
print("---Calcul de la moyenne de la matière FRANCAIS---") 
moyenne_francais = (f1 + f2 + (f3*2) + (f4*2) + (f5*2)) / 8 
print("La moyenne de la matière FRANCAIS est : ", moyenne_francais) 
 
print() 
print("Appréciation de la matière FRANCAIS : ") 
print(appreciation(moyenne_francais)) 
 
 
print() 
print("---ANGLAIS---") 
print() 
print("Veuillez entrer les notes d'interrogations de la matière ANGLAIS : ") 
a1 = float(input("Interrogation 1 : ")) 
while (a1 < 0 or a1 > 20) :
    print("ERREUR. Ecrire une note entre 0 et 20.")
    a1 = float(input("Interrogation 1 : "))
a2 = float(input("Interrogation 2 : ")) 
while (a2 < 0 or a2 > 20) :
    print("ERREUR. Ecrire une note entre 0 et 20.")
    a2 = float(input("Interrogation 2 : "))
 
print() 
print("Veuillez entrer les notes de devoirs de la matière ANGLAIS : ") 
a3 = float(input("Devoir 3 : ")) 
while (a3 < 0 or a3 > 20) :
    print("ERREUR. Ecrire une note entre 0 et 20.")
    a3 = float(input("Devoir 3 : "))
a4 = float(input("Devoir 4 : ")) 
while (a4 < 0 or a4 > 20) :
    print("ERREUR. Ecrire une note entre 0 et 20.")
    a4 = float(input("Devoir 4 : "))
 
print() 
print("Veuillez entrer la note d'examen de la matière ANGLAIS : ") 
a5 = float(input("Examen 5 : ")) 
while (a5 < 0 or a5 > 20) :
    print("ERREUR. Ecrire une note entre 0 et 20.")
    a5 = float(input("Examen 5 : "))
 
print() 
print("---Calcul de la moyenne de la matière ANGLAIS---") 
moyenne_anglais = (a1 + a2 + (a3*2) + (a4*2) + (a5*2)) / 8 
print("La moyenne de la matière ANGLAIS est : ", moyenne_anglais) 
 
print() 
print("Appréciation de la matière ANGLAIS : ") 
print(appreciation(moyenne_anglais)) 
 
 
print() 
print("---Calcul de la moyenne trimestrielle de l'élève---") 
moyenne_trim = (moyenne_maths + moyenne_physique + moyenne_francais + moyenne_anglais) / 4 
print("La moyenne trimestrielle de l'élève est : ", moyenne_trim) 
print() 
print("Appréciation de l'élève : ") 
print(appreciation(moyenne_trim))

print()