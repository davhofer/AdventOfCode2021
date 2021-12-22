import math
import itertools


day = 4

# get input
with open(f'{day}.txt', 'r') as f:
    input = f.read().strip().split('\n')  # f.readlines()



bingo_numbers = input[0]

# input = list(map(int,input))

ans = 0

class Board:
    def __init__(self):
        self.numbers = []
        self.check = [[0 for j in range(5)] for i in range(5)]
    
    def add(self,row):
        l = row.split(' ')
        self.numbers.append([])
        for x in l:
            if x != '':
                self.numbers[-1].append(x)


    def has_bingo(self):
        for i in range(5):
            if sum(self.check[i]) == 5:
                ans = 0
                for a in range(5):
                    for b in range(5):
                        if self.check[a][b] == 0:
                            ans += int(self.numbers[a][b])
                return True,ans
            s = []
            for j in range(5):
                s.append(self.check[j][i])
            if sum(s) == 5:
                ans = 0
                for a in range(5):
                    for b in range(5):
                        if self.check[a][b] == 0:
                            ans += int(self.numbers[a][b])
                return True,ans
        return False,[]

    def draw(self,number):
        for i in range(5):
            for j in range(5):
                if self.numbers[i][j] == number:
                    self.check[i][j] = 1
                    return

boards = []
b = None
# process input
for l in input[1:]:
    if l == '':
        if b is not None:
            boards.append(b)
        b = Board()
    else:
        b.add(l)

boards.append(b)

s= 0
for n in bingo_numbers.split(','):
    new_boards = []
    for b in boards:
        b.draw(n)
        ans,res = b.has_bingo()
        if ans:
            if len(boards) == 1:

            
                print("BINGO")
                nn = int(n)
                s = res*nn
                print(s)
                break
        else:
            new_boards.append(b)
    if s != 0:
        break
    boards = new_boards




# solve problem


