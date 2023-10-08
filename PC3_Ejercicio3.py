class circulo:
    def __init__(self, radio):
        self.radio = radio
    
    def calculo_area(self):
        area = 3.1416 * (self.radio ** 2)
        return area

if __name__ == '__main__':
    try:
        radio = float(input("Ingrese el radio del círculo: "))
        circulo2 = circulo(radio)
        area = circulo2.calculo_area()
        print(f"El área del círculo con radio {radio} es: {area}")
    except ValueError:
        print("Error: Ingrese un número válido para el radio del circulo")
