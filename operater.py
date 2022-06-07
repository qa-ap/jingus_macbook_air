# operator
# 할당 연산자
# 복합 할당 연산자
count = 1
count += 1
count = count + 1

# 산술 연산자
# ** 제곱
# // 몫
# % 나머지 , 홀짝 구할 때 쉽게 구한다.  

3 ** 2
7 // 3 # 몫만 구하고 싶을 때
7 % 3 # 나머지 1 

numbers     = range(8)
odd_numbers = [n for n in range(10) if n % 2 == 1]

for n in numbers:
    if n % 2 == 1: # 홀수!
        print(n)

for n in odd_numbers:
    print(n)

### 문자열도 연산자가 있다.
# + : *
# 문자열 연산자는 문자열끼리 할 수 있다. 문자열과 숫자열 더하기 안된다.

def cls():
    print('\n' * 20) # 엔터를 곱하기 여러번

cls()

# == 같냐?
# != 다르냐 ?
# > 크냐 < 작냐
# 결과는 True or False
# 논리 연산자
# and / or / not

True and False
print(False or not False)

height =180
age = 8
height > 140 and age > 10

### Membership
# 값이 있는 지 확인하는 연산자
김왼손과_집단지성들 = ['조희진','불탄고등어','요거트','류도영','스치','망고','Meta']
# 스치가 있냐?
print('스치' in 김왼손과_집단지성들)
print('이에스' not in 김왼손과_집단지성들)