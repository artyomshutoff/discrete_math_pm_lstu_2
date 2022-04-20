from itertools import combinations as combo
import ttg_fix as ttg
from math import log
from prettytable import PrettyTable

def nice_carnot_out(left, right, vars_left, vars_right, map_):
	t = PrettyTable()
	t.field_names = [f'{left}/{right}'] + vars_right
	for i in range(len(vars_left)):
		t.add_row([vars_left[i]] + map_[i])
	print(t)

def carnot(expr, variables):

	left = variables[:len(variables) // 2]
	right = variables[len(variables) // 2:]

	A = ttg.Truths([i for i in variables], [expr], ascending = True).as_pandas().to_numpy().tolist()

	map_y = 2 ** len(left)
	map_x = 2 ** len(right)

	map_ = []

	for i in range(map_y):
		map_.append([0 for j in range(map_x)])

	vars_left = []

	for i in range(map_y):
		to_app = ''
		for j in range(len(left), 0, -1):
			again = 2 ** j
			ap = [('0' if x < again // 2 else '1') for x in range(again)]
			if (i // again) % 2:
				ap = ap[::-1]
			to_app += ap[i % again]
		vars_left.append(to_app)

	vars_right = []

	for i in range(map_x):
		to_app = ''
		for j in range(len(right), 0, -1):
			again = 2 ** j
			ap = [('0' if x < again // 2 else '1') for x in range(again)]
			if (i // again) % 2:
				ap = ap[::-1]
			to_app += ap[i % again]
		vars_right.append(to_app)

	for i in range(len(A)):
		row = vars_left.index(''.join(map(str, A[i][:len(left)])))
		col = vars_right.index(''.join(map(str, A[i][len(left): len(A[i]) - 1])))
		map_[row][col] = A[i][-1]

	def isRect(points, map_):
		map_0 = []
		for i in range(len(map_)):
			map_0.append([0 for j in range(len(map_[i]))])
		for i in points:
			map_0[int(i[0])][int(i[1])] = 1
		xs = [int(i[1]) for i in points]
		ys = [int(i[0]) for i in points]
		xMin, xMax = min(xs), max(xs)
		yMin, yMax = min(ys), max(ys)
		for i in range(yMin, yMax + 1):
			for j in range(xMin, xMax + 1):
				if not map_0[i][j]:
					return False
		return 1

	print(f'Карта Карно для функции: {expr}')
	nice_carnot_out(left, right, vars_left, vars_right, map_)

	def minimization(type_, map_, left, right, vars_left, vars_right):

		def area_accessibility(using_cells, points, type_):
			a = []
			for i in points:
				a.append(not using_cells[int(i[0])][int(i[1])])
			return any(a) if type_ == 'dnf' else any([not i for i in a])

		def parentheses_and_out(connector, minimized):
			if len(minimized) == 1:
				return minimized[0]
			minimized_new = []
			for i in minimized:
				if len(i.split()) > 2:
					minimized_new.append(f'({i})')
				elif len(i.split()) == 2:
					if i.split()[0] == 'not' and len(i.split()[1]) == 1:
						minimized_new.append(i)
					else:
						minimized_new.append(f'({i})')
				else:
					minimized_new.append(i)
			return f' {connector} '.join(minimized_new)

		minimized = []

		A = []
		for i in range(len(map_)):
			for j in range(len(map_[i])):
				if type_ == 'dnf':
					if map_[i][j]:
						A.append(str(i) + str(j))
				elif not map_[i][j]:
					A.append(str(i) + str(j))
		area = len(map_) * len(map_[0])
		p = int(log(area, 2))

		using_cells = []
		for i in range(len(map_)):
			using_cells.append([0 if type_ == 'dnf' else 1 for j in range(len(map_[i]))])

		while p > -1:
			area = 2**p
			for i in combo(A, r = area):
				i = list(i)
				if not isRect(i, map_):
					continue
				if area_accessibility(using_cells, i, type_):
					for j in i:
						using_cells[int(j[0])][int(j[1])] = 1 if type_ == 'dnf' else 0
					xs = [int(j[1]) for j in i]
					ys = [int(j[0]) for j in i]
					xMin, xMax = min(xs), max(xs)
					yMin, yMax = min(ys), max(ys)
					current_funcs = []
					for j in range(len(right)):
						same_check = set([])
						for n in range(xMin, xMax + 1):
							same_check.add(vars_right[n][j])
						if len(same_check) == 1:
							for_inverse = int(list(same_check)[0])
							if type_ == 'dnf':
								for_inverse = not for_inverse
							if for_inverse:
								current_funcs.append(f'not {right[j]}')
							else:
								current_funcs.append(f'{right[j]}')

					for j in range(len(left)):
						same_check = set([])
						for n in range(yMin, yMax + 1):
							same_check.add(vars_left[n][j])
						if len(same_check) == 1:
							for_inverse = int(list(same_check)[0])
							if type_ == 'dnf':
								for_inverse = not for_inverse
							if for_inverse:
								current_funcs.append(f'not {left[j]}')
							else:
								current_funcs.append(f'{left[j]}')

					if current_funcs:
						if len(current_funcs) == 1:
							minimized.append(current_funcs[0])
						else:
							connector = 'and' if type_ == 'dnf' else 'or'
							minimized.append(f' {connector} '.join(current_funcs))

					print('\nВыберем ячейки:', ', '.join(i))
					nice_carnot_out(left, right, vars_left, vars_right, using_cells)
					print('Полученное выражение:', minimized[-1])
			p -= 1
		connector = 'or' if type_ == 'dnf' else 'and'
		return parentheses_and_out(connector, minimized)

	print('\nМинимизация ДНФ:')
	mdnf = minimization('dnf', map_, left, right, vars_left, vars_right)
	print('\nМинимизированная ДНФ:')
	print(mdnf)

	print('\nМинимизация КНФ:')
	mdnf = minimization('cnf', map_, left, right, vars_left, vars_right)
	print('\nМинимизированная КНФ:')
	print(mdnf)
