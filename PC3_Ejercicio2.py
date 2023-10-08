def funcion_numeros():
    while True:
        entrada = input("Ingrese números separados por comas: ")
        
        try:
            numeros_texto = entrada.split(',') 
            numeros_decimales = [float(num.strip()) for num in numeros_texto]
            numeros_enteros = [int(num) for num in numeros_decimales]
            return numeros_enteros
        except ValueError:
            print("Error: Hubo un problema al convertir los números. "
                  "Por favor, asegúrese de ingresar números válidos.")

if __name__ == '__main__':
    numeros_enteros = funcion_numeros()
    
    if numeros_enteros:
        print("Números enteros obtenidos:", numeros_enteros)
