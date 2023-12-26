class Robot:
    def __init__(self, width: int, height: int):
        self.w = width
        self.h = height
        self.cur = [0,0]
        self.dir = "East"
        self.dirs = {"East":[1,0],
                    "North":[0,1],
                    "West":[-1,0],
                    "South":[0,-1]
                    }
        self.nextdir={"East":"North",
                    "North":"West",
                    "West":"South",
                    "South":"East"}
    def step(self, num: int) -> None:
        # num = num % (2*(self.w-1) + 2*(self.h-1))
        num = num % ((2*self.w + 2*self.h) - 4)
        x = self.cur[0] + (self.dirs[self.dir][0])*num
        y = self.cur[1] + (self.dirs[self.dir][1])*num
        if x == 0 and y == 0:
            self.dir = "South"
        elif x == self.w-1 and y==0:
            self.dir = "East"
        elif x == self.w-1 and y== self.h-1:
            self.dir = "North"
        elif x == 0 and y== self.h-1:
            self.dir = "West"
        if 0 <= x < self.w and 0 <= y < self.h:
            self.cur = [x,y]
        else:
            self.dir = self.nextdir[self.dir]
            k = 0
            if x>=self.w:
                k = x-self.w + 1
                x = self.w-1
            elif x<0:
                k = 0-x
                x= 0
            elif y>=self.h:
                k = y-self.h + 1
                y = self.h-1
            elif y<0:
                k = 0-y
                y= 0
            self.cur = [x,y]
            self.step(k)


    def getPos(self) -> List[int]:
        return self.cur
    def getDir(self) -> str:
        return self.dir
        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()