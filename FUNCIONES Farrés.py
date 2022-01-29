def calcularFactorial(n):
    return 1 if (n == 1 or n == 0) else n * calcularFactorial(n - 1);


def factorial(n):
    print(f"El factorial de {str(n)} es {str(calcularFactorial(n))}")


def sum(x, y):
    result = 0
    if x < y:
        for num in range(x, y+1):
            result += num
        print(result)
    else:
        print(f"El primer numero de ingresado({x}) no puede ser mayor que el segundo({y})")

sum(7,5)