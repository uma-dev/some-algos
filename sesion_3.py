def inserta(x, lst, i):
    return lst[:i] + [x] + lst[i:]


def inserta_multiple(x, lst):
    return [inserta(x, lst, i) for i in range(len(lst) + 1)]


lista = [1, 2, 3]
print("inserta_multiple", inserta_multiple(0, lista))


def permuta(c):
    if len(c) == 0:
        return [[]]
    lst = []
    for i in permuta(c[1:]):
        lst = lst + inserta_multiple(c[0], i)
    return lst


print("permutaciones", permuta(lista))


def sgn(p):
    # Calcula el numero de inversiones en unapermutacion a y clacular su signo
    count = 0
    i = -1
    a = []

    for k in range(len(p)):
        a = a + [p[k]]

    while i < len(a) - 2:
        i += 1
        if a[i] > a[i + 1]:
            aux = a[i]
            a[i] = a[i + 1]
            a[i + 1] = aux
            count = count + 1
            i = -1
            continue

    if count % 2 == 0:
        return 1
    return -1


def det(a):
    # Calcula el determinante de la matriz a
    n = len(a)
    s = range(n)
    t = permuta(s)
    d = 0
    for u in t:
        for i in range(n):
            r = r * a[i, u[i]]
        d = d + r
    return d
