# artyomshutoff
import ttg_fix as ttg
from pdnf_pcnf import truth2pdnf, truth2pcnf
from itertools import combinations as combo

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

def direct_minimization(expr, variables):

	A = ttg.Truths([i for i in variables], [expr], ascending = True).as_pandas().to_numpy()
	pdnf = truth2pdnf(A, variables)
	pcnf = truth2pcnf(A, variables)

	print('')

	for type_ in ['pdnf', 'pcnf']:

		print(f'Непосредственная минимизация {"СДНФ" if type_ == "pdnf" else "СКНФ"}:\n')

		expr = pdnf if type_ == "pdnf" else pcnf
		print(f'Исходная функция: {expr}\n')
		
		
		def minimizer(expr):
			sweep = 0
			c = 0

			while True:
				sweep += 1
				expr = expr.split(f' {"or" if type_ == "pdnf" else "and"} ')
				expr = list(map(lambda x: x[1:len(x)-1] if x[0] == '(' and x[-1] == ')' else x, expr))
				used = []
				minimized = []
				for i in combo([j for j in range(len(expr))], r = 2):
					i = list(i)
					if i[0] in used or i[1] in used:
						continue
					func1 = expr[i[0]].split(f' {"and" if type_ == "pdnf" else "or"} ')
					func2 = expr[i[1]].split(f' {"and" if type_ == "pdnf" else "or"} ')
					if len(func1) == 1 or len(func2) == 1 or len(func1) != len(func2):
						continue
					diff_vars = []
					plus_vars = func1 + func2
					for j in plus_vars:
						if j in func1 and j in func2:
							continue
						diff_vars.append(j)
					for j in diff_vars:
						plus_vars.remove(j)
					plus_vars = list(set(plus_vars))
					if len(diff_vars) > 2:
						continue
					func1_out = f' {"and" if type_ == "pdnf" else "or"} '.join(func1)
					func1_out = f'({func1_out})'
					func2_out = f' {"and" if type_ == "pdnf" else "or"} '.join(func2)
					func2_out = f'({func2_out})'
					c += 1
					print(f'{c}) Склеиваем {func1_out} и {func2_out}. Убираем {diff_vars[0]} и {diff_vars[1]}.')
					minimized.append(f' {"and" if type_ == "pdnf" else "or"} '.join(plus_vars))
					used.append(i[0])
					used.append(i[1])
	
				for_remove = [expr[i] for i in used]
				for i in for_remove:
					expr.remove(i)
	
				expr = parentheses_and_out("or" if type_ == "pdnf" else "and", minimized + expr)
				if minimized and sweep >= 1:
					print(f'Полученная функция: {expr}')
				
				if not minimized:
					return expr
			
		new_expr = minimizer(expr)
		if new_expr != expr:
			print(f'\nМинимизированная {"СДНФ" if type_ == "pdnf" else "СКНФ"}: {new_expr}\n')
		else:
			print('Функция уже тупиковая. Минимизация не требуется.\n')
