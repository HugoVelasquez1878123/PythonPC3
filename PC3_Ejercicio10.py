class circulo:
    def __init__(self, radio):
        self.radio = radio
    
    def calculo_area(self):
        area = 3.1416 * (self.radio ** 2)
        return area

class rectangulo:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho
    
    def calculo_area(self):
        area = self.largo * self.ancho
        return area

def menu():
    while True:
        print("\nMenú:")
        print("1. Calcular el área de un círculo")
        print("2. Calcular el área de un rectángulo")
        print("3. Calcular el área de un cuadrado")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            radio = float(input("Ingrese el radio del círculo: "))
            circulo2 = circulo(radio)
            area = circulo2.calculo_area()
            print(f"El área del círculo con radio {radio} es: {area}")
        elif opcion == '2':
            largo = float(input("Ingrese el largo del rectángulo: "))
            ancho = float(input("Ingrese el ancho del rectángulo: "))
            rectangulo2 = rectangulo(largo, ancho)
            area = rectangulo2.calculo_area()
            print(f"El área del rectángulo con largo {largo} y ancho {ancho} es: {area}")
        elif opcion == '3':
            lado = float(input("Ingrese el lado del cuadrado: "))
            cuadrado = rectangulo(lado, lado)  # Un cuadrado es un tipo especial de rectángulo
            area = cuadrado.calculo_area()
            print(f"El área del cuadrado con lado {lado} es: {area}")
        elif opcion == '4':
            print("Bais")
            break
        else:
            print("Por favor, seleccione una opción válida.")

if __name__ == '__main__':
    menu()
