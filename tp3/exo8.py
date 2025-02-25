
print("Personne N°=1")
nom1= input("Nom: ").strip()
age1=int(input("Age: "))
print("Personne N°=2")
nom2= input("Nom: ").strip()
age2=int(input("Age: "))

if age1>age2:
    print(f"{nom1.capitalize()} est l’ainée ;)")
elif age2>age1:
    print(f"{nom2.capitalize()} est l’ainée ;)")  # .capilatize() zdtha ghir bash tban l output perfect u zwina
else:
     print(f"{nom1.capitalize()} et {nom2.capitalize()} ont le même âge !") 

