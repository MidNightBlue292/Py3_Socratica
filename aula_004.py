example = set()  # Não memoriza duplicados e não importa a ordem
example.add(42)
example.add(False)
example.add(3.14159)
example.add('Thor')
print(example)
print(len(example))
example.remove(42)  # se não existir dá erro
example.discard(50)  # se não existir não dá erro
print(example)
print()

example2 = set([28, True, 2.789, 'Hell'])
print(example2)
print(len(example2))
example2.clear()
print(len(example2))

odds = set([10, 20, 30, 40, 50])
evens = set([15, 25, 35, 45, 55])
primes = set([15, 25, 40])
composites = set([10, 30, 40, 55])

print(odds.union(evens))  # Junta tudo
print(evens.union(odds))
print(sorted(odds.union(evens)))
print(evens.intersection(primes))
print(15 in primes)
print(16 in primes)
print(150 not in primes)
