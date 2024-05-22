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
