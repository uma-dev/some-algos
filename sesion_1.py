def base(n, b):
    """Toma un numero y una base y da sus coeficientes"""
    if n < b:
        return [n]
    return base(n // b, b) + [n % b]


print(base(11, 2))


def horner(coeficientes, x):
    """Toma una lista de coeficientes y una base y la evalua"""
    if len(coeficientes) == 0:
        return 0
    return horner(coeficientes[1:], x) * x + coeficientes[0]


coef = [1, 2, 3, 4]
print(horner(coef, 2))


def binario(n):
    """Toma un numero y da sus coeficientes base 2"""
    if n < 2:
        return [n]
    # return binario(n // 2) + [n % 2]
    # Se cambia el orden para que sea compatible con la funcion que calcula el residuo
    return [n % 2] + binario(n // 2)


def residuo(b, x, r):
    """algoritmo de residuos cuadraticos corazon del algoritmo para encriptar"""
    l = []
    a = binario(x)
    n = len(a)
    for i in range(n):
        c = b % r
        l = l + [c]
        b = c * c
    s = 1
    for i in range(n):
        if a[i] == 1:
            s = s * l[i]
            s = s % r
    return s, l


print(residuo(13, 11, 9))


def euclides(a, b):
    """Algoritmo de euclides para encontrar MCD"""
    if a == 0:
        return b
    if b == 0:
        return a
    return euclides(b, a % b)


print(euclides(1, 0))
print(euclides(6, 0))
print(euclides(60, 40))


def phi(n):
    """cuenta la cantidad de enteros positivos menores o iguales a n que son coprimos con n."""
    count = 0
    for i in range(1, n + 1):
        if euclides(n, i) == 1:
            count += 1
    return count


print(phi(10))
