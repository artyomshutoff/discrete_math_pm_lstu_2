# artyomshutoff
import ttg_fix as ttg
from minimization import mdnf, mcnf
print('Вариант 29 f(x, y, z, t) ПМ-21-2 Шутов А.С.')

print('')
print('а)')
print(ttg.Truths(['x', 'y', 'z', 't'], ['((z and x) xor y) nor t'], ascending = True).as_prettytable())
A = ttg.Truths(['x', 'y', 'z', 't'], ['((z and x) xor y) nor t'], ascending = True).as_pandas().to_numpy().tolist()

print('')
print('Минимизированная ДНФ:')
print(ttg.Truths(['x', 'y', 'z', 't'], [mdnf(A, 'xyzt')], ascending = True).as_prettytable())
print('')
print('Минимизированная КНФ')
print(ttg.Truths(['x', 'y', 'z', 't'], [mcnf(A, 'xyzt')], ascending = True).as_prettytable())

print('')
print('б)')
print(ttg.Truths(['x', 'y', 'z', 't'], ['((not x) nor ((not y) or z)) = ((not y) nor (not t))'], ascending = True).as_prettytable())
A = ttg.Truths(['x', 'y', 'z', 't'], ['((not x) nor ((not y) or z)) = ((not y) nor (not t))'], ascending = True).as_pandas().to_numpy().tolist()

print('')
print('Минимизированная ДНФ:')
print(ttg.Truths(['x', 'y', 'z', 't'], [mdnf(A, 'xyzt')], ascending = True).as_prettytable())
print('')
print('Минимизированная КНФ')
print(ttg.Truths(['x', 'y', 'z', 't'], [mcnf(A, 'xyzt')], ascending = True).as_prettytable())

print('')
print('в)')
print(ttg.Truths(['x', 'y', 'z', 't'], ['(t = (z xor (x and y))) = ((not x) or (not y))'], ascending = True).as_prettytable())
A = ttg.Truths(['x', 'y', 'z', 't'], ['(t = (z xor (x and y))) = ((not x) or (not y))'], ascending = True).as_pandas().to_numpy().tolist()

print('')
print('Минимизированная ДНФ:')
print(ttg.Truths(['x', 'y', 'z', 't'], [mdnf(A, 'xyzt')], ascending = True).as_prettytable())
print('')
print('Минимизированная КНФ')
print(ttg.Truths(['x', 'y', 'z', 't'], [mcnf(A, 'xyzt')], ascending = True).as_prettytable())