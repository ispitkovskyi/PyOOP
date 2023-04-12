# def colour_set():
#     while True:
#         set = input("What colour your figure is?(W-White/B-Black)").lower()
#         if set.startswith("w"):
#             color = "white"
#         elif set.startswith("b"):
#             color = "black"
#         else:
#             continue
#         print(f"The colur of figure is {color}")
#         return color
# def setx_position():
#     while True:
#         rang = range(1,8)
#         x = int(input("Set position in line(1-8)"))
#         if x in rang:
#             x = x
#         else:
#             continue
#         print(x)
#         return x
# def  sety_position():
#     while True:
#         y = int(input("Set line(1-8)"))
#         if y in range(1, 8):
#             y = y
#         else:
#             continue
#         print(y)
#         return y
class Piece:

    def __init__(self, x, y, color):
        self.color = color
        self.x = x
        self.y = y

    def color_set(self):
        while True:
            set = input("What colour your figure is?(W-White/B-Black)").lower()
            if set.startswith("w"):
                self.color = "white"
            elif set.startswith("b"):
                self.color = "black"
            else:
                continue
            print(f"The color of figure is {self.color}")
            return

    def setx_position(self):
        while True:
            rang = range(1, 8)
            x = int(input("Set position in line(1-8)"))
            if x in rang:
                self.x = self.x - 1
            else:
                continue
            print(x)
            return

    def sety_position(self):
        while True:
            y = int(input("Set line(1-8)"))
            if y in range(1, 8):
                self.y = self.y - 1
            else:
                continue
            print(y)
            return

    def show_position(self):
        print(f"Figure was placed on position: {self.y}:{self.x}")




