# artyomshutoff
import ttg_fix as ttg
from minimization import mdnf, mcnf
from itertools import product
print('Вариант 29 f(x, y, z) ПМ-21-2 Шутов А.С.')

print('')
print('а)')
print(ttg.Truths(['x', 'y', 'z'], ['y and x', '(y and x) nand z'], ascending = True).as_prettytable())
A = []
for x, y, z in product([0, 1], repeat = 3):
	A.append([x, y, z, int(not((y and x) and z))])

print('')
print('Минимизированная ДНФ:')
print(ttg.Truths(['x', 'y', 'z'], [mdnf(A, 'xyz')], ascending = True).as_prettytable())
print('')
print('Минимизированная СКНФ')
print(ttg.Truths(['x', 'y', 'z'], [mcnf(A, 'xyz')], ascending = True).as_prettytable())

print('')
print('б)')
print(ttg.Truths(['x', 'y', 'z'], ['not y or z', 'y xor (not y or z)', 'x nor (y xor (not y or z))'], ascending = True).as_prettytable())
A = []
for x, y, z in product([0, 1], repeat = 3):
	A.append([x, y, z, int(not(x or (y != ((not y) or z))))])

print('')
print('Минимизированная ДНФ:')
print(ttg.Truths(['x', 'y', 'z'], [mdnf(A, 'xyz')], ascending = True).as_prettytable())
print('')
print('Минимизированная СКНФ')
print(ttg.Truths(['x', 'y', 'z'], [mcnf(A, 'xyz')], ascending = True).as_prettytable())

print('')
print('в)')
print(ttg.Truths(['x', 'y', 'z'], ['z nor y', 'y = x', '(z nor y) xor (y = x)', '(z nor y) xor (y = x) and not x'], ascending = True).as_prettytable())
A = []
for x, y, z in product([0, 1], repeat = 3):
	A.append([x, y, z, int((not (z or y)) != (((y == x) and (not x))))])

print('')
print('Минимизированная ДНФ:')
print(ttg.Truths(['x', 'y', 'z'], [mdnf(A, 'xyz')], ascending = True).as_prettytable())
print('')
print('Минимизированная СКНФ')
print(ttg.Truths(['x', 'y', 'z'], [mcnf(A, 'xyz')], ascending = True).as_prettytable())