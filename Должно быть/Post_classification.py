# artyomshutoff
from Zhegalkin_polynomial import Zhegalkin_build

def post(truth_table):
	T_0, T_1, L, M, S = 0, 0, 0, 0, 0
	
	print('+-----+-----+---+---+---+')
	print('| T_0 | T_1 | L | M | S |')
	print('+-----+-----+---+---+---+')
	
	if [0 for i in truth_table[0]] in truth_table:
		T_0 = 1
	
	if [1 for i in truth_table[0]] in truth_table:
		T_1 = 1
		
	if 'and' not in Zhegalkin_build(truth_table, [f'x{i}' for i in range(len(truth_table[0]) - 1)]):
		L = 1
	
	def check4mono(truth_table):
		for i in range(len(truth_table)):
			for j in range(len(truth_table[i:])):
				for n in range(len(truth_table[i]) - 1):
					if truth_table[i][n] <= truth_table[j][n]:
						if truth_table[i][-1] > truth_table[j][-1]:
							return 0
		return 1

	def check4selfduality(truth_table):
		for i in range(1, len(truth_table) // 2 + 1):
			if truth_table[len(truth_table) // 2 - i][-1] ==  truth_table[len(truth_table) // 2 + i - 1][-1]:
				return 0
		return 1
	
	M = check4mono(truth_table)
	
	S = check4selfduality(truth_table)
	
	print(f'|  {T_0}  |  {T_1}  | {L} | {M} | {S} |')
	print('+-----+-----+---+---+---+')