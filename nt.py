'''
    Python implementation of various functions and algorithems
    useful in number theory.
'''


def gcd(a, b):
    # by Euclidian Algorithem
    if a < b:
        t = a
        a = b
        b = t
    q = a % b
    while q != 0:
        a = b
        b = q
        q = a % b
    return b


def possibleOrders(og):
    # By Lagrange, the order of the element must divide the order of the group
    ords = []
    for o in range(1, (og // 2) + 2):  # do we really need + 2?
        if og % o == 0:
            ords.append(o)
    ords.append(og)
    return ords


def primativeRoots(p):
    # finds primitive roots (elements with order p - 1) in (Z/p)*
    prs = []
    for e in range(1, p - 1):
        if e ** (p - 1) % p == 1:
            prim = True
            for o in possibleOrders(p - 1)[0:-1]:
                if e ** o % p == 1:
                    prim = False
            if prim:
                prs.append(e)
    return prs


def multOrders(mod, prnt=False):
    # orders of elements in the group (Z/mod)*
    elems = []
    pairs = []
    elems.append(1)
    for pe in range(2, mod - 1):
        if mod % pe != 0:
            elems.append(pe)
    ords = possibleOrders(mod - 1)
    for e in elems:
        for o in ords:
            if e ** o % mod == 1:
                pairs.append((e, o))
                if prnt:
                    print(f'{e} has order {o}')
                break
    if prnt:
        print(f'in (Z/{mod})*')
    return pairs


def addOrders(mod, prnt=False):
    # orders of elements in the group Z/og
    elems = range(mod)
    pairs = []
    ords = possibleOrders(mod)
    for e in elems:
        for o in ords:
            if e * o % mod == 0:
                pairs.append((e, o))
                if prnt:
                    print(f'{e} has order {o}')
                break
    if prnt:
        print(f'in Z/{mod}')
    return pairs


def quadraticResidues(p):
    return sorted(set([a ** 2 % p for a in range(1, p - 1) if a % p != 0]))


def squares(p):
    es = [e for e in range(1, p)]
    sqs = [a ** 2 % p for a in range(1, p)]
    return list(zip(es, sqs))
