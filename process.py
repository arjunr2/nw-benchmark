import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from pathlib import Path


# Limit must be a multiple of binwidth and tickwidth
limit = 5000
tickwidth = 1000
binwidth = 100

def plot(infile, outfile):
    print("Processing ", infile)
    with open(infile, "r") as f:
        content = f.read()
        values = np.array([int(x) for x in content.split(',')[:-1]])

    print(f"Num values: ", values.size)
    print(f"Deadline misses (>{limit//1000}ms) = ", np.sum(values > limit))
    print(f"Std Dev = " + str(round(np.std(values))) + " us")
    print(f"Mean = " + str(round(np.mean(values))) + " us")
    print("--------------")

    fig, (ax, ax2) = plt.subplots(1, 2)
    plt.rcParams['figure.figsize'] = [14, 6]

    # Obtain bins and clipped values > limit
    bins = np.arange(0, limit + binwidth + 1, binwidth) 
    clipped_values = np.clip(values, bins[0], bins[-1])

    # Generate plot
    sns.histplot(clipped_values, bins=bins, stat='proportion', ax=ax)
    sns.ecdfplot(clipped_values, color='orange', stat='proportion', linewidth=3, ax=ax)

    # Set plot labels and width
    ax.set_xlim(right=limit+2*binwidth)

    ticks = np.arange(0, limit + tickwidth, tickwidth)
    xlabels = (ticks//1000).astype(str);
    xlabels[-1] = xlabels[-1] + '>'
    
    #ticks = np.append(ticks, limit + tickwidth);
    #xlabels = np.append(xlabels, ">" + xlabels[-1])

    #print(bins)
    #print(ticks)
    
    ax.set_xticks(ticks)
    ax.set_xticklabels(xlabels)
    ax.set_ylabel('Density')
    ax.set_xlabel('Transmission time (ms)')

    ax2.set_ylabel('Transmission time (ms)')
    ax2.set_xlabel('Packet #')
    ax2.plot(values/1000)
    #ax.plot(values)
    plt.savefig(outfile)
    plt.close()

def main():
    res_dir = Path('nw_results')
    for infile in res_dir.glob('*'):
        outfile = Path("plots") / Path(infile.with_suffix('.png').name)
        plot(infile, outfile)

if __name__ == '__main__':
    main()
