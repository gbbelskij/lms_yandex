with open("numbers.num", "rb") as f:
    numbers = f.read()
print(sum([int.from_bytes(numbers[i:i + 2], "big") for i in range(0, len(numbers), 2)]) % 2**16)
