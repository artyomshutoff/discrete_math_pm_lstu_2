# artyomshutoff
import ttg_fix as ttg
import numpy as np
from to_nand_nor import to_nand
out = []
print('Вариант 29 f(x, y, z) ПМ-21-2 Шутов А.С.')

print('')
print('а)')
print(ttg.Truths(['x', 'y'], ['(not x nor y) nor (x nor not y)'], ascending = True).as_prettytable())
