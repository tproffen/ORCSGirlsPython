
# %matplotlib inline

import matplotlib.pyplot as plt
import matplotlib
plt.style.use('seaborn-white')
matplotlib.rcParams.update({'font.size': 14})


def plot(data):

    # this tells matplotlib how large should the figure be
    plt.figure(figsize=(12, 8))

    # this creates the plot
    data_len = len(data)
    positions = range(data_len)
    plt.bar(positions, data)

    plt.xticks(positions, [x + 1 for x in positions])

    # this shows the horizontal lines
    plt.gca().yaxis.grid(True)

    # and this displays the plot!
    plt.show()
