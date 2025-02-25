
nombre1=float(input("Nombre 1: "))
nombre2=float(input("Nombre 2: "))
operation = input("Opération: ")
# vous pouvez faire un overwriting sur operation de la facon suivante 
# operation = operation.strip()
# aussi si vous faites .strip()  avant lors de la recuperation est encore mieux comme l'exemple suivant
# operation = input("Opération: ").strip()
# si vous optez pour l'une de ces choix, vous faites operation=="+" directement sans strip()
if operation.strip()=="+":
    print(f"{nombre1}+{nombre2}= {nombre1+nombre2}")
elif operation.strip()=="-":
    print(f"{nombre1}-{nombre2}= {nombre1-nombre2}")
elif operation.strip()=="*":
    print(f"{nombre1}*{nombre2}= {nombre1*nombre2}")
elif operation.strip()=="/" and nombre2!=0:
    print(f"{nombre1}/{nombre2}= {nombre1/nombre2}")
else :
    print("Pas d'opération valide!!!")
