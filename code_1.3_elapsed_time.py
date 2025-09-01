import time

myBag = []
start = time.time()

# 'insert' 함수 대신 'append' 메서드를 사용합니다.
myBag.append('축구공')

end = time.time()

print("myBag 내용:", myBag)
print(f"실행시간 = {end - start:.10f}초")