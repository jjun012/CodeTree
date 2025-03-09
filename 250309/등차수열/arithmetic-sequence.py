# 입력 받기
N = int(input())  # N개의 수
arr = list(map(int, input().split()))  # N개의 수

# 수열을 집합(set)으로 변환하여 빠르게 검색할 수 있도록 함
arr_MAX_A = 100

# 변수 선언 및 입력
n = int(input())

arr = list(map(int, input().split()))

ans = 0

# 각 숫자에 대해 
# 등차수열의 개수를 확인합니다.
for x in range(1, MAX_A + 1):
	# 모든 쌍을 만들어 등차수열의 개수를 확인합니다.
    cnt = 0

    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == 2 * x:
                cnt += 1

    ans = max(ans, cnt)
    
print(ans)
set = set(arr)

# 쌍의 개수 세기
count = 0
for num in arr:
    if num + K in arr_set:  # num + K가 수열에 존재하면 그 쌍을 만족함
        count += 1

# 결과 출력
print(count)
