import matplotlib.pyplot as plt
import numpy as np

raw_scores = [601, 582, 570, 570, 558, 553, 551, 545, 534, 530, 523, 523, 521, 521, 519, 514, 513, 509, 509, 500, 499, 495, 495, 495, 494, 491, 491, 486, 485, 485, 475, 454, 450]
b = len(raw_scores) + 1


raw_scores = sorted(raw_scores)
min = raw_scores[0]
max = raw_scores[-1]
# Use numpy to generate a bunch of random data in a bell curve around 5.
n = [n for n in raw_scores]

m = [m for m in range(len(raw_scores))]

plt.ylim([min, max])
plt.bar(m, n)
plt.title("Aguirre Raw Data for 2021 State Test")
plt.show()

plt.hist(n, bins=b, color='lightcoral')
plt.title("Histogram for Aguirre 2021 State Test")
plt.show()

plt.hist(n, cumulative=True, bins=b)
plt.title("Cumulative Histogram")
plt.show()

'''
import numpy as np
import matplotlib.pyplot as plt

# Fixing random state for reproducibility
np.random.seed(19680801)
N = 136
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = (30 * np.random.rand(N))**2  # 0 to 15 point radii

plt.scatter(n, m, s=20, c=colors, alpha=0.5)
plt.show()
'''
