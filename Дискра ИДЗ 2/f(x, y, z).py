# artyomshutoff
from pdnf_pcnf import truth2pdnf, truth2pcnf
from pdnf_pcnf4check import truth2pdnf4check, truth2pcnf4check
import ttg_fix as ttg
print('Вариант 29 f(x, y, z) ПМ-21-2 Шутов А.С.')

print('')
print('а)')
print(ttg.Truths(['x', 'y', 'z'], ['y and x', '(y and x) nand z'], ascending = True).as_prettytable())
A = ttg.Truths(['x', 'y', 'z'], ['(y and x) nand z'], ascending = True).as_pandas().to_numpy()

print('')
print('СДНФ:')
print(ttg.Truths(['x', 'y', 'z'], truth2pdnf4check(A, 'xyz'), ascending = True).as_prettytable())

print('')
print('СКНФ:')
print(ttg.Truths(['x', 'y', 'z'], truth2pcnf4check(A, 'xyz'), ascending = True).as_prettytable())

print('')
print('б)')
print(ttg.Truths(['x', 'y', 'z'], ['not y or z', 'y xor (not y or z)', 'x nor (y xor (not y or z))'], ascending = True).as_prettytable())
A = ttg.Truths(['x', 'y', 'z'], ['x nor (y xor (not y or z))'], ascending = True).as_pandas().to_numpy()

print('')
print('СДНФ:')
print(ttg.Truths(['x', 'y', 'z'], truth2pdnf4check(A, 'xyz'), ascending = True).as_prettytable())

print('')
print('СКНФ:')
print(ttg.Truths(['x', 'y', 'z'], truth2pcnf4check(A, 'xyz'), ascending = True).as_prettytable())

print('')
print('в)')
print(ttg.Truths(['x', 'y', 'z'], ['z nor y', 'y = x', '(z nor y) xor (y = x)', '(z nor y) xor (y = x) and not x'], ascending = True).as_prettytable())
A = ttg.Truths(['x', 'y', 'z'], ['(z nor y) xor (y = x) and not x'], ascending = True).as_pandas().to_numpy()

print('')
print('СДНФ:')
print(ttg.Truths(['x', 'y', 'z'], truth2pdnf4check(A, 'xyz'), ascending = True).as_prettytable())

print('')
print('СКНФ:')
print(ttg.Truths(['x', 'y', 'z'], truth2pcnf4check(A, 'xyz'), ascending = True).as_prettytable())