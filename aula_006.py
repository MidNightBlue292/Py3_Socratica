import sys  # print(dir(sys))
import timeit
print(help(sys.getsizeof))
print()

# Lists: add data, remove data, change data
list_ex = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', True, 3.14]

# Tuples: cannot be changed, "Immutable", made quickly
tuple_ex = (1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', True, 3.14)

print('List size = ', sys.getsizeof(list_ex))
print('Tuple size = ', sys.getsizeof(tuple_ex))
print()

list_test = timeit.timeit(stmt='[1,2,3,4,5]', number=1000000)
tuple_test = timeit.timeit(stmt='(1,2,3,4,5)', number=1000000)
print('List time = ', list_test)
print('Tuple time = ', tuple_test)
print()

# Modo 1
survey = (27, 'Vietnam', True)
age = survey[0]
country = survey[1]
knows_python = survey[2]
print(age, country, knows_python)
print()

# Modo 2
age, country, knows_python = survey
print(age, country, knows_python)
print()
