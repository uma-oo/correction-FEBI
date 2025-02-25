

nombre= float(input("Nombre: "))
if nombre<0:
    print("le nombre est négatif.")
elif nombre%2==0 and nombre%3==0:
    print("fish and ships")
elif nombre%3==0:
    print("chips")
elif nombre%2==0:
    print("fish")
else:
    print("non divisible")
