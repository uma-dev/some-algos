def euclidex(a, b):
    """Version extendida de euclides"""
    if a % b == 0:
        return 0, 1, b
    A, B, C = euclidex(b, a % b)
    qk = a // b
    return B, A - B * (qk), C


print(euclidex(12, 18))
print(euclidex(18, 12))


def bezout(a, b, m, n):
    """calcula m,n pero fuerza a que el segundo es positivo"""
    while n < 0:
        m = m - b
        n = n + a
    return m, n


print(bezout(18, 12, 1, -1))
