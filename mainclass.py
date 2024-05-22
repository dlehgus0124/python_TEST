class Rabbit :
    shape = ""
    xPos = 0
    yPos = 0

    def __init__(self, value) :
        self.shape = value
    
    def goto(self, x, y) :
        self.xPos = x
        self.yPos = y

    class HouseRabbit(Rabbit):
        owner = ""
        def eatFood(self) :
            print("집토끼가 오이를 먹습니다")

    class MoubtainRabbit(Rabbit):
        mountain = ""
        def eatWildGrass(self) :
            print("산토끼가 풀을 뜯어먹습니다")

rabbit1 = Rabbit("원")
rabbit1.goto(10, 20)
print("rabbit1의 모양 : ", rabbit1.shape)
print(f"rabbit1의 좌표 : ({rabbit1.xPos}, {rabbit1.yPos})")

HouseRabbit.owner = "이도현"
print(f"집토끼의 주인 : {HouseRabbit.owner}")
HouseRabbit.eatFood(rabbit1)

rabbit2 = Rabbit("삼각형")
rabbit2.goto(30, 40)
print("rabbit2의 모양 : ", rabbit2.shape)
print(f"rabbit2의 좌표 : ({rabbit2.xPos}, {rabbit2.yPos})")

MoubtainRabbit.mountain = "에베레스트 산"
print(f"산토끼의 산 : {MoubtainRabbit.mountain}")
MoubtainRabbit.eatWildGrass(rabbit2)

rabbit3 = Rabbit("토끼")
rabbit3.goto(50, 60)
print("rabbit3의 모양 : ", rabbit3.shape)
print(f"rabbit3의 좌표 : ({rabbit3.xPos}, {rabbit3.yPos})")