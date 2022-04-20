# artyomshutoff
import ttg_fix as ttg
from minimization import direct_minimization
print('Вариант 29 f(x, y, z) ПМ-21-2 Шутов А.С.')

print('а)')
print(ttg.Truths(['x', 'y', 'z'], ['(y and x) nand z'], ascending = True).as_prettytable())
direct_minimization('(y and x) nand z', 'xyz')

print('б)')
print(ttg.Truths(['x', 'y', 'z'], ['x nor (y xor (not y or z))'], ascending = True).as_prettytable())
direct_minimization('x nor (y xor (not y or z))', 'xyz')

print('в)')
print(ttg.Truths(['x', 'y', 'z'], ['(z nor y) xor (y = x) and not x'], ascending = True).as_prettytable())
direct_minimization('(z nor y) xor (y = x) and not x', 'xyz')