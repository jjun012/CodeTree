# 변수 선언 및 입력
n, b = tuple(map(int, input().split()))
p = [
    int(input())
    for _ in range(n)
]

ans = 0

# 한 명의 학생에 선물 쿠폰을 쓸 때 선물 가능한 학생의 최대 명수를 구합니다.
for i in range(n):
	# i번째 학생의 선물에 쿠폰을 쓸 때 선물 가능한 학생 수를 구합니다.
	
	# tmp배열을 만들어 i번째 학생의 선물에 쿠폰을 쓸 때
	# 각 학생의 원하는 선물 가격을 저장합니다.
	tmp = [
		p[j]
		for j in range(n)
	]
	tmp[i] /= 2
	
	# 학생을 선물 가격 순으로 정렬합니다.
	# 선물 가격이 가장 작은 학생부터 선물을 사 줄 때,
	# 반드시 가장 많은 학생에게 선물을 줄 수 있습니다.
	tmp.sort()
	
	student = 0
	cnt = 0
	
	# 가장 많은 학생에게 선물을 줄 때, 그 학생 수를 구합니다.
	# student : 선물받은 학생 수 / cnt : 현재까지 쓴 돈
	for j in range(n):
		if cnt + tmp[j] > b:
			break
		cnt += tmp[j]
		student += 1
	
	ans = max(ans, student)

print(ans)
