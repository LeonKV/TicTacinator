import agent
import numpy
import random


class Oekosystem:

    def __init__(self):
        self.agents = []
        for _ in range(100):
            self.agents.append(agent.Agent())

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




    def main(self):
        for _ in range(1000):
            score = [0, 0, 0]
            random.shuffle(self.agents)
            for _ in range(50):
                max = self.agents.pop(0)
                min = self.agents.pop(0)
                result = self.play(max, min)
                if result == 1:
                    self.agents.append(max)
                    mutierter_agent = agent.Agent(max)
                    mutierter_agent.mutation(5, 10, 15)
                    score[0] += 1
                    self.agents.append(mutierter_agent)
                if result == -1:
                    self.agents.append(min)
                    mutierter_agent = agent.Agent(min)
                    mutierter_agent.mutation(5, 10, 15)
                    self.agents.append(mutierter_agent)
                    score[1] += 1
                else:
                    self.agents.append(max)
                    self.agents.append(min)
                    score[2] += 1
            print(score)

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
