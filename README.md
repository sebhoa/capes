# Capes 2018

Le sujet est ici : [EP1_Info_2018.pdf][1]

J'espère ne pas avoir fait trop de coquilles :laughing:

## Problème I

### Question VI

#### Exo 1

```python
def lucas1(n):
    if n == 0:
        return 2
    phi = (1 + sqrt(5)) / 2
    phi2 = (1 - sqrt(5)) / 2
    return phi ** n + phi2 ** n
```

```python
[lucas1(i) for i in range(8)]
>>> [2, 1.0, 3.0, 4.0, 7.000000000000001, 11.000000000000002, 18.000000000000004, 29.000000000000007]
```

**Pourquoi les valeurs ne sont pas entières ?**

La liste n'est pas une liste d'entiers car `phi` (et `phi2`) est un `float` et donc la fonction `lucas1` retourne un `float`


#### Exo 2

```python
def lucas2(n):
    if n == 0:
        return 2
    phi = (1 + sqrt(5)) / 2
    if n%2 == 0:
        return ceil(phi ** n)
    else:
        return floor(phi ** n)
```

1. Expliquer le choix et démontrer que si le calcul des flottants est exact alors `lucas2(n)` calcule bien `Ln`.
2. `L36` vaut  33385282 alors que `lucas2(36)` retourne  33385283 à cause de l'erreur d'arrondi sur `phi`

### Question VII

```python
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
```

**Invariant :** Pour tout `n ≥ 1` on a `a` qui vaut `Ln` et `b` `L(n+1)` Pour `n ≥ 2` `lucas3(n)` effectue n additions.


### Question IX

1. Si k est un entier `1 - 2*(k % 2)` vaut 0 quand k est pair et -1 sinon.
2. 

```python
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
```

Pour `lucas4(n)` il y aura `floor(log2(n))` appels récursifs. 


### Question XI

1. 
```python
def prodMat(m1, m2):
    m = [[0,0], [0, 0]]
    for row in range(2):
        for col in range(2):
            for k in range(2):
                m[row][col] +=  m1[row][k] * m2[k][col]
    return m
```

2. L'appel à `prodMat` effectue 8 multiplications et 4 additions.
3. La version naïve de `puissanceMat` effectue p multiplications de matrice

### Question XII

```python
def puissMatRap(m, n):
    r = [[1, 0], [0, 1]]
    p = m
    while n > 0:
        if n%2 == 1:
            r = prodMat(r, p)
        p = prodMat(p, p)
        n = n // 2
    return r
```


### Question XIII


```python
def lucas5(n):
    r = [[2, 0], [1, 0]]
    a = [[0, 1], [1, 1]]
    a = puissMatRap(a, n)
    r = prodMat(a, r)
    return r[0][0]
```


## Problème II

### Question I

#### Algorithme (naïf)

On parcourt les cours par ordre croissant de début. On parcourt les salles par ordre croissant de numéro : si ce début est supérieur à la fin de la salle courante, on affecte à cette salle sinon on en prend une autre. Si on n'en trouve aucune on affecte une nouvelle salle

Voici les allocations obtenues :
![Allocations Exemple 1](/pII_ex1_affectation.png)
![Allocations Exemple 2](/pII_ex2_affectation.png)

#### Le nombre minimal de salles 

Pour l'exemple 1 est 2, et c'est 3 pour le deuxième exemple.


### Question II

On modélise par la liste `[d, f]` un cours se déroulant sur l'intervalle mathématique `[d, f[`.


#### Les modélisations

```python
cours_1 = [[0,7], [2,13], [8,10]]
cours_2 = [[0,2], [1,7], [4,11], [5,6], [8,10], [9,13]]
```

#### Insérer dans une liste triée

```python
def insere(l, elt):
    index = 0
    while index < len(l) and elt > l[index]:
        index += 1
    l.insert(index, elt)
```

### Question III

#### La fonction `traduit` 

```python
def traduit(l_intervalles):
    l_instants = []
    for index, (deb, fin) in enumerate(l_intervalles):
        l_instants.extend([[deb, index, 0], [fin, index, 1]])
    return l_instants
```


#### Agendas des exemples

```python
agenda_1 = [[0, 0, 0], [2, 1, 0], [7, 0, 1], [8, 2, 0], [10, 2, 1], [13, 1, 1]]
agenda_2 = [[0, 0, 0], [1, 1, 0], [2, 0, 1], [4, 2, 0], 
            [5, 3, 0], [6, 3, 1], [7, 1, 1], [8, 4, 0], 
            [9, 5, 0], [10, 4, 1], [11, 2, 1], [13, 5, 1]]
```


#### La fonction `agenda`

```python
def agenda(l_evt):
    cal = []
    for evt in l_evt:
        insereBis(cal, evt)
    return cal
```


### Question IV

#### Les fonctions `valide` 

Les réponses correctes sont les définitions `valideB` et `valideD` 


#### Définition de `intersection_max` 

```python
def intersection_max(agenda):
    maxi = 1
    c = 0
    for e in agenda:
        c += 1 - 2*e[2]
        if c > maxi:
            maxi = c
    return maxi
```
**Justification :** à chaque fois qu'on croise un début on incrémente notre compteur `c`. Et on mémorise la valeur maximale atteinte c'est-à-dire le nombre maximal d'intervalles commencés mais non terminés (on n'a pas croisé la fin et donc on n'a pas décrémenté le compteur) ce qui correspond à notre définition.

#### Définition de la fonction `nbr_optimal`

```python
def nbr_optimal(l_intervalles):
    l_instants = traduit(l_intervalles)
    cal = agenda(l_instants)
    return intersection_max(cal)
```

### Question V

#### Plus indice de True

Version élève :
```python
def plus_petit_vrai(liste):
    n = len(liste)
    while liste[i] and (i < n):
        i += 1
    if i = n:
        return -1
    else:
        return i
```

Version corrigée :
```python
def plus_petit_vrai(liste):
    i = 0
    n = len(liste)
    while i < n and not liste[i]:
        i += 1
    if i == n:
        return -1
    else:
        return i
```

#### La fonction d'allocation

```python
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
```

[1]:http://www4.ac-nancy-metz.fr/capesmath/data/uploads/EP1_info_2018.pdf

