"""
CAPES NANCY-METZ 2018
"""


from math import *


# --------------------------------------
# --
# -- PROBLEME I
# --
# --------------------------------------


def lucas1(n):
    if n == 0:
        return 2
    phi = (1 + sqrt(5)) / 2
    phi2 = (1 - sqrt(5)) / 2
    return phi ** n + phi2 ** n


def lucas2(n):
    if n == 0:
        return 2
    phi = (1 + sqrt(5)) / 2
    if n%2 == 0:
        return ceil(phi ** n)
    else:
        return floor(phi ** n)

def lucas3(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        a, b = 2, 1
        for i in range(n):
            a, b = b, a + b
        return a

def lucas4(n):
    if n == 0:
        return 2, 1
    elif n == 1:
        return 1, 3
    else:
        k = n // 2
        u = 1 - 2 * (k % 2)
        a, b = lucas4(k)
        print(a,b)
        if n % 2 == 0:
            return a*a - 2*u, a*b - u
        else:
            return a*b - u, b*b - 2*u


def prodMat(m1, m2):
    m = [[0,0], [0, 0]]
    for row in range(2):
        for col in range(2):
            for k in range(2):
                m[row][col] +=  m1[row][k] * m2[k][col]
    return m

def puissMatRap(m, n):
    r = [[1, 0], [0, 1]]
    p = m
    while n > 0:
        if n%2 == 1:
            r = prodMat(r, p)
        p = prodMat(p, p)
        n = n // 2
    return r

def lucas5(n):
    r = [[2, 0], [1, 0]]
    a = [[0, 1], [1, 1]]
    a = puissMatRap(a, n)
    r = prodMat(a, r)
    return r[0][0]




# ma_liste = [lucas3(i) for i in range(8)]
# print(lucas2(36))
# print(lucas3(36))
# print(lucas4(36))
# print(lucas5(36))
# print(lucas4(4))


# --------------------------------------
# --
# -- PROBLEME II
# --
# --------------------------------------


def alloc(salles, cours):
    cours.sort()
    for (deb, fin) in cours:
        affecte = False
        for salle in salles:
            last_cm = salle[-1]
            if deb >= last_cm[1]:
                salle.append((deb, fin))
                affecte = True
                break
        if not affecte:
            salles.append([(deb, fin)])

cours_1 = [(0,7), (2,13), (8,10)]
cours_2 = [(0,2), (1,7), (4,11), (5,6), (8,10), (9,13)]
# salles = []
# alloc(salles, cours_2)
# print(salles)

def insere(l, elt):
    index = 0
    while index < len(l) and elt > l[index]:
        index += 1
    l.insert(index, elt) 

# l = [1,2,4,5]
# insere(l,3)
# print(l)
# l2 = []
# insere(l2, 10)
# print(l2)
# l3 = [1,2,3]
# insere(l3,4)
# print(l3)

def smaller(l1, l2):
    return l1[0] <= l2[0]

def insereBis(ll, li):
    index = 0
    while index < len(ll) and not smaller(li, ll[index]):
        index += 1
    ll.insert(index, li)

# ll = [[1,5],[4,9]]
# li = [2,10]
# insere(ll,li)
# print(ll)


def traduit(l_intervalles):
    l_instants = []
    for index, (deb, fin) in enumerate(l_intervalles):
        l_instants.extend([[deb, index, 0], [fin, index, 1]])
    return l_instants


def agenda(l_evt):
    cal = []
    for evt in l_evt:
        insereBis(cal, evt)
    return cal

def intersection_max(agenda):
    maxi = 1
    c = 0
    for e in agenda:
        c += 1 - 2*e[2]
        if c > maxi:
            maxi = c
    return maxi

def nbr_optimal(l_intervalles):
    l_instants = traduit(l_intervalles)
    cal = agenda(l_instants)
    return intersection_max(cal)


def plus_petit_vrai(liste):
    i = 0
    n = len(liste)
    while i < n and not liste[i]:
        i += 1
    if i == n:
        return -1
    else:
        return i

def allocation(l_intervalles):
    l_instants = traduit(l_intervalles)
    liste = agenda(l_instants)
    nb_cours = len(l_intervalles)
    nb_salles = nbr_optimal(l_intervalles)
    salles_dispos = [True] * nb_salles
    alloc = [-1] * nb_cours
    for l in liste:
        if l[2] == 0:
            alloc[l[1]] = plus_petit_vrai(salles_dispos)
            salles_dispos[alloc[l[1]]] = False
        else:
            salles_dispos[alloc[l[1]]] = True
    return alloc

print(allocation(cours_1))
print(allocation(cours_2))




# l_evt_1 = traduit(cours_1)
# l_evt_2 = traduit(cours_2)
# print(l_evt_1)
# agenda_1 = agenda(l_evt_1)
# agenda_2 = agenda(l_evt_2)
# print(agenda_1)
# print(agenda_2)

# print(intersection_max(agenda_2))
# print(nbr_optimal(cours_2))



