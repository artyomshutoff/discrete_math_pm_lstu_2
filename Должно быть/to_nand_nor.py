def list_subset(r1, r2):
	if not r1: return True
	if not r2: return False
	return r2[0] < r1[0] and r1[1] < r2[1]

def nesting_sort(funcs):
	res = []
	for i in funcs:
		res.append(0)
		without_i = funcs[:]
		without_i.remove(i)
		for j in without_i:
			if list_subset(i, j):
				res[-1] += 1
	return [i for _, i in sorted(zip(res, funcs), key = lambda x: x[0], reverse = True)]

def split_expr(expr):
	out = []
	_ = ''
	brackets = 0
	start = 0
	s_i = 0
	for i in range(len(expr)):
		if expr[i] == ')':
			brackets -= 1
		if start and brackets == 0:
			out.append(expr[s_i:i+1])
			start = 0
		if expr[i] == '(':
			if not brackets:
				s_i = i
			start = 1
			brackets += 1
		if expr[i] not in ' ()' and not brackets:
			_ += expr[i]
			if i == (len(expr) - 1):
				out.append(_)
				_ = ''
			continue
		if expr[i] == ' ' and _ != '' and not brackets:
			out.append(_)
			_ = ''
	for i in range(len(out)):
		if out[i][0] == '(' and out[i][-1] == ')':
			out[i] = out[i][1:len(out[i]) - 1]
	return out

def find_nested_funcs(expr):
	bracket1 = []
	funcs = []
	for i in range(len(expr)):
		if expr[i] == '(':
			bracket1.append(i)
		elif expr[i] == ')':
			funcs.append([bracket1[-1], i + 1])
			bracket1 = bracket1[:len(bracket1) - 1]
	return funcs

def converter(expr, type_):
	if type_ == 'nand':
		replacement = {
			'and': '(x nand y) nand (x nand y)',
			'or': '(x nand x) nand (y nand y)',
			'xor': '((x nand x) nand y) nand (x nand (y nand y))',
			'nor': '((x nand x) nand (y nand y)) nand ((x nand x) nand (y nand y))',
			'=>': 'x nand (not y)',
			'=': '(x nand y) nand ((x nand x) nand (y nand y))'
			}
	else:
		replacement = {
			'and': '(x nor x) nor (y nor y)',
			'or': '(x nor y) nor (x nor y)',
			'xor': '((x nor x) nor (y nor y)) nor (x nor y)',
			'nand': '((x nor x) nor (y nor y)) nor ((x nor x) nor (y nor y))',
			'=>': '((x nor x) nor y) nor ((x nor x) nor y)',
			'=': '(not x nor y) nor (x nor not y)'
			}
	funcs = nesting_sort(find_nested_funcs(expr))
	for i in range(len(funcs)):
		current_func = expr[funcs[i][0] + 1: funcs[i][1] - 1]
		current_func = split_expr(current_func)
		not_connect = []
		skip = 0
		for j in range(len(current_func)):
			if skip:
				skip = 0
				continue
			if current_func[j] == 'not':
				not_connect.append(f'not {current_func[j + 1]}')
				skip = 1
				continue
			not_connect.append(current_func[j])
		current_func = not_connect
		if current_func[1] == type_:
			continue
		sub_str = replacement[current_func[1]]
		change = {ord('x'): f'({current_func[0]})' if len(current_func[0]) > 1 else current_func[0], 
			ord('y'): f'({current_func[2]})' if len(current_func[2]) > 1 else current_func[2]}
		sub_str = sub_str.translate(change)
		expr = expr[:funcs[i][0]] + f'({sub_str})' + expr[funcs[i][1]:]
		end_i = funcs[i][1]
		diff = len(sub_str) - len(expr[funcs[i][0] + 1: funcs[i][1] - 1])
		for j in range(i, len(funcs)):
			if funcs[j][1] >= end_i:
				funcs[j][1] += diff
			if j != i:
				if funcs[j][0] >= end_i:
					funcs[j][0] += diff
	current_func = split_expr(expr)
	not_connect = []
	skip = 0
	for j in range(len(current_func)):
		if skip:
			skip = 0
			continue
		if current_func[j] == 'not':
			not_connect.append(f'not {current_func[j + 1]}')
			skip = 1
			continue
		not_connect.append(current_func[j])
	current_func = not_connect
	again = 0
	if type_ == 'nand':
		operations = ['and', 'or', 'xor', 'nor', '=>', '=']
	else:
		operations = ['and', 'or', 'xor', 'nand', '=>', '=']
	def check(current_func, operations):
		for i in current_func:
			for j in operations:
				if i == j:
					return 1
		return 0

	while check(current_func, operations):
		for o in operations:
			if again:
				again = 0
				break
			if [1 for i in current_func if i == o]:
				for i in range(len(current_func)):
					if current_func[i] == o:
						sub_str = replacement[current_func[i]]
						change = {ord('x'): f'({current_func[i-1]})' if len(current_func[i-1]) > 1 else current_func[i-1], 
							ord('y'): f'({current_func[i+1]})'} if len(current_func[i+1]) > 1 else current_func[i+1]
						sub_str = sub_str.translate(change)
						expr = sub_str
						current_func = expr
						again = 1
						break
	return expr

def to_nand(expr):
	return converter(expr, 'nand')

def to_nor(expr):
	return converter(expr, 'nor')