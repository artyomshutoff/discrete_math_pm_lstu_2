from pyeda.inter import *
import numpy as np

def expr2py(expr, sep = 'or'):
	expr = expr.replace('+', 'or')
	expr = expr.replace('·', 'and')
	nots = expr.count('′')
	for i in range(nots):
		for j in range(-1, -len(expr) - 1, -1):
			if expr[j] == '′':
				replace_expr = '′'
				for n in range(j - 1, -len(expr) - 1, -1):
					if expr[n] == ' ' or expr[n] == '(':
						break
					replace_expr += expr[n]
				r = 'not '
				re = replace_expr[::-1]
				expr = expr.replace(re, r + re[:len(re) - 1])
				break
	if sep == 'and':
		return expr
	res = ''
	for i in expr.split(' or '):
		if len(i.split(' and ')) != 1:
			res += f'({i}) or '
		else:
			res += f'{i} or '
	res = res.rstrip(' or ')
	
	if not res.count('or'):
		res = res.rstrip(')')
		res = res.lstrip('(')
	
	return res

def mdnf(truth_table, variables):
	x = farray(list(map(exprvar, variables[::-1])))
	a = np.array(truth_table)
	vector = [i[len(variables)] for i in a]
	f = truthtable(x, vector)
	f_expr = truthtable2expr(f)
	f_expr, = espresso_exprs(f_expr.to_dnf())
	return expr2py(f_expr.to_dnf().to_unicode(), sep = 'or')

def mcnf(truth_table, variables):
	x = farray(list(map(exprvar, variables[::-1])))
	a = np.array(truth_table)
	vector = [i[len(variables)] for i in a]
	f = truthtable(x, vector)
	f_expr = truthtable2expr(f)
	return expr2py(f_expr.to_cnf().to_unicode(), sep = 'and')