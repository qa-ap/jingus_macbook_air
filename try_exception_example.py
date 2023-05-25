num1 = 'a'
num2 = 0
try:
    result = num1 / num2 # num1 = 3, num2 = 0 이라 가정
    print(f'연산 결과는 {result} 입니다')
# except Exception as err:

except ZeroDivisionError:
    # 에러의 원인을 알아내자.
    print('0으로 나눌 수 없어요.')

except TypeError:
    print('값의 형태가 이상해요')

except ValueError:
    print('ValueError : 값의 형태가 이상해요')

except Exception as err:
    print('에러가 발생했어요')

else:
    # try 가 동작했을 때 동작
    print('정상 동작했어요.')
finally:
    # 무조건 동작
    print('수행 종료.')