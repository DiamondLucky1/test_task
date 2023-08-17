a = [1, 10, 2, 9]
m = sorted(a)[len(a) // 2]
print(sum(abs(i - m) for i in a))