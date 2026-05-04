class Robot:
    
    # 클래스 변수, 로봇 인스턴스를 세는 변수
    population = 0

    def __init__(self, name):
        self._name = name
        Robot.population += 1

    def die(self):
        print(f"{self._name}가 소멸했습니다.")
        Robot.population -= 1
        if Robot.population == 0:
            print(f"{self._name}가 마지막 로봇 이였습니다.")
        else:
            print("이제 {:d}대의 로봇이 남아 있습니다.".format(Robot.population))
    
    def sayHi(self):
        print(f"안녕하세요. 주인님 저는 {self._name}입니다.")
    
    @classmethod
    def count(cls):
        print(f"로봇이 모두 {cls.population}대가 있습니다.")
    


# 객체(실체) 만들기
robot1 = Robot("알투디투(R2D2)")
robot2 = Robot("씨쓰리피오(C3PO)")

# 객체의 행동 실행하기
robot1.sayHi()           # 출력: 안녕하세요. 주인님 저는 알투디투(R2D2)입니다.
robot2.sayHi()           # 출력: 안녕하세요. 주인님 저는 씨쓰리피오(C3PO)입니다.

robot2.die()             # 출력: 씨쓰리피오(C3PO)가 소멸했습니다.
Robot.count()            # 출력: 로봇이 모두 1대가 있습니다.