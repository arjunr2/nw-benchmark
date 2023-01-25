import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from pathlib import Path

def plot(infile, outfile):
    with open(infile, "r") as f:
        content = f.read()
        values = np.array([int(x) for x in content.split(',')[:-1]])

    print(values)
    fig, ax = plt.subplots()
    plt.xlim(right=10000)
    sns.histplot(values, binwidth=1000, stat='proportion', ax=ax)
    sns.ecdfplot(values, color='orange', stat='proportion', linewidth=3, ax=ax)
    plt.ylabel('Density')
    plt.xlabel('Transmission time (us)')
    plt.savefig(outfile)

def main():
    res_dir = Path('nw_results')
    for infile in res_dir.glob('*'):
        outfile = Path("plots") / Path(infile.with_suffix('.png').name)
        plot(infile, outfile)

if __name__ == '__main__':
    main()
