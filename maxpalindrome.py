from collections import defaultdict
from copy import copy

M = int(1e9) + 7
fact = [1]
for i in range(1, int(1e5) + 10):
    fact.append(fact[-1] * i % M)

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


memo = {}


def modinv(a, m):
    if a in memo:
        return memo[a]
    while a < 0:
        a += m
    g, x = egcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        memo[a] = x % m
        return x % m


s = input('String: ').strip()
occ = [defaultdict(int)]
for ch in s:
    newd = copy(occ[-1])
    newd[ch] += 1
    occ.append(newd)


def query(l, r):
    d = defaultdict(int)
    for ch in occ[r]:
        d[ch] += occ[r][ch]
    for ch in occ[l - 1]:
        d[ch] -= occ[l - 1][ch]

    odds = 0
    for k, v in copy(d).items():
        if v & 1:
            odds += 1
        d[k] = v - (v & 1)

    res = 1
    total = 0
    for k, v in d.items():
        res *= modinv(fact[v // 2], M)
        total += v // 2
        res %= M
    return (max(1, odds) * res * fact[total]) % M


for _ in range(int(input('Integer days: '))):
    l, r = map(int, input('sub string: ').split())
    print(query(l, r))