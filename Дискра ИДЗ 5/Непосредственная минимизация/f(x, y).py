# artyomshutoff
import ttg_fix as ttg
from minimization import direct_minimization
print('Вариант 29 f(x, y) ПМ-21-2 Шутов А.С.')

print('а)')
print(ttg.Truths(['x', 'y'], ['(y = x) or y'], ascending = True).as_prettytable())
direct_minimization('(y = x) or y', 'xy')

print('б)')
print(ttg.Truths(['x', 'y'], ['(x or (not y => x)) nor y'], ascending = True).as_prettytable())
direct_minimization('(y = x) or y', 'xy')

print('в)')
print(ttg.Truths(['x', 'y'], ['(not y and x) xor ((y and not x) nor not x)'], ascending = True).as_prettytable())
print('')
direct_minimization('(not y and x) xor ((y and not x) nor not x)', 'xy')