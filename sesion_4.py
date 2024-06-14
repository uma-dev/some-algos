def conjunto_potencia(a):
    if len(a) == 1:
        return [[], a]
    lst = []
    b = conjunto_potencia(a[1:])
    for i in b:
        aux = [a[0]] + i
        lst = lst + [aux]
    return b + lst


print(conjunto_potencia([0, 1, 2, 3]))


def selec(a, p, m):
    s = conjunto_potencia(a)
    r = []
    for i in s:
        if checa(i, p, m):
            r = r + [i]
    return r


def checa(lst, p, m):
    s = 0
    for k in lst:
        s = s + p[k]
    return s < m


def max_val(a, b):
    m_val = -1
    m_sol = a[0]
    for i in a:
        if val(i, b) > m_val:
            m_val = val(i, b)
            m_sol = i
    return m_sol, m_val


def val(lst, b):
    r = 0
    for i in lst:
        r = r + b[i]
    return r


m = 6
b = [3, 2, 4, 4]
P = [4, 3, 2, 3]
a = [0, 1, 2, 3]
r = selec(a, P, m)
print(max_val(r, b))
