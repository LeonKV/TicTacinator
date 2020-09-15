class Neo:

    def __init__(self):
        self.score = 0
        self.age = 0

    # Move gibt eine Stelle von 0 bis 8 aus auf die gespielt werden soll

    def move_o(self, board):
        printboard = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        i = 0
        for n in board:
            if (n == 0):
                printboard[i] = " "
            elif (n == 1):
                printboard[i] = "X"
            elif (n == -1):
                printboard[i] = "O"
            i += 1
        for j in [0, 3]:
            print(" " + printboard[j] + " | " + printboard[j + 1] + " | " + printboard[j + 2])
            print("---|---|---")
        print(" " + printboard[6] + " | " + printboard[7] + " | " + printboard[8])
        print("_____________________")
        stelle = int(input("Wohin willst du spielen?(0-8): "))
        return stelle - 1

    def move_x(self, board):
        printboard = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        i = 0
        for n in board:
            if (n == 0):
                printboard[i] = " "
            elif (n == 1):
                printboard[i] = "X"
            elif (n == -1):
                printboard[i] = "O"
            i += 1
        for j in [0, 3]:
            print(" " + printboard[j] + " | " + printboard[j + 1] + " | " + printboard[j + 2])
            print("---|---|---")
        print(" " + printboard[6] + " | " + printboard[7] + " | " + printboard[8])
        print("_____________________")
        stelle = int(input("Wohin willst du spielen?(1-9): "))
        return stelle - 1