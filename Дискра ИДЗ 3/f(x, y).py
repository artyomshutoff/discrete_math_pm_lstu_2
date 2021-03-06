# artyomshutoff
from Zhegalkin_polynomial import Zhegalkin_build
import ttg_fix as ttg
print('Вариант 29 f(x, y) ПМ-21-2 Шутов А.С.')

print('')
print('а)')
print(ttg.Truths(['x', 'y'], ['y = x', '(y = x) or y'], ascending = True).as_prettytable())
A = ttg.Truths(['x', 'y'], ['(y = x) or y'], ascending = True).as_pandas().to_numpy().tolist()

print('')
print('Полином Жегалкина:')
print(ttg.Truths(['x', 'y'], [Zhegalkin_build(A, 'xy')], ascending = True).as_prettytable())

print('')
print('б)')
print(ttg.Truths(['x', 'y'], ['not y => x', 'x or (not y => x)', '(x or (not y => x)) nor y'], ascending = True).as_prettytable())
A = ttg.Truths(['x', 'y'], ['(x or (not y => x)) nor y'], ascending = True).as_pandas().to_numpy().tolist()

print('')
print('Полином Жегалкина:')
print(ttg.Truths(['x', 'y'], [Zhegalkin_build(A, 'xy')], ascending = True).as_prettytable())

print('')
print('в)')
print(ttg.Truths(['x', 'y'], ['not y and x', 'y and not x', '(y and not x) nor not x', '(not y and x) xor ((y and not x) nor not x)'], ascending = True).as_prettytable())
A = ttg.Truths(['x', 'y'], ['(not y and x) xor ((y and not x) nor not x)'], ascending = True).as_pandas().to_numpy().tolist()

print('')
print('Полином Жегалкина:')
print(ttg.Truths(['x', 'y'], [Zhegalkin_build(A, 'xy')], ascending = True).as_prettytable())