class Pawn(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        #self.move = ''

    def forward(self):
        if self.y>3:
            self.y-=1
        elif self.y<4:
            self.y+=1
        return self.x, self.y

    def diagonal_left(self):
        if self.y>3:
            self.y-=1
            self.x-=1
        elif self.y<4:
            self.y+=1
            self.x+=1
        return self.x, self.y

    def diagonal_right(self):
        if self.y>3:
            self.y+=1
            self.x+=1
        elif self.y<4:
            self.y-=1
            self.x-=1
        return self.x, self.y

class Knight(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)


    def q1_up(self):
        self.x += 1
        self.y -= 2
        return self.x, self.y
    def q1_down(self):
        self.x += 2
        self.y -= 1
        return self.x, self.y
    def q2_up(self):
        self.x -= 1
        self.y -= 2
        return self.x, self.y
    def q2_down(self):
        self.x -= 2
        self.y -= 1
        return self.x, self.y

    def q3_up(self):
        self.x -= 2
        self.y += 1
        return self.x, self.y
    def q3_down(self):
        self.x -= 1
        self.y += 2
        return self.x, self.y

    def q4_up(self):
        self.x += 2
        self.y += 1
        return self.x, self.y

    def q4_down(self):
        self.x += 1
        self.y += 2
        return self.x, self.y

class Bishop(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)

    def move(self):
        print(f"You can only move this figure using diagonal directions from position {self.x}:{self.y}")
        step = int(input("How many steps do you want to make?(1-8)"))
        x = step
        y = step
        if self.y+y < 9:
            print("Now you have to choose the direction(q1 - right up, q3 - left down).")
        else:
            print("Board doesn`t have anough space for this step")
            return self.x, self.y
        q = int(input("Which guarter of board is it?(1/2/3/4):"))
        if q == 1:
            self.x -= x
            self.y += y
        elif q == 2:
            self.x -= x
            self.y -= y
        elif q == 3:
            self.x -= x
            self.y += y
        elif q == 4:
            self.x += x
            self.y += y
        return self.x, self.y

class Rook(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)

    def move(self):
        print("This figure can be moved relatively vertical or horizontal axis.")
        step = int(input("How many steps do you want to make?"))
        direction = input("Which direction you choose?(U-Up, D-Down, R-Right, L-Left):").lower()
        if direction.startswith("u"):
            if self.y > 3:
                self.y -= step
            elif self.y < 4:
                self.y += step
        elif direction.startswith("d"):
            if self.y > 3:
                self.y += step
            elif self.y < 4:
                self.y -= step
        elif direction.startswith("r"):
            self.x += step
        elif direction.startswith("l"):
            self.y -= step
        return self.x, self.y
class Queen(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)

    def move_like_plus(self):
        step = int(input("How many steps do you want to make?"))
        direction = input("Which direction you choose?(U-Up, D-Down, R-Right, L-Left):").lower()
        if direction.startswith("u"):
            if self.y > 3:
                self.y -= step
            elif self.y < 4:
                self.y += step
        elif direction.startswith("d"):
            if self.y > 3:
                self.y += step
            elif self.y < 4:
                self.y -= step
        elif direction.startswith("r"):
            self.x += step
        elif direction.startswith("l"):
            self.y -= step
        return self.x, self.y

    def move_like_x(self):
        step = int(input("How many steps do you want to make?(1-8)"))
        x = step
        y = step
        if self.y + y < 9:
            print("Now you have to choose the direction(q1 - right up, q3 - left down).")
        else:
            print("Board doesn`t have anough space for this step")
            return self.x, self.y
        q = int(input("Which guarter of board is it?(1/2/3/4):"))
        if q == 1:
            self.x -= x
            self.y += y
        elif q == 2:
            self.x -= x
            self.y -= y
        elif q == 3:
            self.x -= x
            self.y += y
        elif q == 4:
            self.x += x
            self.y += y
        return self.x, self.y

class King(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)

    def move_like_plus(self):
        direction = input("Which direction you choose?(U-Up, D-Down, R-Right, L-Left):").lower()
        if direction.startswith("u"):
            if self.y > 3:
                self.y -= 1
            elif self.y < 4:
                self.y += 1
        elif direction.startswith("d"):
            if self.y > 3:
                self.y += 1
            elif self.y < 4:
                self.y -= 1
        elif direction.startswith("r"):
            self.x += 1
        elif direction.startswith("l"):
            self.y -= 1
        return self.x, self.y

    def move_like_x(self):
        x = 1
        y = 1
        if self.y + y < 9:
            print("Now you have to choose the direction(q1 - right up, q3 - left down).")
        else:
            print("Board doesn`t have anough space for this step")
            return self.x, self.y
        q = int(input("Which guarter of board is it?(1/2/3/4):"))
        if q == 1:
            self.x -= x
            self.y += y
        elif q == 2:
            self.x -= x
            self.y -= y
        elif q == 3:
            self.x -= x
            self.y += y
        elif q == 4:
            self.x += x
            self.y += y
        return self.x, self.y



#BOARD CLASS HERE:
class Board():
    # for i in range(1,8):
    #     for j in range(1,8):
    current_x = 0
    current_y = 0
    def __init__(self):
        self.board = [[0 for i in range(8)] for j in range(8)]
        return

    def place_piece(self, piece):
        print(self.board)
        self.board[piece.x-1][piece.y-1] = piece
        print(self.board, "after")
        return

    def move_piece(self, piece):
        self.place_piece(piece)
        self.board[self.current_x][self.current_y] = 0
        return

    def remove_piece(self,  piece):
        self.board[piece.x-1][piece.y-1] = 0
        return

    def get_piece_at_position(self, x, y):
        current_piece = self.board[x-1][y-1]
        if(not(isinstance(current_piece, Piece))):
            print("No figure at coordinates provided. Returning None")
            return None
        self.current_x = x-1
        self.current_y = y-1
        return current_piece

    def get_all_pieces(self):

        return

    def is_valid_move(self):

        return


# x = setx_position()
# y = sety_position()
# color = colour_set()
white = "white"
black = "black"
# body = Piece(x=x,y=y, color=color)
# pawn = Pawn(x=x,y=y, color=color)
# print(pawn.forward())
# print(pawn.diagonal_right())
# print(pawn.diagonal_left())
# knight = Knight(x=x,y=y, color=color)
# step = input("Step:").lower()
# if step.startswith("q2"):
#     direction = input("Direction:").lower()
#     if direction.startswith("u"):
#         print(knight.q2_up())
#     elif direction.startswith("d"):
#         print(knight.q2_down())
# bishop = Bishop(x=x,y=y, color=color)
# print(bishop.move())
# rook = Rook(x=x,y=y, color=color)
# print(rook.move())
queen = Queen(4, 4, black)
# type_of_step = input("How do you want queen to be replaced?('x' - diagonals, '+' - horisontal/vertical):").lower()
# if type_of_step.startswith("+"):
#     print(queen.move_like_plus())
# elif type_of_step.startswith("x"):
#     print(queen.move_like_x())
king = King(2, 3, white)
# type_of_step = input("How do you want king to be replaced?('x' - diagonals, '+' - horisontal/vertical):").lower()
# if type_of_step.startswith("+"):
#     print(king.move_like_plus())
# elif type_of_step.startswith("x"):
#     print(king.move_like_x())
board = Board()
board.place_piece(king)
board.place_piece(queen)
my_piece = board.get_piece_at_position(2, 3)
my_piece.move_like_plus()
#king.move_like_plus()
board.move_piece(my_piece)
board.remove_piece(my_piece)