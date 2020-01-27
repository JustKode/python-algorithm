def loop(n):
    if n == 1:  # 기저 사례, 1일 때 1을 반환
        return 1
    return loop(n - 1) + n  # 1부터 n - 1 까지 더한 것의 반환 값 + n

print(loop(100))