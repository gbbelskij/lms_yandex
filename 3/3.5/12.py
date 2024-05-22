with open(input(), 'r', encoding='utf-8') as f1:
    with open(input(), 'w', encoding='utf-8') as f2:
        with open(input(), 'w', encoding='utf-8') as f3:
            with open(input(), 'w', encoding='utf-8') as f4:
                for i in f1.readlines():
                    s = i.rstrip().split()
                    even = ''
                    odd = ''
                    equal = ''
                    if s != '':
                        for j in s:
                            len_even = len([int(x) for x in j if int(x) % 2 == 0])
                            len_odd = len([int(x) for x in j if int(x) % 2 != 0])
                            if len_even > len_odd:
                                even += j + ' '
                            elif len_even < len_odd:
                                odd += j + ' '
                            elif len_even == len_odd:
                                equal += j + ' '
                    f2.write(even.rstrip() + '\n')
                    f3.write(odd.rstrip() + '\n')
                    f4.write(equal.rstrip() + '\n')
