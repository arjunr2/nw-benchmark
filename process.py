import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def main():
    with open("default.results", "r") as f:
        content = f.read()
        values = np.array([int(x) for x in content.split(',')[:-1]])
        print(values)

    print(values)
    fig, ax = plt.subplots()
    plt.xlim(right=20000)
    sns.histplot(values, binwidth=1000, stat='proportion', ax=ax)
    sns.ecdfplot(values, color='orange', stat='proportion', ax=ax)
    plt.ylabel('Density')
    plt.xlabel('Transmission time (us)')
    plt.savefig('hist.png')


if __name__ == '__main__':
    main()
