# artyomshutoff
from Post_classification import post
import ttg_fix as ttg
import numpy as np
out = []
print('Вариант 29 f(x, y, z) ПМ-21-2 Шутов А.С.')

print('')
print('а)')
print(ttg.Truths(['x', 'y', 'z'], ['y and x', '(y and x) nand z'], ascending = True).as_prettytable())
A = ttg.Truths(['x', 'y', 'z'], ['(y and x) nand z'], ascending = True).as_pandas().to_numpy().tolist()
out.append(post(A))

print('')
print('б)')
print(ttg.Truths(['x', 'y', 'z'], ['not y or z', 'y xor (not y or z)', 'x nor (y xor (not y or z))'], ascending = True).as_prettytable())
A = ttg.Truths(['x', 'y', 'z'], ['x nor (y xor (not y or z))'], ascending = True).as_pandas().to_numpy().tolist()
out.append(post(A))

print('')
print('в)')
print(ttg.Truths(['x', 'y', 'z'], ['z nor y', 'y = x', '(z nor y) xor (y = x)', '(z nor y) xor (y = x) and not x'], ascending = True).as_prettytable())
A = ttg.Truths(['x', 'y', 'z'], ['(z nor y) xor (y = x) and not x'], ascending = True).as_pandas().to_numpy().tolist()
out.append(post(A))

print('')
print('Классификация Поста:')
print('+-----+-----+---+---+---+')
print('| T_0 | T_1 | L | M | S |')
print('+-----+-----+---+---+---+')
for i in out:
	print(f'|  {i[0]}  |  {i[1]}  | {i[2]} | {i[3]} | {i[4]} |')
print('+-----+-----+---+---+---+')

def output(out):
	out = np.array(out)
	for i in range(len(out[0])):
		if not 0 in out[:, i]:
			print('Система не является полной.')
			return
	print('Система является полной.')

output(out)