# 빈 리스트(가방)를 만듭니다.
myBag = []

# .append()를 사용해서 가방에 물건을 넣습니다.
myBag.append('휴대폰')
myBag.append('지갑')
myBag.append('손수건')
myBag.append('빗')
myBag.append('자료구조')
myBag.append('야구공')
print('가방속의 물건:', myBag)

# 이미 들어있는 '빗'을 또 추가합니다.
myBag.append('빗')
# .remove()를 사용해서 '손수건'을 꺼냅니다.
myBag.remove('손수건')
print('가방속의 물건:', myBag)