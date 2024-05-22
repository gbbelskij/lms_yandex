kids = int(input())
name_max = ''
number_max = 0
for _ in range(kids):
    name = input()
    number = input()
    local_number_max = 0
    for j in number:
        local_number_max += int(j)
    if local_number_max >= number_max:
        number_max = local_number_max
        name_max = name
print(name_max)
