import agent
import numpy
import random


class Oekosystem:

    def __init__(self):
        self.agents = []
        # agents play tictactoe
        for _ in range(100):
            self.agents.append(agent.Agent())

    # main trainings function
    def main(self):
        for i in range(100000):
            # [X wins, O wins, draw]
            score = [0, 0, 0]
            random.shuffle(self.agents)
            # 50 matches of tictactoe
            for _ in range(50):
                # two agents are playing against each other
                max = self.agents.pop(0)
                min = self.agents.pop(0)
                result = self.play(max, min)
                # max wins
                if result == 1:
                    self.agents.append(max)
                    mutierter_agent = agent.Agent(max)
                    mutierter_agent.mutation(5, 10, 15)
                    self.agents.append(mutierter_agent)
                    score[0] += 1
                #min wins
                elif result == -1:
                    self.agents.append(min)
                    mutierter_agent = agent.Agent(min)
                    mutierter_agent.mutation(5, 10, 15)
                    self.agents.append(mutierter_agent)
                    score[1] += 1
                # draw
                else:
                    self.agents.append(max)
                    self.agents.append(min)
                    score[2] += 1
            if i % 1000 == 0 or i % 1000 == 1 or i % 1000 == 2 or i % 1000 == 3 or i % 1000 == 4:
                print('Runde: ' + str(i) + 'Score: ' + str(score))
                # print(self.agents[0].weights1)

    # useless
    def deathmatch(self, max, min):
        # [max wins, min wins, draw]
        score = [0, 0, 0]
        for _ in range(5):
            winner = self.play(max, min)
            score[winner] += 1
        return score

    def play(self, max, min):
        board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(9):
            if i % 2 == 0:
                board[max.move_max(board)] = 1
                if self.winner(board):
                    return 1
            else:
                board[min.move_min(board)] = -1
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


oko = Oekosystem()
oko.main()
