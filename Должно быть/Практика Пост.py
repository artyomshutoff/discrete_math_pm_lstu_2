# artyomshutoff
import ttg_fix as ttg
from Post_classification import post

print(ttg.Truths(['f_0'], ['0'], ascending = True).as_prettytable())
A = ttg.Truths(['f_0'], ['0'], ascending = True).as_pandas().to_numpy().tolist()
post(A)
print('\n')

print(ttg.Truths(['x', 'y'], ['x and y'], ascending = True).as_prettytable())
A = ttg.Truths(['x', 'y'], ['x and y'], ascending = True).as_pandas().to_numpy().tolist()
post(A)

print('\n')

print(ttg.Truths(['x', 'y'], ['not (x => y)'], ascending = True).as_prettytable())
A = ttg.Truths(['x', 'y'], ['not (x => y)'], ascending = True).as_pandas().to_numpy().tolist()
post(A)
print('\n')

print(ttg.Truths(['x'], ['(x)'], ascending = True).as_prettytable())
A = ttg.Truths(['x'], ['(x)'], ascending = True).as_pandas().to_numpy().tolist()
post(A)
print('\n')

print(ttg.Truths(['x', 'y'], ['not (y => x)'], ascending = True).as_prettytable())
A = ttg.Truths(['x', 'y'], ['not (y => x)'], ascending = True).as_pandas().to_numpy().tolist()
post(A)
print('\n')

print(ttg.Truths(['y'], ['(y)'], ascending = True).as_prettytable())
A = ttg.Truths(['y'], ['(y)'], ascending = True).as_pandas().to_numpy().tolist()
post(A)
print('\n')

print(ttg.Truths(['x', 'y'], ['x xor y'], ascending = True).as_prettytable())
A = ttg.Truths(['x', 'y'], ['x xor y'], ascending = True).as_pandas().to_numpy().tolist()
post(A)
print('\n')

print(ttg.Truths(['x', 'y'], ['x or y'], ascending = True).as_prettytable())
A = ttg.Truths(['x', 'y'], ['x or y'], ascending = True).as_pandas().to_numpy().tolist()
post(A)
print('\n')

print(ttg.Truths(['x', 'y'], ['x nor y'], ascending = True).as_prettytable())
A = ttg.Truths(['x', 'y'], ['x nor y'], ascending = True).as_pandas().to_numpy().tolist()
post(A)
print('\n')

print(ttg.Truths(['x', 'y'], ['x = y'], ascending = True).as_prettytable())
A = ttg.Truths(['x', 'y'], ['x = y'], ascending = True).as_pandas().to_numpy().tolist()
post(A)
print('\n')

print(ttg.Truths(['y'], ['not y'], ascending = True).as_prettytable())
A = ttg.Truths(['y'], ['not y'], ascending = True).as_pandas().to_numpy().tolist()
post(A)
print('\n')

print(ttg.Truths(['x', 'y'], ['y => x'], ascending = True).as_prettytable())
A = ttg.Truths(['x', 'y'], ['y => x'], ascending = True).as_pandas().to_numpy().tolist()
post(A)
print('\n')

print(ttg.Truths(['x'], ['not x'], ascending = True).as_prettytable())
A = ttg.Truths(['x'], ['not x'], ascending = True).as_pandas().to_numpy().tolist()
post(A)
print('\n')

print(ttg.Truths(['x', 'y'], ['x => y'], ascending = True).as_prettytable())
A = ttg.Truths(['x', 'y'], ['x => y'], ascending = True).as_pandas().to_numpy().tolist()
post(A)
print('\n')

print(ttg.Truths(['x', 'y'], ['x nand y'], ascending = True).as_prettytable())
A = ttg.Truths(['x', 'y'], ['x nand y'], ascending = True).as_pandas().to_numpy().tolist()
post(A)
print('\n')

print(ttg.Truths(['f_15'], ['1'], ascending = True).as_prettytable())
A = ttg.Truths(['f_15'], ['1'], ascending = True).as_pandas().to_numpy().tolist()
post(A)