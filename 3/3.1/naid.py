n = int(input())
articles = [''] * n
for i in range(n):
    articles[i] = input()
research = input()
for i in articles:
    if research.lower() in i.lower():
        print(i)
