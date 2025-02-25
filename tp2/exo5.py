

nbre_etudians = int(input("Combien d'étudians dans le cours? "))
taille_grp= int(input("Taille de groupe souhaitée? "))
nombre_grp=nbre_etudians//taille_grp
reste=nbre_etudians!=taille_grp*nombre_grp
print(f"Nombre de groupes formés: {nombre_grp+reste}")