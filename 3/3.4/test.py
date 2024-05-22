from itertools import product

operations = {
    'not': 'not',
    'and': 'and',
    'or': 'or',
    '^': '!=',
    '->': '<=',
    '~': '==',
}

priority = {
    'not': 0,
    'and': 1,
    'or': 2,
    '^': 3,
    '->': 4,
    '~': 5,
    '(': 6,
}


def parse_phrase(phrase, vars):
    temp = []
    result = []
    phrase = phrase.replace('(', '( ').replace(')', ' )')
    for symbol in phrase.split():
        if symbol in vars:
            result.append(symbol)
        elif symbol == '(':
            temp.append(symbol)
        elif symbol == ')':
            while temp[-1] != '(':
                result.append(operations[temp.pop()])
            temp.pop()
        elif symbol in operations:
            while temp and priority[symbol] >= priority[temp[-1]]:
                result.append(operations[temp.pop()])
            temp.append(symbol)
    while temp:
        result.append(operations[temp.pop()])
    # print(result)
    return result


def evaluate(phrase, vars):
    temp = []
    for symbol in phrase:
        if symbol in vars:
            temp.append(vars[symbol])
        else:
            if symbol == 'not':
                temp.append(not temp.pop())
            else:
                operator = symbol
                variable2, variable1 = temp.pop(), temp.pop()
                if operator == '!=':
                    result = variable1 != variable2
                elif operator == '<=':
                    result = variable1 <= variable2
                elif operator == '==':
                    result = variable1 == variable2
                else:
                    result = variable1 and variable2
                temp.append(result)
    return int(temp.pop())

phrase = input()
vars = sorted(set([symbol for symbol in phrase if symbol.isupper()]))
parsed_phrase = parse_phrase(phrase, vars)
table = product([0, 1], repeat=len(vars))
print(*vars, 'F')
for values in table:
    globals = {key: value for key, value in zip(vars, values)}
    print(*values, evaluate(parsed_phrase, globals))
