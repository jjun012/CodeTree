# 입력 받기
N = int(input())  # 격자의 크기 N
grid = [list(map(int, input().split())) for _ in range(N)]  # N개의 줄로 격자 정보 받기

# 3x3 격자 범위 내에서 동전의 개수를 최대화
max_coins = 0

# 3x3 격자에서 가능한 범위를 순차적으로 탐색
for i in range(N - 2):  # i는 3x3 격자의 시작 행, N-2까지
    for j in range(N - 2):  # j는 3x3 격자의 시작 열, N-2까지
        # 3x3 격자에서 동전 개수 세기
        coin_count = sum(sum(grid[i + x][j + y] for y in range(3)) for x in range(3))
        max_coins = max(max_coins, coin_count)  # 동전 개수 최대값 갱신

# 결과 출력
print(max_coins)
