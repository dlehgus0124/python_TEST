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