
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 1000 simulations of die roll
n = 1000

# In each simulation, there is one trial more than the previous simulation
avg = []
for i in range(2,n):
    print(f'{n}')
    a = np.random.randint(1,7,i)
    avg.append(np.average(a))

def clt(current):
    print(f'clt {current}')
    # if animation is at the last frame, stop it
    plt.cla()
    if current == 1000:
        a.event_source.stop()

    plt.hist(avg[0:current])

    plt.gca().set_title('Expected value of die rolls')
    plt.gca().set_xlabel('Average from die roll')
    plt.gca().set_ylabel('Frequency')

    plt.annotate('Die roll = {}'.format(current), [3,27])

fig = plt.figure()
a = animation.FuncAnimation(fig, clt, interval=1)
plt.show()
