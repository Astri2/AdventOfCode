import re

def sumallunmarked(board):
    sum=0
    for column in board:
        for value in column:
            sum+=int(value[0])*(not(value[1]))
    return sum

def haswin(board,x,y):
    victory = True
    for value in board[x]: #
        if not(value[1]):
            victory = False
            break
    if(victory): 
        return True
    
    victory = True
    for column in board:
        if not(column[y][1]):
            victory = False
            break
    return victory

def win_action_1(boards, board, k):
    print("WIN",int(k)*sumallunmarked(board))
    return True

def win_action_2(boards, board, k):
    boards.remove(board)
    if(len(boards)==0):
        print("LAST",int(k)*sumallunmarked(board))
        return True
    return False                           

def bingo(order,boards,win_action):
    for k in order:
        i=0
        while i < len(boards):
            board = boards[i]
            for x in range(len(board)):
                for y in range(len(board[x])):
                    if board[x][y][0] == k:
                        if(not(board[x][y][1])):
                            board[x][y][1] = True
                            win = haswin(board,x,y)
                            if win:
                                if(win_action(*(boards,board,k))):
                                    return
                                i-=1
                                
            i+=1

def handle_input(path):
    content = open(path,'r').read()
    lines = content.splitlines()
    order = [k.replace("\\n","") for k in re.split(",",lines[0]) if k !=""]
    k = 1
    boards=[]
    while(k < len(lines)):
        boards.append([])
        for i in range(k+1,k+6):
            boards[-1].append([[j,False] for j in re.split("\\s+",lines[i]) if j != ""])
        k+=6
    return (order,boards)

def main():
    (order,boards) = handle_input("AdventOfCode2021\\D4\\input.txt")
    bingo(order,list(boards),win_action_1)
    bingo(order,list(boards),win_action_2)
    
if __name__ == "__main__":
    main()