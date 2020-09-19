import agent
import random
import game


class Oekosystem:

    def __init__(self):
        self.agents = []
        self.waiting = []
        for _ in range(100):
            self.agents.append(agent.Agent())
        self.echo = True

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
                    mutierter_agent = agent.Agent(maxi)
                    mutierter_agent.mutation(1, 10, 30)
                    score[0] += 1
                    self.waiting.append(mutierter_agent.copy())
                    self.waiting.append(maxi.copy())
                elif result == -1:
                    scorestring += "O"
                    mutierter_agent = agent.Agent(mini)
                    mutierter_agent.mutation(1, 10, 30)
                    self.waiting.append(mutierter_agent.copy())
                    self.waiting.append(mini.copy())
                    score[1] += 1
                else:
                    scorestring += "-"
                    self.waiting.append(maxi.copy())
                    self.waiting.append(mini.copy())
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
        self.reset_score('./score_save.txt')
        while True:
            all_score = [0, 0, 0]

            for agentss in self.agents:
                agentss.score = 0
            # self.neo.score = 0
            for j in range(50):
                random.shuffle(self.agents)
                for k in range(50):
                    # two agents are playing against each other
                    result = self.play(self.agents[k], self.agents[50 + k])
                    if result == 1:
                        self.agents[k].score += 4
                        all_score[0] += 1
                    elif result == -1:
                        self.agents[50 + k].score += 5
                        all_score[1] += 1
                    else:
                        self.agents[k].score += 2
                        self.agents[50 + k].score += 3
                        all_score[2] += 1

            self.agents.sort(key=lambda x: x.score)
            for i in range(len(self.agents)):
                self.agents[i].age += 1

            self.agents[99].save_setting('./weight_save.txt')

            if season % 10 == 0:
                print("\n\n\n Saison: " + str(season))
                gamerecorder = game.Game()
                self.play(self.agents[99], self.agents[98], gamerecorder)
                gamerecorder.print_out()
                print("Score: " + str(self.agents[98].score) + "   Age: " + str(self.agents[98].age))
                print("Score: " + str(self.agents[99].score) + "   Age: " + str(self.agents[99].age))
                print("\n Season Score: " + str(all_score))

            # kick noobs
            self.agents[0] = agent.Agent()
            for s in range(int(len(self.agents) * 0.01), int(len(self.agents) * 0.5)):
                self.agents[s] = agent.Agent(self.agents[len(self.agents) - 1])
                self.agents[s].mutation(1, 2, 10)

            # for mitte in range(int(len(self.agents) * 0.1), int(len(self.agents) * 0.6)):
            #    self.agents[mitte].mutation(0, 0, 0)

            season += 1
            self.save_score('./score_save.txt', all_score)

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

    def reset_score(self, file):
        f = open(file, 'w')
        f.write('[0, 0, 0]')
        f.close()

    def save_score(self, file, score):
        f = open(file, 'r')
        save_data = f.read() + '\n' + str(score)
        f.close()
        f = open(file, 'w')
        f.write(save_data)
        f.close()


if __name__ == '__main__':
    oko = Oekosystem()
    oko.liga()
