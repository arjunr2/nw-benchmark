import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

with open("default.results", "r") as f:
    content = f.read()
    values = np.array([int(x) for x in content.split(',')[:-1]])
    print(values)

print(values)
fig, ax = plt.subplots()
#sns.kdeplot(values, ax=ax)
plt.xlim(right=20000)
sns.histplot(values, binwidth=1000, stat='proportion', ax=ax)
sns.ecdfplot(values, color='orange', stat='proportion', ax=ax)
#plt.hist(values, density=True, bins=30)
plt.ylabel('Density')
plt.xlabel('Transmission time (us)')
plt.savefig('hist.png')
