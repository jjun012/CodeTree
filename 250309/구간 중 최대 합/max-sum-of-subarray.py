# 입력 받기
N, K = map(int, input().split())  # N은 수의 개수, K는 연속된 수의 개수
numbers = list(map(int, input().split()))  # N개의 수가 주어짐

# 처음 K개의 합을 계산
current_sum = sum(numbers[:K])
max_sum = current_sum

# 슬라이딩 윈도우 방식으로 연속된 K개의 합을 구하고 최대값 찾기
for i in range(K, N):
    current_sum += numbers[i] - numbers[i - K]  # 윈도우를 한 칸 이동
    max_sum = max(max_sum, current_sum)  # 최대값 갱신

# 결과 출력
print(max_sum)
