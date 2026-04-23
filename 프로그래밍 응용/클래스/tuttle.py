import turtle as t

class 트레져헌터(t.Turtle): 
    def __init__(self):
        # 부모 클래스(Turtle)의 초기화 실행
        t.Turtle.__init__(self) 
        
        # 트레져헌터만의 초기 설정
        self.penup()       # 펜 들기
        self.hideturtle()  # 거북이 숨기기
        self.goto(0, 0)    # 정중앙(0,0)으로 이동
        self.write("TreasureHunter", align="center") # 글자 쓰기

    def location(self):
        h = self.heading()
        x = self.xcor()
        y = self.ycor()
        dis = self.distance(self)
        
        print("헌터의 방향: ")
        print("X coor:",x ,", Ycoor:",y,", Direction",h)
        print("Distance", dis)

a= 트레져헌터()
a.location()

turtle.mainloop()
