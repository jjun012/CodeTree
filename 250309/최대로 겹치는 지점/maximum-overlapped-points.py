# 입력 받기
N = int(input())  # 선분의 개수
events = []

# 선분의 정보 입력
for _ in range(N):
    x1, x2 = map(int, input().split())
    events.append((x1, 1))  # 선분의 시작은 +1
    events.append((x2 + 1, -1))  # 선분의 끝은 +1을 포함하기 위해 x2+1로 처리, 끝은 -1

# 이벤트 정렬: 첫번째 기준은 위치, 두번째 기준은 끝점(-1)이 먼저 오게
events.sort(key=lambda x: (x[0], x[1]))

max_overlap = 0  # 최대 겹치는 선분 수
current_overlap = 0  # 현재 겹치는 선분 수

# 각 이벤트를 처리
for event in events:
    current_overlap += event[1]  # +1 또는 -1을 더해줌
    max_overlap = max(max_overlap, current_overlap)  # 최대 겹치는 선분 수 갱신

print(max_overlap)
