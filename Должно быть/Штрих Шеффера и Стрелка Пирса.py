# artyomshutoff
from Post_classification import post
import ttg_fix as ttg
import numpy as np
from to_nand_nor import to_nand, to_nor
out = []
print('Вариант 29 f(x, y) ПМ-21-2 Шутов А.С.')

print('')
print('а)')
print(ttg.Truths(['x', 'y'], ['(y = x) or y', to_nand('(y = x) or y'), to_nor('(y = x) or y')], ascending = True).as_prettytable())

print('')
print('б)')
print(ttg.Truths(['x', 'y'], ['(x or (not y => x)) nor y', to_nand('(x or (not y => x)) nor y'), to_nor('(x or (not y => x)) nor y')], ascending = True).as_prettytable())

print('')
print('в)')
print(ttg.Truths(['x', 'y'], ['(not y and x) xor ((y and not x) nor not x)', to_nand('(not y and x) xor ((y and not x) nor not x)'), to_nor('(not y and x) xor ((y and not x) nor not x)')], ascending = True).as_prettytable())
