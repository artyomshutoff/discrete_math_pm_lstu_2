# artyomshutoff
from Post_classification import post
import ttg_fix as ttg
import numpy as np
out = []
print('Вариант 29 f(x, y) ПМ-21-2 Шутов А.С.')

print('')
print('а)')
print(ttg.Truths(['x', 'y'], ['y = x', '(y = x) or y'], ascending = True).as_prettytable())
A = ttg.Truths(['x', 'y'], ['(y = x) or y'], ascending = True).as_pandas().to_numpy().tolist()
out.append(post(A))

print('')
print('б)')
print(ttg.Truths(['x', 'y'], ['not y => x', 'x or (not y => x)', '(x or (not y => x)) nor y'], ascending = True).as_prettytable())
A = ttg.Truths(['x', 'y'], ['(x or (not y => x)) nor y'], ascending = True).as_pandas().to_numpy().tolist()
out.append(post(A))

print('')
print('в)')
print(ttg.Truths(['x', 'y'], ['not y and x', 'y and not x', '(y and not x) nor not x', '(not y and x) xor ((y and not x) nor not x)'], ascending = True).as_prettytable())
A = ttg.Truths(['x', 'y'], ['(not y and x) xor ((y and not x) nor not x)'], ascending = True).as_pandas().to_numpy().tolist()
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