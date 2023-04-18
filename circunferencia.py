import math

def circunferencia(radio):
    return radio*radio*math.pi

try:
    num = float(input("Ingrese el radio del círculo: "))
except ValueError:
    print("Debe ser un valor válido.")

area = circunferencia(num)
print(f'Area: {area}')
