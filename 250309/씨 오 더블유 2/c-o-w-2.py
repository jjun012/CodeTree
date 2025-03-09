# 입력 받기
N = int(input())  # 문자열 길이
s = input().strip()  # 문자열

# 각 문자의 위치를 저장할 리스트
c_indices = []
o_indices = []
w_indices = []

# 문자열에서 C, O, W의 인덱스 저장
for i, char in enumerate(s):
    if char == 'C':
        c_indices.append(i + 1)  # 1-based index
    elif char == 'O':
        o_indices.append(i + 1)
    elif char == 'W':
        w_indices.append(i + 1)

# 가능한 (C, O, W) 조합을 찾기
result = []
for c in c_indices:
    for o in o_indices:
        if o > c:  # O가 C보다 뒤에 나와야 함
            for w in w_indices:
                if w > o:  # W가 O보다 뒤에 나와야 함
                    result.append((c, o, w))

# 결과 출력
print(len(result))

