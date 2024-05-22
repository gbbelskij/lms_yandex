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

phrase = input()
variables = sorted(set([item for item in phrase if item.isupper()]))
temp = []
res = []
phrase = phrase.replace('(', '( ')
phrase = phrase.replace(')', ' )')
for item in phrase.split():
    if item in variables:
        res.append(item)
    elif item == '(':
        temp.append(item)
    elif item == ')':
        while temp[-1] != '(':
            res.append(operations[temp.pop()])
        temp.pop()
    elif item in operations:
        while temp and priority[item] >= priority[temp[-1]]:
            res.append(operations[temp.pop()])
        temp.append(item)
while temp:
    res.append(operations[temp.pop()])
table = product([0, 1], repeat=len(variables))
print(*variables, 'F')
for values in table:
    global_vars = {key: value for key, value in zip(variables, values)}
    temp = []
    for item in res:
        if item in global_vars:
            temp.append(global_vars[item])
        else:
            if item == 'not':
                temp.append(not temp.pop())
            else:
                variable2, variable1 = temp.pop(), temp.pop()
                temp.append(eval(f'{variable1} {item} {variable2}'))
    print(*values, int(temp.pop()))
