
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
    
def plot_book_scores(chapter_names, chapter_scores):
    
    plt.figure(figsize=(12, 8))
    
    pos = list(range(len(chapter_scores)))
    
    plt.plot(pos, list(chapter_scores))
    
    plt.xticks(pos, chapter_names, rotation=90)
    
    plt.show()

def plot_all_book_scores(all_names, all_scores):
    plt.figure(figsize=(20, 10))
    
    c = ['blue', 'green', 'yellow', 'red', 'black', 'orange', 'purple']
    
    previous = 0

    for idx, scores in enumerate(all_scores):
        pos = [i + previous for i in range(len(scores))]
        previous += len(scores)
        plt.plot(pos, scores, color=c[idx])

    plt.xlim((-0.5, previous + 0.5))
    xticks = [n for ns in all_names for n in ns]
    plt.xticks(list(range(len(xticks))), xticks, rotation=90, fontsize=6)
    
    plt.tight_layout()
    
    plt.savefig('all_chapters.pdf')
    
    plt.show()
