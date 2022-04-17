# artyomshutoff
def truth2pdnf(truth_table, variables):
	pdnf = ''
	check_for_brackets = 0
	unit = 0
	for i in truth_table:
		if i[-1] != 1:
			continue
		check_for_brackets += 1
		unit += 1
	for i in range(len(truth_table)):
		if truth_table[i][-1] != 1:
			continue
		unit -= 1
		if check_for_brackets != 1:
			pdnf += '('
		for j in range(len(truth_table[i]) - 1):
			if truth_table[i][j]:
				pdnf += variables[j]
			else:
				pdnf += f'not {variables[j]}'
			if j != (len(truth_table[i]) - 2):
				pdnf += ' and '
		if (check_for_brackets != 1):
			if unit > 0:
				pdnf += ') or '
			else:
				pdnf += ')'
	
	return pdnf if pdnf else 0

def truth2pcnf(truth_table, variables):
	pcnf = ''
	check_for_brackets = 0
	unit = 0
	for i in truth_table:
		if i[-1] != 0:
			continue
		check_for_brackets += 1
		unit += 1
	for i in range(len(truth_table)):
		if truth_table[i][-1] != 0:
			continue
		unit -= 1
		if check_for_brackets != 1:
			pcnf += '('
		for j in range(len(truth_table[i]) - 1):
			if truth_table[i][j]:
				pcnf += f'not {variables[j]}'
			else:
				pcnf += variables[j]
			if j != (len(truth_table[i]) - 2):
				pcnf += ' or '
		if (check_for_brackets != 1):
			if unit > 0:
				pcnf += ') and '
			else:
				pcnf += ')'
	
	return pcnf if pcnf else 0