import time
from typing import List, Tuple, Generator

class Life:
    state: List[List[bool]]
    m: int
    n: int
    def __init__( self, m : int, n : int ) :
        self.m = m
        self.n = n
        helperList = []
        self.state = []
        for x in range(self.m):
            for y in range(self.n):
                helperList.append(False)
            self.state.append(helperList)
            helperList = []

    def __repr__( self ) -> str:
        return str(self.state)

    def neighbours ( self, i : int, j : int ) -> Generator[ Tuple[ int, int ], None, None ]:
        if i - 1 >= 0 and i - 1 < self.m:
            if j - 1 >= 0 and j - 1 < self.n:
                yield ( i - 1, j - 1)
            if j >= 0 and j < self.n:
                yield ( i - 1, j)
            if j + 1 >= 0 and j + 1 < self.n:
                yield ( i - 1, j + 1)
        if i >= 0 and i < self.m:
            if j - 1 >= 0 and j - 1 < self.n:
                yield ( i, j - 1)
            if j + 1 >= 0 and j + 1 < self.n:
                yield ( i, j + 1)
        if i + 1 >= 0 and i + 1 < self.m:
            if j - 1 >= 0 and j - 1 < self.n:
                yield ( i + 1, j - 1)
            if j >= 0 and j < self.n:
                yield ( i + 1, j)
            if j + 1 >= 0 and j + 1 < self.n:
                yield ( i + 1, j + 1)

    def nextstate( self ) -> None :
        next : List[ List[ bool ] ]
        helperList = []
        next = []
        count = 0
        for x in range(self.m):
            for y in range(self.n):
                for pnt in self.neighbours( x, y ):
                    if( self.state[pnt[0]][pnt[1]] == True):
                        count += 1

                if(self.state[x][y] == True and (count == 2 or count == 3)):
                    helperList.append(True)
                elif( self.state[x][y] == False and count == 3):
                    helperList.append(True)
                else:
                    helperList.append(False)
                count = 0
            next.append(helperList)
            helperList = []
        self.state = next

    def addfigure( self, i : int, j : int, figure : List[ str ] ) -> None :
        if i < 0 or j < 0:
            raise ValueError( "Grid position can't be less than 0" )
        for x in range( i, i + len(figure) ):
            for y in range ( j, j + len(figure[x - i])):
                if x > self.m or y > self.n:
                    raise ValueError("Out of range")
                if figure[x - i][y - j] == '.' or figure[x - i][y - j] == ' ':
                    self.state[x][y] = False
                else:
                    self.state[x][y] = True

    def __str__(self) -> str :
        result = ""
        for x in range(self.m):
            for y in range (self.n):
                if self.state[x][y] == True:
                    result+="#"
                else:
                    result+="."
            result+="\n"
        return result

def start( ) :
    toad = [ ".###","###." ]
    blinker = [ "###" ]
    block = ["..##..", "..##.."]
    glidergun = ["...................................#............",
                 ".................................#.#............",
                 ".......................##......##............##.",
                 "......................#...#....##............##.",
                 "...........##........#.....#...##...............",
                 "...........##........#...#.##....#.#............",
                 ".....................#.....#.......#............",
                 "......................#...#.....................",
                 ".......................##......................."]
    lf = Life(50, 80)
    lf.addfigure(10, 10, glidergun)
    lf.addfigure(30, 10, toad)
    lf.addfigure(40, 15, blinker)
    while True:
        print(lf)
        print("press Ctrl-C to stop")
        lf.nextstate()
        time.sleep(0.25)


start()
