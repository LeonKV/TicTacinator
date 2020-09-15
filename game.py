class Game:

    def __init__(self):
        self.moves = [[0,0,0,0,0,0,0,0,0]]

    def add_move(self, move):
        self.moves.append(move)

    def print_out(self):
        for move in self.moves:
            for n, i in enumerate(move):
                if(i == 0):
                    move[n] = " "
                if(i == 1):
                    move[n] = "X"
                if(i == -1):
                    move[n] = "O"
            for j in [0, 3]:
                print(" " + move[j] + " | " + move[j+1] + " | " + move[j+2])
                print("---|---|---")
            print(" " + move[6] + " | " + move[7] + " | " + move[8])
            print("_____________________")