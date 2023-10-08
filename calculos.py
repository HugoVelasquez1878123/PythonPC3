import operaciones

a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segunod número: "))

suma2 = operaciones.suma(a, b)
print(f"La suma de {a} y {b} es: {suma2}")

resta2 = operaciones.resta(a, b)
print(f"La resta de {a} y {b} es: {resta2}")

producto2 = operaciones.producto(a, b)
print(f"El producto de {a} y {b} es: {producto2}")

division2 = operaciones.division(a, b)
print(f"La división de {a} entre {b} es: {division2}")
