# 변수 선언 및 입력
n = int(input())

# 길이가 n인 직각삼각형을 뒤집어 출력합니다.
for i in range(n-1, -1, -1):
	for _ in range(i+1):
		print("*", end=" ")
	print()
	
# 길이가 n-1인 직각삼각형을 출력합니다.
for i in range(1, n):
	for _ in range(i+1):
		print("*", end=" ")
	print()
