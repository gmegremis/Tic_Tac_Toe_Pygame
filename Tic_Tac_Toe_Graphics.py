import pygame

#colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
CYAN = (0, 255, 255)

# window setup
WIDTH, HEIGHT = 600, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe!")

# globals
x = pygame.image.load(r"C:\Users\user\Desktop\Giorgos\Python\VScode\Tic_Tac_Toe_GraphicsVersion\x_photo.png")
x = pygame.transform.scale(x, (120, 120))
player = 1
board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

def update_window():
    pygame.display.update()
    WIN.fill(BLACK)

def move(row, column, player):
    board[row][column] = player

def display_moves():
    for row in range(3):
        for col in range(3):
            if board[row][col] == 1:
                WIN.blit(x, (row*200+40, col*200+40))
            if board[row][col] == 2:
                pygame.draw.circle(WIN, GREEN, (int(row * 200 + 100), int(col * 200 + 100)), 65)
                pygame.draw.circle(WIN, BLACK, (int(row * 200 + 100), int(col * 200 + 100)), 50)

def draw_lines():
    pygame.draw.line(WIN, RED, (WIDTH/3, 0), (WIDTH/3, 600), 10)
    pygame.draw.line(WIN, RED, (2*WIDTH/3, 0), (2*WIDTH/3, 600), 10)
    pygame.draw.line(WIN, RED, (0, HEIGHT/3), (600, HEIGHT/3), 10)
    pygame.draw.line(WIN, RED, (0, 2*HEIGHT/3), (600, 2*HEIGHT/3), 10)

def message_box(situation):
    pygame.font.init()
    winner_font = pygame.font.SysFont("comicsans", 100)
    draw_font = pygame.font.SysFont("comicsans", 50)

    if situation == "D":
       message = draw_font.render("That's a draw!", 5, CYAN) 
       WIN.blit(message, (120, HEIGHT/3 - 50))
    elif situation == "W" and player == 1:
        message = winner_font.render("O won!", 5, CYAN)
        WIN.blit(message, (130, HEIGHT/3 - 50))
    elif situation == "W" and player == 2:
        message = winner_font.render("X won!", 5, CYAN)
        WIN.blit(message, (130, HEIGHT/3 - 50))

def check_rows():
    
    if board[0][0] == board[1][0] == board[2][0] != 0:
        return True 
    elif board[0][1] == board[1][1] == board[2][1] != 0:
        return True 
    elif board[0][2] == board[1][2] == board[2][2] != 0:
        return True 
    else:
        return False

def check_columns():
    if board[0][0] == board[0][1] == board[0][2] != 0:
        return True 
    elif board[1][0] == board[1][1] == board[1][2] != 0:
        return True 
    elif board[2][0] == board[2][1] == board[2][2] != 0:
        return True 
    else:
        return False

def check_diagonals():
    if board[0][0] == board[1][1] == board[2][2] != 0:
        return True 
    elif board[0][2] == board[1][1] == board[2][0] != 0:
        return True 
    else:
        return False

def check_for_winner():

    if check_rows() or check_columns() or check_diagonals():
        return True
    else:
        return False

def draw():
    flag = True

    for row in range(3):
        for col in range(3):
            if board[row][col] == 0:
                flag = False

    if flag == True:
        return True
    else:
        return False


def main():    
    Run = True
    clock = pygame.time.Clock()
    FPS = 60

    while Run:
        update_window()
        draw_lines()
        display_moves()

        if check_for_winner():
            message_box("W")
        elif draw():
            message_box("D")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()

                clicked_row = int(mx // (WIDTH/3))
                clicked_col = int(my // (HEIGHT/3))

                if board[clicked_row][clicked_col] == 0:
                    global player

                    move(clicked_row, clicked_col, player)

                    if player == 1:
                        player = 2
                    else:
                        player = 1

    pygame.quit()

def main_menu_setup():
    pygame.font.init()
    MAIN_MENU_FONT = pygame.font.SysFont("comicsans", 30)

    welcome = MAIN_MENU_FONT.render("Welcome to the Tic Tac Toe Game!", 5, WHITE)
    WIN.blit(welcome, (50, HEIGHT/3 - 100))

    instruction = MAIN_MENU_FONT.render("Press any key or click mouse to start...", 5, WHITE)
    WIN.blit(instruction, (40, HEIGHT/3 + 100))


# main menu setup
while True:
    pygame.display.update()

    main_menu_setup()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
            main()
        elif event.type == pygame.QUIT:
            pygame.quit()
