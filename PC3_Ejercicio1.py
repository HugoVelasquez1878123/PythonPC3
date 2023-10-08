def porcentaje_gasolina(fraction):
    try:
        x, y = map(int, fraction.split('/'))

        if y == 0:
            raise ZeroDivisionError("El denominador no puede ser cero.")
        if x < 0 or y <= 0:
            raise ValueError("Los números deben ser enteros y X debe ser menor o igual a Y.")
        if x/y > 1:
            raise ValueError("Vuelva a ingresar el número")

        porcentaje = (x / y) * 100

        if porcentaje > 0.99 and porcentaje < 1:
            return 'E'
        else:
            return f'{round(porcentaje)}%'

    except ValueError as ve:
        print(f"Error: {ve}")
        return None
    except ZeroDivisionError as zde:
        print(f"Error: {zde}")
        return None

if __name__ == '__main__':
    while True:
        entrada = input("Ingrese una fracción en formato X/Y (e.g., 3/4): ")
        resultado = porcentaje_gasolina(entrada)
        
        if resultado is not None:
            print(f"El resultado es: {resultado}")
            break

