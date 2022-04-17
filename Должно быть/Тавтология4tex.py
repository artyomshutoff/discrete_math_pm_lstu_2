#artyomshutoff
import ttg_fix as ttg

print(ttg.Truths(['A'], ['A or not A'], ascending = True).as_prettytable())

print('\n')

print(ttg.Truths(['A', 'B'], ['A => (B => A)'], ascending = True).as_prettytable())

print('\n')

print(ttg.Truths(['A', 'B'], ['(A and B) => A'], ascending = True).as_prettytable())

print('\n')

print(ttg.Truths(['A', 'B'], ['(A and B) => B'], ascending = True).as_prettytable())

print('\n')

print(ttg.Truths(['A', 'B'], ['((not B) => (not A)) => (((not B) => A) => B)'], ascending = True).as_prettytable())

print('\n')

print(ttg.Truths(['A', 'B', 'C'], ['(A => B) => ((B => C) => (A => C))'], ascending = True).as_prettytable())

print('\n')

print(ttg.Truths(['A'], ['A => A'], ascending = True).as_prettytable())

print('\n')

print(ttg.Truths(['A', 'B'], ['A => (B => (A and B))'], ascending = True).as_prettytable())

print('\n')

print(ttg.Truths(['A', 'B'], ['A => (A or B)'], ascending = True).as_prettytable())

print('\n')

print(ttg.Truths(['A', 'B'], ['B => (A or B)'], ascending = True).as_prettytable())

print('\n')

print(ttg.Truths(['A', 'B'], ['((A => B) => A) => A'], ascending = True).as_prettytable())

print('\n')

print(ttg.Truths(['A', 'B', 'C'], ['(A => (B => C)) => ((A => B) => (A => C))'], ascending = True).as_prettytable())