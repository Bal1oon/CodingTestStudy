# https://school.programmers.co.kr/learn/courses/30/lessons/17679

def find_rm_blocks(m, n, board):
    rm_blocks = set()
    for i in range(m-1):
            for j in range(n-1):
                if (
                    board[i][j] != ' ' and
                    board[i][j] == board[i+1][j] and
                    board[i][j] == board[i][j+1] and
                    board[i][j] == board[i+1][j+1]
                ):
                    rm_blocks.update({(i, j), (i+1, j), (i, j+1), (i+1, j+1)})
                    
    return rm_blocks

def rearrange_board(m, n, board):
    for j in range(n):
            stack = []
            for i in range(m):
                if board[i][j] != ' ':
                    stack.append(board[i][j])
            for i in range(m-1, -1, -1):
                board[i][j] = stack.pop() if stack else ' '
    return board
    
def solution(m, n, board):
    board = [list(i) for i in board]
    
    answer = 0
    while True:
        rm_blocks = find_rm_blocks(m, n, board)
        answer += len(rm_blocks)
        
        if not rm_blocks:
            break
        
        for i, j in rm_blocks:
            board[i][j] = ' '
            
        board = rearrange_board(m, n, board)
        
    return answer