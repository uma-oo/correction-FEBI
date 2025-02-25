
annee = int(input("Entrer une année: "))
leap_annee= False

if annee % 100 == 0:
    if annee % 400 == 0:
        leap_annee=True
elif annee % 4 == 0:   
    leap_annee=True
 
if leap_annee:
    print("Cette année est leap")
else:
    print("Cette année n'est pas leap")