# artyomshutoff
import ttg_fix as ttg
from minimization import direct_minimization
print('Вариант 29 f(x, y, z, t) ПМ-21-2 Шутов А.С.')

print('а)')
print(ttg.Truths(['x', 'y', 'z', 't'], ['((z and x) xor y) nor t'], ascending = True).as_prettytable())
direct_minimization('((z and x) xor y) nor t', 'xyzt')

print('б)')
print(ttg.Truths(['x', 'y', 'z', 't'], ['((not x) nor ((not y) or z)) = ((not y) nor (not t))'], ascending = True).as_prettytable())
direct_minimization('((not x) nor ((not y) or z)) = ((not y) nor (not t))', 'xyzt')

print('в)')
print(ttg.Truths(['x', 'y', 'z', 't'], ['(t = (z xor (x and y))) = ((not x) or (not y))'], ascending = True).as_prettytable())
direct_minimization('(t = (z xor (x and y))) = ((not x) or (not y))', 'xyzt')