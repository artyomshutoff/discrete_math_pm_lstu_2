# artyomshutoff
from Zhegalkin_polynomial import Zhegalkin_build
import ttg_fix as ttg
print('Вариант 29 f(x, y, z) ПМ-21-2 Шутов А.С.')

print('')
print('а)')
print(ttg.Truths(['x', 'y', 'z'], ['y and x', '(y and x) nand z'], ascending = True).as_prettytable())
A = ttg.Truths(['x', 'y', 'z'], ['(y and x) nand z'], ascending = True).as_pandas().to_numpy().tolist()

print('')
print('Полином Жегалкина:')
print(ttg.Truths(['x', 'y', 'z'], [Zhegalkin_build(A, 'xyz')], ascending = True).as_prettytable())

print('')
print('б)')
print(ttg.Truths(['x', 'y', 'z'], ['not y or z', 'y xor (not y or z)', 'x nor (y xor (not y or z))'], ascending = True).as_prettytable())
A = ttg.Truths(['x', 'y', 'z'], ['x nor (y xor (not y or z))'], ascending = True).as_pandas().to_numpy().tolist()

print('')
print('Полином Жегалкина:')
print(ttg.Truths(['x', 'y', 'z'], [Zhegalkin_build(A, 'xyz')], ascending = True).as_prettytable())

print('')
print('в)')
print(ttg.Truths(['x', 'y', 'z'], ['z nor y', 'y = x', '(z nor y) xor (y = x)', '(z nor y) xor (y = x) and not x'], ascending = True).as_prettytable())
A = ttg.Truths(['x', 'y', 'z'], ['(z nor y) xor (y = x) and not x'], ascending = True).as_pandas().to_numpy().tolist()

print('')
print('Полином Жегалкина:')
print(ttg.Truths(['x', 'y', 'z'], [Zhegalkin_build(A, 'xyz')], ascending = True).as_prettytable())