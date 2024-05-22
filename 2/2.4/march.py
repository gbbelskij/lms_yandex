opponents = int(input())
qualification = 3
for i in range(1, opponents + 1):
    for j in range(qualification, 0, -1):
        print(f"До старта {j} секунд(ы)")
    print(f"Старт {i}!!!")
    qualification += 1
