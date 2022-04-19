# artyomshutoff
import ttg_fix as ttg

print(ttg.Truths(['f_0'], ['not 0'], ascending = True).as_prettytable())

print('\n')

print(ttg.Truths(['x', 'y'], ['not (not x and not y)'], ascending = True).as_prettytable())

print('\n')

print(ttg.Truths(['x', 'y'], ['not (not (not x => not y))'], ascending = True).as_prettytable())

print('\n')

print(ttg.Truths(['x'], ['not (not x)'], ascending = True).as_prettytable())

print('\n')

print(ttg.Truths(['x', 'y'], ['not (not (not y => not x))'], ascending = True).as_prettytable())

print('\n')

print(ttg.Truths(['y'], ['not (not y)'], ascending = True).as_prettytable())

print('\n')

print(ttg.Truths(['x', 'y'], ['not ((not x) xor (not y))'], ascending = True).as_prettytable())

print('\n')

print(ttg.Truths(['x', 'y'], ['not ((not x) or (not y))'], ascending = True).as_prettytable())

print('\n')

print(ttg.Truths(['x', 'y'], ['not ((not x) nor (not y))'], ascending = True).as_prettytable())

print('\n')

print(ttg.Truths(['x', 'y'], ['not ((not x) = (not y))'], ascending = True).as_prettytable())

print('\n')

print(ttg.Truths(['y'], ['not (not (not y))'], ascending = True).as_prettytable())

print('\n')

print(ttg.Truths(['x', 'y'], ['not ((not y) => (not x))'], ascending = True).as_prettytable())

print('\n')

print(ttg.Truths(['x'], ['not (not (not x))'], ascending = True).as_prettytable())

print('\n')

print(ttg.Truths(['x', 'y'], ['not ((not x) => (not y))'], ascending = True).as_prettytable())

print('\n')

print(ttg.Truths(['x', 'y'], ['not ((not x) nand (not y))'], ascending = True).as_prettytable())

print('\n')

print(ttg.Truths(['f_15'], ['not 1'], ascending = True).as_prettytable())