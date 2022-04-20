# artyomshutoff
import ttg_fix as ttg
from carnot_map import carnot
print('Вариант 29 f(x, y, z, t) ПМ-21-2 Шутов А.С.')

print('')
print('а)')
print(ttg.Truths(['x', 'y', 'z', 't'], ['((z and x) xor y) nor t'], ascending = True).as_prettytable())
print('')
carnot('((z and x) xor y) nor t', 'xyzt')

print('')
print('б)')
print(ttg.Truths(['x', 'y', 'z', 't'], ['((not x) nor ((not y) or z)) = ((not y) nor (not t))'], ascending = True).as_prettytable())
print('')
carnot('((not x) nor ((not y) or z)) = ((not y) nor (not t))', 'xyzt')

print('')
print('в)')
print(ttg.Truths(['x', 'y', 'z', 't'], ['(t = (z xor (x and y))) = ((not x) or (not y))'], ascending = True).as_prettytable())
print('')
carnot('(t = (z xor (x and y))) = ((not x) or (not y))', 'xyzt')