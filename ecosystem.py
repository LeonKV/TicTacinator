import agent
import agent
import numpy
import random
import game

class Oekosystem:

    def __init__(self):
        self.agents = []
        self.waiting = []
        for _ in range(100):
            self.agents.append(agent.Agent([50, 50]))
        self.echo = True

    def deathmatch(self, max, min):
        # [max wins, min wins, draw]
        score = [0, 0, 0]
        for _ in range(5):
            winner = self.play(max, min)
            score[winner] += 1
        return score

    def play(self, max, min, gamerecorder = None):
        board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(9):
            if i % 2 == 0:
                board[max.move_x(board)] = 1
                if gamerecorder != None:
                    gamerecorder.add_move(board.copy())
                if self.winner(board):
                    return 1
            else:
                board[min.move_o(board)] = -1
                if gamerecorder != None:
                    gamerecorder.add_move(board.copy())
                if self.winner(board):
                    return -1
        return 0

    def main(self):
        round = 0
        flag = False
        while(True):
            score = [0, 0, 0]
            scorestring = ""
            # random.shuffle(self.agents)
            for gamenumber in range(50):
                if round % 100 == 0 and gamenumber == 0:
                    flag = True
                    gamerecorder = game.Game()
                a = random.randint(0, 99 - 2 * gamenumber)
                maxi = self.agents.pop(a)
                b = random.randint(0, 98 - 2 * gamenumber)
                mini = self.agents.pop(b)
                if flag:
                    result = self.play(maxi, mini, gamerecorder)
                else:
                    result = self.play(maxi, mini)
                if result == 1:
                    scorestring += "X"
                    mutierter_agent = agent.Agent(0, maxi)
                    mutierter_agent.mutation(1, 10, 30)
                    score[0] += 1
                    self.waiting.append(mutierter_agent)
                    self.waiting.append(maxi)
                elif result == -1:
                    scorestring += "O"
                    mutierter_agent = agent.Agent(0, mini)
                    mutierter_agent.mutation(1, 10, 30)
                    self.waiting.append(mutierter_agent)
                    self.waiting.append(mini)
                    score[1] += 1
                else:
                    scorestring += "-"
                    self.waiting.append(maxi)
                    self.waiting.append(mini)
                    score[2] += 1
                if self.echo == True and flag == True:
                    flag = False
                    gamerecorder.print_out()
            self.agents = self.waiting.copy()
            self.waiting = []
            self.minimutate()
            if self.echo == True and round % 10 == 0:
                print(str(score) + " " + str(round) + " " + scorestring)
            round += 1

    def liga(self):
        season = 0
        while(True):
            all_score = [0, 0, 0]

            for agentss in self.agents:
                agentss.score = 0
            for j in range(10):
                random.shuffle(self.agents)
                for k in range(50):
                    # two agents are playing against each other
                    result = self.play(self.agents[k], self.agents[50 + k])
                    if result == 1:
                        self.agents[k].score += 2
                        all_score[0] += 1
                    elif result == -1:
                        self.agents[50 + k].score += 2
                        all_score[1] += 1
                    else:
                        self.agents[k].score += 1
                        self.agents[50 + k].score += 1
                        all_score[2] += 1

            self.agents.sort(key=lambda x: x.score)
            for i in range(len(self.agents)):
                self.agents[i].age += 1

            if season % 10 == 0:
                print("\n\n\n Saison: " + str(season))
                gamerecorder = game.Game()
                self.play(self.agents[99], self.agents[98], gamerecorder)
                gamerecorder.print_out()
                print("Score: " + str(self.agents[99].score) + "   Age: " + str(self.agents[99].age))
                print("\n Season Score: " + str(all_score))

                self.check_better_than_chance()

            # kick noobs
            av_age = 0
            max_age = 0
            for s in range(int(len(self.agents) * 0.1)):
                av_age += self.agents[s].age * (1 / (0.1 * len(self.agents)))
                if self.agents[s].age > max_age:
                    max_age = self.agents[s].age
                self.agents[s] = agent.Agent(0, self.agents[len(self.agents) - s - 1])
                self.agents[s].mutation(15, 100, 200)

            for s in range(int(len(self.agents) * 0.2)):
                self.agents[s + int(len(self.agents) * 0.1)].mutation(3, 50, 150)


            if season % 10 == 0:
                print("av. age kicked: " + str(av_age) + " & max age: " + str(max_age))

            season += 1

    def check_better_than_chance(self):
        wins = 0
        draws = 0
        agent = self.agents[50]
        for i in range(50):
            res = self.play_rand_x(agent)
            if res == 1:
                wins += 1
            if res == 0:
                draws += 1
        for i in range(50):
            res = self.play_rand_o(agent)
            if res == -1:
                wins += 1
            if res == 0:
                draws += 1
        print("Average Bot wins " + str(wins) + " and draws " + str(draws) + " of 100 games against random play")
        print("Score: " + str(wins + 0.5 * draws))


            
    def play_rand_x(self, agent, gamerecorder = None):
        board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(9):
            if i % 2 == 0:
                board[agent.move_x(board)] = 1
                if gamerecorder != None:
                    gamerecorder.add_move(board.copy())
                if self.winner(board):
                    return 1
            else:
                move = random.randint(0,8)
                while(board[move] != 0):
                    move = random.randint(0,8)
                board[move] = -1
                if gamerecorder != None:
                    gamerecorder.add_move(board.copy())
                if self.winner(board):
                    return -1
        return 0

    def play_rand_o(self, agent, gamerecorder = None):
        board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(9):
            if i % 2 == 0:
                move = random.randint(0,8)
                while(board[move] != 0):
                    move = random.randint(0,8)
                board[move] = 1
                if gamerecorder != None:
                    gamerecorder.add_move(board.copy())
                if self.winner(board):
                    return 1
            else:
                board[agent.move_o(board)] = -1
                if gamerecorder != None:
                    gamerecorder.add_move(board.copy())
                if self.winner(board):
                    return -1
        return 0



    def winner(self, v):
        for i in range(3):
            if v[i] == v[i+3] and v[i] == v[i+6] and v[i] != 0:
                return True
            i *= 3
            if v[i] == v[i+1] and v[i] == v[i+2] and v[i] != 0:
                return True
        if v[0] == v[4] and v[4] == v[8] and v[4] != 0:
            return True
        if v[2] == v[4] and v[4] == v[6] and v[4] != 0:
            return True
        return False

    def minimutate(self):
        for agent in self.agents:
            agent.mutation(2, 3, 5)


oko = Oekosystem()
oko.liga()
