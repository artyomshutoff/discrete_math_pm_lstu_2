# artyomshutoff
from pdnf_pcnf import truth2pdnf, truth2pcnf

def truth2pdnf4check(truth_table, variables):
	out = []
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
		for j in range(len(truth_table[i]) - 1):
			if truth_table[i][j]:
				pdnf += variables[j]
			else:
				pdnf += f'not {variables[j]}'
			if j != (len(truth_table[i]) - 2):
				pdnf += ' and '
		out.append(pdnf)
		pdnf = ''
	
	if (check_for_brackets != 1):
		out.append(truth2pdnf(truth_table, variables))
	
	return out

def truth2pcnf4check(truth_table, variables):
	out = []
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
		for j in range(len(truth_table[i]) - 1):
			if truth_table[i][j]:
				pcnf += f'not {variables[j]}'
			else:
				pcnf += variables[j]
			if j != (len(truth_table[i]) - 2):
				pcnf += ' or '
		out.append(pcnf)
		pcnf = ''
	
	
	if (check_for_brackets != 1):
		out.append(truth2pcnf(truth_table, variables))
	
	return out