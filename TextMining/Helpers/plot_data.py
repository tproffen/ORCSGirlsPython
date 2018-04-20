
#%matplotlib inline
import matplotlib.pyplot as plt
import matplotlib
plt.style.use('bmh')
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


def plot_words(data):

    words = []
    counts = []
    for d in data:
        words.append(d[0])
        counts.append(d[1])

    plt.figure(figsize=(12, 8))

    counts_len = len(counts)
    positions = range(counts_len)
    plt.bar(positions, counts)

    plt.xticks(positions, words, rotation=45)

    plt.show()
