import tkinter #tk-inteface is gui library

def set_tile(row,column):
    global curr_player

    # after game over i should not be able to play
    if(game_over):
        return

    # but i should not overwrite any value so
    if board[row][column]["text"] != "":
        # already taken spot
        return

    board[row][column]["text"] = curr_player #marking the board
    # iska matlab main jaise hi board pe click kru uspe current player ki value aa jaye

    # ab muje doosre player ki value ko switch bhi karna hai 
    if curr_player == playerO: 
        curr_player = playerX
    else:
        curr_player = playerO

    label["text"] = curr_player+"'s turn"

    check_winner()

def check_winner(): #check the conditions for winning the game
    # say if player got hoirzonatlly or vertically or diagonally filling he wins

    global turns,game_over

    # horizontally check 3 rows
    for row in range(3):
        if(board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"] and board[row][0]["text"] != ""):
            # pehle label change karenge 
            label.config(text=board[row][0]["text"]+" is the winner!" , foreground=color_yellow)

            # uss horizontal row ko highlight karenge
            for column in range(3):
                board[row][column].config(foreground=color_yellow, background=color_light_gray)

            game_over = True
            return

    # vertically check 3 rows
    for column in range(3):
        if(board[0][column]["text"] == board[1][column]["text"] == board[2][column]["text"] and board[0][column]["text"] != ""):
            # pehle label change karenge 
            label.config(text=board[0][column]["text"]+" is the winner!" , foreground=color_yellow)

            # uss horizontal row ko highlight karenge
            for row in range(3):
                board[row][column].config(foreground=color_yellow, background=color_light_gray)

            game_over = True
            return

    # diagonally check 3 rows
    # for column in range(3):
        if(board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"] and board[0][0]["text"] != ""):
            # pehle label change karenge 
            label.config(text=board[0][0]["text"]+" is the winner!" , foreground=color_yellow)

            # uss horizontal row ko highlight karenge
            for i in range(3):
                board[i][i].config(foreground=color_yellow, background=color_light_gray)

            game_over = True
            return
        
    # anti diagonally check 3 rows
    # for column in range(3):
        if(board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"] and board[0][2]["text"] != ""):
            # pehle label change karenge 
            label.config(text=board[0][2]["text"]+" is the winner!" , foreground=color_yellow)

            # uss horizontal row ko highlight karenge
            board[0][2].config(foreground=color_yellow, background=color_light_gray)
            board[1][1].config(foreground=color_yellow, background=color_light_gray)
            board[2][0].config(foreground=color_yellow, background=color_light_gray)

            game_over = True
            return

    # tie
    if(turns == 9):
        game_over = True
        label.config(text="Tie!" , foreground=color_yellow)

def new_game():
    global turns,game_over

    turns = 0
    game_over = False

    label.config(text = curr_player+"'s turn" , foreground="white")

    for row in range(3):
        for column in range(3):
            board[row][column].config(text="", foreground=color_blue, background=color_gray)

# game setup
playerX = 'X'
playerO = 'O'

curr_player = playerX

board = [[0,0,0],
         [0,0,0],
         [0,0,0]]

# colors for code
color_blue = "#4584b6"
color_yellow = "#ffde57"
color_gray = "#343434"
color_light_gray = "#646464"

turns = 0
game_over = False

# window setup
window = tkinter.Tk() #creates the game window
window.title = "Tic Tac Toe"
window.resizable(False,False)

# first create a frame - in that frame include each of your content and after that push your frame into the tk gui
frame = tkinter.Frame(window)
label = tkinter.Label(frame,text=curr_player+"'s turn", font=("Consolas", 20), background=color_gray , foreground="white")

label.grid(row=0, column=0, columnspan=3 , sticky="ew") #label packed in frame
# ew measn east to west ans ns means north to south

for row in range(3):
    for column in range(3):
        board[row][column] = tkinter.Button(frame, text="" , font=("Consolas",50,"bold"),background=color_gray, foreground=color_blue, width=4, height=1, command=lambda row=row, column=column : set_tile(row,column))
        
        board[row][column].grid(row=row+1, column=column)


button = tkinter.Button(frame, text="restart" , font=("Consolas", 20), background=color_gray, foreground="white", command = new_game)
button.grid(row=4, column=0, columnspan=3 , sticky="ew")

frame.pack() #frame packer in tk gui






# to center our window
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))

#format "(w)x(h)+(x)+(y)"
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

window.mainloop() #to run our window continuously
