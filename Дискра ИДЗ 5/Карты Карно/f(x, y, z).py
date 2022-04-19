# artyomshutoff
import ttg_fix as ttg
from carnot_map import carnot
print('Вариант 29 f(x, y, z) ПМ-21-2 Шутов А.С.')

print('')
print('а)')
print(ttg.Truths(['x', 'y', 'z'], ['(y and x) nand z'], ascending = True).as_prettytable())
print('')
carnot('(y and x) nand z', 'xyz')

print('')
print('б)')
print(ttg.Truths(['x', 'y', 'z'], ['x nor (y xor (not y or z))'], ascending = True).as_prettytable())
print('')
carnot('x nor (y xor (not y or z))', 'xyz')

print('')
print('в)')
print(ttg.Truths(['x', 'y', 'z'], ['(z nor y) xor (y = x) and not x'], ascending = True).as_prettytable())
print('')
carnot('(z nor y) xor (y = x) and not x', 'xyz')