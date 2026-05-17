import matplotlib.pyplot as plt
import numpy as np

s1 = np.array([3, 4, 5, 3])
s2 = np.array([1, 2, 2, 5])
s3 = np.array([2, 3, 3, 4])

index = np.arange(4)

plt.figure(figsize=(8, 5))
plt.axis([-0.5, 3.5, 0, 13])
plt.title('Групова складена діаграма')

plt.bar(index, s1, color='r', label='s1')
plt.bar(index, s2, color='b', bottom=s1, label='s2')
plt.bar(index, s3, color='g', bottom=(s2 + s1), label='s3')

plt.xticks(index, ['I кв.', 'II кв.', 'III кв.', 'IV кв.'])
plt.legend()
plt.show()