from itertools import product

phrase = input()
variables = [symbol for symbol in sorted(set(phrase.split())) if symbol.isupper()]
length = len(variables)
print(*variables, "F")
for values in product([False, True], repeat=length):
    result_vars = {key: value for key, value in zip(variables, values)}
    expression_result = int(eval(phrase, result_vars))
    print(*[int(i) for i in values], expression_result)
