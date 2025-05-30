# 변수 선언 및 입력
n = int(input())

# 1부터 n까지의 수 중, 온전수를 찾아 출력합니다.
for i in range(1, n + 1):
	if i % 2 == 0:
		continue
	if i % 10 == 5:
		continue
	if i % 3 == 0 and i % 9 != 0:
		continue
	print(i, end=" ")
