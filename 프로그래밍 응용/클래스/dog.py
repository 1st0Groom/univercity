# 클래스 (설계도) 만들기
class Dog:
    # 1. 초기화 메서드 (객체가 생성될 때 처음 실행됨)
    def __init__(self, name, age):
        self.name = name  # 속성: 이름
        self.age = age    # 속성: 나이

    # 2. 메서드 (행동)
    def bark(self):
        print(f"{self.name}가 멍멍 짖습니다!")
        
    def get_older(self):
        self.age += 1
        print(f"{self.name}가 한 살 더 먹어서 {self.age}살이 되었습니다.")

# 객체(실체) 만들기
dog1 = Dog("바둑이", 3)
dog2 = Dog("초코", 1)

# 객체의 행동 실행하기
dog1.bark()        # 출력: 바둑이가 멍멍 짖습니다!
dog2.get_older()   # 출력: 초코가 한 살 더 먹어서 2살이 되었습니다.
