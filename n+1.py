# 1부터 n까지의 합을 계산하는 함수
def calc_sum1(n):
    # 'sum'은 파이썬 내장 함수 이름이므로 'total' 같은 다른 변수명을 쓰는 것이 좋습니다.
    total = 0
    
    # for i in range(1, n + 1)은 1부터 n까지의 숫자를 반복합니다.
    for i in range(1, n + 1):
        total = total + i  # 또는 total += i 와 같이 줄여 쓸 수 있습니다.
        
    return total

# 함수를 테스트해봅시다.
result = calc_sum1(10)
print(f"1부터 10까지의 합은 {result}입니다.") # 결과: 1부터 10까지의 합은 55입니다.