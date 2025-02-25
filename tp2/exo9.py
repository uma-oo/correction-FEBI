from math import sqrt 
a= float(input("Valaur de a: "))
b=float(input("Valeur de b: "))
c= float(input("Valeur de c:"))

x1=(-b+sqrt(b**2-(4*a*c)))/(2*a)
x2=(-b-sqrt(b**2-(4*a*c)))/(2*a)
print(f"Les racines sont {x1} et {x2}")