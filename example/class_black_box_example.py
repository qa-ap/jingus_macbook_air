class BlackBox:
    # return 값이 어떠한 상태인지를 명시해 주기 위함이다?
    def __init__(self,name,price) -> None:
       self.name  = name
       self.price = price

class TravelBlackBox:
    def __init__(self,name,price) -> None:
       self.name  = name
       self.price = price

    def set_travel_mode(self,min):
        print(f'{self.name} {min} 분 동안 여행모드 ON')

# 기본 블랙박스와 여행모드 지원 블랙박스를 따로 만들고 싶으면?
# 두 클래스의 __init__() 메소드는 완전히 일치한다.
# 새로운 클래스를 만들 때마다 중복되는 클래스 내용을 모두 다 적는 건 비효율적이다.
# 클래스에는 상속이라는 기능이 있다. 물려받은 코드에 덧붙일 수 있다.

class TravelBlackBox(BlackBox): # BlackBox 상속!
    # def __init__(self,name,price) -> None:
    #    self.name  = name
    #    self.price = price
    def set_travel_mode(self,min):
        print(f'{self.name} {min} 분 동안 여행모드 ON')
    # 코드 사용법은 동일하다.

# __init__() 메서드를 새롭게 정의해주려면 상속은 어떻게!?
class TravelBlackBox(BlackBox): # BlackBox 상속!
    def __init__(self,name,price,sd):
        BlackBox.__init__(self,name,price) # 이부분이 중요하다! 기존 클래스를 재활용
        super().__init__(name,price) # 부모클래스 이름을 다시 적어주지 않아도 된다. self 도 생략가능
        self.sd = sd

    def set_travel_mode(self,min):
        print(f'{self.name} {min} 분 동안 여행모드 ON')

# 짜바리 클래스들
class VideoMaker:
    def make(self):
        print('추억용 여행 영상 제작')

class MailSender:
    def send(self):
        print('메일 발송')

# 블랙박스에 비디오 메이커 기능을 추가하고 싶은데? 이미 상속을 먼저 받아 부렀네 .. ㅠㅠ 
# 다중 상속을 받자!
class TravelBlackBox(BlackBox,VideoMaker,MailSender): # BlackBox 상속!
    def __init__(self,name,price,sd):
        BlackBox.__init__(self,name,price) # 이부분이 중요하다! 기존 클래스를 재활용
        super().__init__(name,price) # 부모클래스 이름을 다시 적어주지 않아도 된다. self 도 생략가능
        # super 는 첫번쨰 피상속인을 가리킨다.
        self.sd = sd

    def set_travel_mode(self,min):
        print(f'{self.name} {min} 분 동안 여행모드 ON')

# 상속의 재상속, 메소드 오버라이딩
class AdvancedTravelBlackBox(TravelBlackBox):
    #set_travel_mode() 재정의 가능
    def set_travel_mode(self, min):
        print(str(min) + '분 동안 여행 모드 ON')
        self.make()
        self.send()


b1 = TravelBlackBox('이진구',500,64)
b1.make() # > 결과 추억용 영상 제작
b1.send() # 함수니까 괄호가 있지
b1.nickname = '1호'
TravelBlackBox.set_travel_mode(b1,20) # 함수를 호출하는 것처럼 바로 실행
# 자동으로 영상 녹화하고 메일까지 보내주는 64기가 블랙박스
b2 = AdvancedTravelBlackBox('초록이',120000,64)
b2.set_travel_mode(15)