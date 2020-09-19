import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import ast


score_x = []
score_o = []
score_draw = []
x_axis = []

style.use('default')
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)


def animate(self):
    file = open('./score_save.txt', 'r')
    count = 0
    for line in file:
        scores = ast.literal_eval(line)
        score_x.append(scores[0])
        score_o.append(scores[1])
        score_draw.append(scores[2])
        count += 1
        x_axis.append(count)
    file.close()
    ax1.clear()
    lines = ax1.plot(x_axis, score_x, 'bp', x_axis, score_o, 'rp', x_axis, score_draw, 'gp')
    plt.setp(lines, linewidth=0.5)


plt.ylabel('Wins')
plt.xlabel('Seasons')
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()