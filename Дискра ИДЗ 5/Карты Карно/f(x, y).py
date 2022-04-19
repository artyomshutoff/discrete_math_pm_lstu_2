# artyomshutoff
import ttg_fix as ttg
from carnot_map import carnot
print('Вариант 29 f(x, y) ПМ-21-2 Шутов А.С.')

print('')
print('а)')
print(ttg.Truths(['x', 'y'], ['(y = x) or y'], ascending = True).as_prettytable())
print('')
carnot('(y = x) or y', 'xy')

print('')
print('б)')
print(ttg.Truths(['x', 'y'], ['(x or (not y => x)) nor y'], ascending = True).as_prettytable())
print('')
carnot('(x or (not y => x)) nor y', 'xy')

print('')
print('в)')
print(ttg.Truths(['x', 'y'], ['(not y and x) xor ((y and not x) nor not x)'], ascending = True).as_prettytable())
print('')
carnot('(not y and x) xor ((y and not x) nor not x)', 'xy')