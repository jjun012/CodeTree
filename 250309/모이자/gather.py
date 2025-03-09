# 입력 받기
N = int(input())
people = list(map(int, input().split()))

# 최소 이동 거리 합을 찾기 위한 변수
min_distance = float('inf')

# 각 집을 기준으로 계산
for i in range(N):
    total_distance = 0
    # 해당 집을 기준으로 다른 모든 집과의 이동 거리 합 계산
    for j in range(N):
        total_distance += abs(i - j) * people[j]
    
    # 이동 거리 합이 최소가 되는 값을 찾음
    min_distance = min(min_distance, total_distance)

# 결과 출력
print(min_distance)
