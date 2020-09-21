#Global 
game_still_going=True
winner=None
current_player="X"
board=["-" , "-" , "-",
        "-" , "-" , "-",
        "-" , "-" , "-"]
def disp_board():
        print(board[0] + "|" + board[1] +"|" + board[2])
        print(board[3] + "|" + board[4] +"|" + board[5])
        print(board[6] + "|" + board[7] +"|" + board[8])

def play():
        disp_board()

        while game_still_going:
                handle_turn(current_player)
                check_if_game_over()
                flip_player()
                #game over
        if winner=="X" or winner=="O":
                print(winner+"won.")
        elif winner==None:
                print("Tie")

def handle_turn(player):
        print(player +"'s turn")
        valid=False
        while not valid:
                pos=input("Choose a position from 1-9:")
                while pos not in ["1","2","3","4","5","6","7","8","9"]:
                        pos=input("Choose a position from 1-9:")
                pos=int(pos)-1
                if board[pos]=="-":
                        valid=True
                else:
                        print("You can't go there")

        board[pos]=player
        disp_board()
def check_if_game_over():
        check_if_win()
        check_if_tie()
def check_if_win():
        #set value
        global winner
        #check rows,column,diagonal
        row_win=check_rows()
        cols_win=check_cols()
        diag_win=check_diagonals()
        if row_win:
                winner=row_win
        elif cols_win:
                winner=cols_win
        elif diag_win:
                winner=diag_win
        else :
                winner=None

        return



def check_rows():
        global game_still_going
        r_1=board[0]==board[1]==board[2]!="-"
        r_2=board[3]==board[4]==board[5]!="-"
        r_3=board[6]==board[7]==board[8]!="-"
        if r_1 or r_2 or r_3:
                game_still_going=False
        if r_1:
                return board[0]
        elif r_2:
                return board[3]
        elif r_3:
                return board[6]
        
def check_cols():
        global game_still_going
        c_1=board[0]==board[3]==board[6]!="-"
        c_2=board[1]==board[4]==board[7]!="-"
        c_3=board[2]==board[5]==board[8]!="-"
        if c_1 or c_2 or c_3:
                game_still_going=False
        if c_1:
                return board[0]
        elif c_2:
                return board[1]
        elif c_3:
                return board[2]
        
def check_diagonals():
        global game_still_going
        d_1=board[0]==board[4]==board[8]!="-"
        d_2=board[2]==board[4]==board[6]!="-"
        if d_1 or d_2:
                game_still_going=False
        if d_1:
                return board[0]
        elif d_2:
                return board[2]
                
def check_if_tie():
        #check board full
        global game_still_going
        if "-" not in board:
                game_still_going=False

        return
        
def flip_player():
        global current_player
        #change turn
        if current_player=="X":
                current_player="O"
        elif current_player=="O":
                current_player="X"

play()







