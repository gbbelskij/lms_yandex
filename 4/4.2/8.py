
string = 'Яндекс использует Python во многих проектах'
print(sorted(string.split(), key=lambda s: (len(s), s.lower())))
