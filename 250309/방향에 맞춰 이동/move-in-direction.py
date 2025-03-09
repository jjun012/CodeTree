# N번 이동
N = int(input())

# 초기 좌표 (0, 0)
x, y = 0, 0

# 방향에 따른 dx, dy 값 설정
directions = {'W': (-1, 0), 'S': (0, -1), 'N': (0, 1), 'E': (1, 0)}

# 이동 방향과 거리 입력 받기
for _ in range(N):
    direction, distance = input().split()
    distance = int(distance)
    
    # 방향에 따른 이동
    dx, dy = directions[direction]
    
    # 현재 좌표에 이동 적용
    x += dx * distance
    y += dy * distance

# 최종 좌표 출력
print(x, y)
