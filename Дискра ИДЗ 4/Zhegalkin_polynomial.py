# artyomshutoff
import numpy as np

def Zhegalkin_build(truth_table, variables):
	triangle = [[i for i in np.array(truth_table)[:, len(truth_table[0]) - 1]]]
	for j in range(len(truth_table) - 1):
		triangle.append([0 for i in range(len(truth_table))])
	stop = len(triangle[0])
	for i in range(1, len(triangle)):
		stop -= 1
		for j in range(stop):
			triangle[i][j] = 1 if triangle[i - 1][j] != triangle[i - 1][j + 1] else 0
	coef = list(np.array(triangle)[:, 0])
	del triangle
	out = ''
	for i in range(len(truth_table)):
		brackets = 0
		if not any(truth_table[i][:len(truth_table[i]) - 1]) and coef[i]:
			out += '1'
		elif any(truth_table[i][:len(truth_table[i]) - 1]) and coef[i]:
			ands = (truth_table[i][:len(truth_table[i]) - 1]).count(1) - 1
			if ands:
				brackets = 1
			flag = 1
			for j in range(len(truth_table[i][:len(truth_table[i]) - 1])):
				if truth_table[i][j]:
					if brackets and flag:
						out += '('
						flag = 0
					out += variables[j]
					if ands > 0:
						out += ' and '
					ands -= 1

		if brackets:
			out += ')'
		if coef[i + 1:len(coef)].count(1) and coef[i]:
			out += ' xor '
	return out if out else '0'
