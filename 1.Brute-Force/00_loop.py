def loop(n):
    result = 0
    for i in range(1, n + 1):  # 1 ~ n까지 반복
        result += i
    return result

print(loop(100))