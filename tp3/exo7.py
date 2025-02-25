

premier=input("Veuillez saisir le premier mot: ").strip()
second=input("Veuillez saisir le deuxième mot: ").strip()


if premier<second:
    print(f"Le mot {premier} vient en premier ")
elif premier>second:
    print(f"Le mot {second} vient en premier ")
else:
    print('Vous avez entré le même mot 2 fois !!')