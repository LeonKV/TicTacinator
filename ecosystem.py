import agent
import numpy
import random
import game

class Oekosystem:

    def __init__(self):
        self.agents = []
        for _ in range(100):
            self.agents.append(agent.Agent())
        self.echo = True;

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
                board[max.move_max(board)] = 1
                if gamerecorder != None:
                    gamerecorder.add_move(board.copy())
                if self.winner(board):
                    return 1
            else:
                board[min.move_min(board)] = -1
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
            random.shuffle(self.agents)
            for gamenumber in range(50):
                if round % 100 == 0 and gamenumber == 0:
                    flag = True
                    gamerecorder = game.Game()
                max = self.agents.pop(0)
                min = self.agents.pop(0)
                if flag:
                    result = self.play(max, min, gamerecorder)
                else:
                    result = self.play(max, min)
                if result == 1:
                    self.agents.append(max)
                    mutierter_agent = agent.Agent(max)
                    mutierter_agent.mutation(1, 5, 15)
                    score[0] += 1
                    self.agents.append(mutierter_agent)
                elif result == -1:
                    self.agents.append(min)
                    mutierter_agent = agent.Agent(min)
                    mutierter_agent.mutation(1, 5, 15)
                    self.agents.append(mutierter_agent)
                    score[1] += 1
                else:
                    self.agents.append(max)
                    self.agents.append(min)
                    score[2] += 1
                if self.echo == True and flag == True:
                    flag = False
                    gamerecorder.print_out()
            if self.echo == True and round % 10 == 0:
                print(str(score) + " " + str(round))
            round += 1

    def liga(self):
        for i in range(1000):
            all_score = [0, 0, 0]
            print("\n\n\n Saison: " + str(i))
            for agentss in self.agents:
                agentss.score = 0
            for j in range(20):
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
            for agentss in self.agents:
                agentss.age += 1
                print("Score: " + str(agentss.score) + "   Age: " + str(agentss.age))
            print("\n Season Score: " + str(all_score))
            # kick noobs
            for s in range(int(len(self.agents) / 2)):
                self.agents[s] = agent.Agent(self.agents[50 + s])
                self.agents[s].mutation(5, 5, 15)


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


oko = Oekosystem()
oko.liga()
