# geometria.py

def calcular_area(base: float, altura: float) -> float:
    """Calcula el área de un rectángulo."""
    if not isinstance(base, (int, float)) or not isinstance(altura, (int, float)):
        raise TypeError("La base y la altura deben ser valores numéricos (int o float).")
    
    if base < 0 or altura < 0:
        raise ValueError("Dimensiones no pueden ser negativas")
        
    return float(base * altura)

def sumar(a, b):

    return a + b

 

def restar(a, b):

    return a - b

def multiplicar(a, b):
    return a * b

 
if __name__ == "__main__":
    print("Calculadora simple")
    print("2 + 3 =", sumar(2, 3))
    print("10 - 4 =", restar(10, 4))
    print("4 * 5 =", multiplicar(4, 5))