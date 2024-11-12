#calculadora

#Ingreso de numeros y operacion a realizar
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
operacion = input("Ingrese la operación (+, -, *, /): ")
print()

#Si se elije una operacion no disponible
while operacion != "+" and operacion != "-" and operacion != "*" and operacion != "/":
    operacion = input("Esa operacion no esta disponible, elija otra: ")

#Cálculo
if operacion == "+":
    print(f'El resultado de {a} más {b} es:', a + b)
elif operacion == "-":
    print(f'El resultado de {a} menos {b} es: ', a - b)
elif operacion == "*":
    print(f'El resultado de {a} multiplicado por {b} es: ', a * b)
elif operacion == "/":
    while b == 0:
        b = float(input("No se puede divir un número por 0, ingrese otro divisor: "))
    print(f'El resultado de {a} dividido {b} es:', round(a / b, 2))
    
print()
print("BIEN HECHO! ¿Por qué no intentas realizar otra operación?")    
