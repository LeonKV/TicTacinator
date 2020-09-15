import agent
import player
import ecosystem


class Society(ecosystem.Oekosystem):

    def __init__(self):
        self.agent_smith = agent.Agent()
        self.agent_smith.update_skillset('./weight_save.txt')
        self.neo = player.Neo()

    def reach_freedom(self):
        result = self.play(self.neo, self.agent_smith)
        if result == 1:
            print('Matrix is doomed')
        elif result == -1:
            print('We are saved')
        else:
            print('Whats going on?')


if __name__ == '__main__':
    Earth = Society()
    Earth.reach_freedom()


