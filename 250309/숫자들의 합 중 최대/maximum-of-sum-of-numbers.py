# 입력 받기
X, Y = map(int, input().split())

# 최대 자리수의 합을 구할 변수
max_sum = 0

# X부터 Y까지의 숫자에 대해 각 자리수의 합을 계산
for num in range(X, Y + 1):
    digit_sum = sum(int(digit) for digit in str(num))  # 각 자리수를 더한 합
    max_sum = max(max_sum, digit_sum)  # 최대값 갱신

# 결과 출력
print(max_sum)
