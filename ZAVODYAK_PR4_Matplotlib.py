import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0.0, 5, 0.1)
y = np.cos(x*np.pi)
plt.title('графік функціїcos(x*np.pi)')
plt.plot(x, y, c = 'r')
plt.grid()
plt.fill_between(x, y, where=y>-0, color='g', alpha=0.3)
plt.fill_between(x, y, where=y<-0, color='r', alpha=0.3)
plt.show()
