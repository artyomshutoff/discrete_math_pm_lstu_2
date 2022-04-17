# artyomshutoff
import ttg_fix as ttg

print('1)')
print(ttg.Truths(['x', 'y'], ['(x = y) xor x', 'x = (y xor x)'], ascending = True).as_prettytable())

print('')

print('2)')
print(ttg.Truths(['x', 'y'], ['(y = x) xor y', 'y = (x xor y)'], ascending = True).as_prettytable())

print('')

print('3)')
print(ttg.Truths(['x', 'y', 'z'], ['(x = y) xor z', 'x = (y xor z)'], ascending = True).as_prettytable())

print('')

print('4)')
print(ttg.Truths(['x', 'y'], ['(x nand y) nor x', 'x nand (y nor x)'], ascending = True).as_prettytable())

print('')

print('5)')
print(ttg.Truths(['x', 'y'], ['(y nand x) nor y', 'y nand (x nor y)'], ascending = True).as_prettytable())

print('')

print('6)')
print(ttg.Truths(['x', 'y', 'z'], ['(x nand y) nor z', 'x nand (y nor z)'], ascending = True).as_prettytable())

print('')

print('7)')
print(ttg.Truths(['x', 'y'], ['(x nand y) and x', 'x nand (y and x)'], ascending = True).as_prettytable())

print('')

print('8)')
print(ttg.Truths(['x', 'y'], ['(y nand x) and y', 'y nand (x and y)'], ascending = True).as_prettytable())

print('')

print('9)')
print(ttg.Truths(['x', 'y', 'z'], ['(x nand y) and z', 'x nand (y and z)'], ascending = True).as_prettytable())

print('')

print('10)')
print(ttg.Truths(['x', 'y'], ['(x nor y) and x', 'x nor (y and x)'], ascending = True).as_prettytable())

print('')

print('11)')
print(ttg.Truths(['x', 'y'], ['(y nor x) and y', 'y nor (x and y)'], ascending = True).as_prettytable())

print('')

print('12)')
print(ttg.Truths(['x', 'y', 'z'], ['(x nor y) and z', 'x nor (y and z)'], ascending = True).as_prettytable())