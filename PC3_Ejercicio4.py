class rectangulo:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho
    
    def calculo_area(self):
        area = self.largo * self.ancho
        return area

if __name__ == '__main__':
    try:
        largo = float(input("Ingrese el largo del rectángulo: "))
        ancho = float(input("Ingrese el ancho del rectángulo: "))
        rectangulo2 = rectangulo(largo, ancho)
        area = rectangulo2.calculo_area()
        print(f"El área del rectángulo con largo {largo} y ancho {ancho} es: {area}")
    except ValueError:
        print("Error: Ingrese valores válidos para el largo y el ancho del rectángulo.")
