def calcularFactorial(n):
    return 1 if (n == 1 or n == 0) else n * calcularFactorial(n - 1);
def factorial(n):
    print(f"El factorial de {str(n)} es {str(calcularFactorial(n))}")

factorial(5)    