# 1. 함수 정의
def contains(bag, e) :
    return e in bag

def insert(bag, e) :
    bag.append(e)

def remove(bag, e) :
    bag.remove(e)

def count(bag):
    return len(bag)

# 2. 함수 사용 (실제로 실행되는 부분)
# 데이터를 저장할 빈 리스트(가방) 만들기
my_bag = []
print(f"최초의 가방 상태: {my_bag}")

# insert 함수로 가방에 물건 넣기
insert(my_bag, "사과")
insert(my_bag, "노트북")
insert(my_bag, "지갑")
print(f"물건을 넣은 후 가방 상태: {my_bag}")

# count 함수로 개수 세기
item_count = count(my_bag)
print(f"가방 속 물건 개수: {item_count}개")

# contains 함수로 물건이 있는지 확인하기
has_apple = contains(my_bag, "사과")
print(f"가방에 '사과'가 있나요? {has_apple}")

# remove 함수로 물건 빼기
remove(my_bag, "사과")
print(f"'사과'를 뺀 후 가방 상태: {my_bag}")

# 다시 한번 물건이 있는지 확인하기
has_apple_again = contains(my_bag, "사과")
print(f"가방에 '사과'가 다시 있나요? {has_apple_again}")