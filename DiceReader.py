import d20
from d20 import utils
import numpy as np
import matplotlib as plt
binop = d20.roll("3d6")
print(binop)
left = binop.expr
print(left)
dieroll = left.roll
print(dieroll)
dievalues = dieroll.num
print(dievalues)
diesize = dieroll.size
print(diesize)
# time to do this in a cringe fashion using arrays
probabilities = [None] * dievalues
for i in range(dievalues):
    count = 1
    arr = [None] * diesize
    for j in range (diesize):
        arr[j] = j+1
        count += 1
    probabilities[i] = arr
print(type(probabilities[0]))
matrix = probabilities[0]@probabilities[1]

# plt.figure(figsize=(10, 6))
# sns.histplot(sample_means, bins=30, kde=True, color='lightgreen')
# plt.title('Sampling Distribution of the Mean (Fair Die)')
# plt.xlabel('Sample Mean')
# plt.ylabel('Frequency')
# plt.axvline(np.mean(sample_means), color='red', linestyle='--', label='Mean')
# plt.legend()
# plt.grid(True)
# plt.show()
