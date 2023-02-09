import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from pathlib import Path

limit = 20000
tickwidth = 2000
binwidth = 1000

def plot(infile, outfile):
    with open(infile, "r") as f:
        content = f.read()
        values = np.array([int(x) for x in content.split(',')[:-1]])

    print(values)

    fig, ax = plt.subplots()

    # Obtain bins and clipped values > limit
    bins = np.arange(0, limit + binwidth, binwidth) 
    clipped_values = np.clip(values, bins[0], bins[-1])

    # Generate plot
    sns.histplot(clipped_values, bins=bins, stat='proportion', ax=ax)
    sns.ecdfplot(clipped_values, color='orange', stat='proportion', linewidth=3, ax=ax)

    # Set plot labels and width
    plt.xlim(right=limit+2*binwidth)

    ticks = np.arange(0, limit + tickwidth, tickwidth)
    xlabels = (ticks//1000).astype(str);
    xlabels[-1] = ">" + xlabels[-1]
    
    plt.xticks(ticks)
    ax.set_xticklabels(xlabels)
    plt.ylabel('Density')
    plt.xlabel('Transmission time (ms)')

    plt.savefig(outfile)
    plt.close()

def main():
    res_dir = Path('nw_results')
    for infile in res_dir.glob('*'):
        outfile = Path("plots") / Path(infile.with_suffix('.png').name)
        plot(infile, outfile)

if __name__ == '__main__':
    main()
