import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 30, 400)

y1 = (10.2*x - 149) / 3.2
y2 = (5.8*x + 83) / 16
y3 = (234 - 10.3*x) / 7.3

plt.figure(figsize=(12, 8))

plt.subplot(1, 2, 1)

plt.plot(x, y1, linestyle='-', label='10.2x1 - 3.2x2 = 149')
plt.plot(x, y2, linestyle='--', label='-5.8x1 + 16x2 = 83')
plt.plot(x, y3, linestyle=':', label='10.3x1 + 7.3x2 = 234')

A1 = np.array([[10.2, -3.2], [-5.8, 16]])
B1 = np.array([149, 83])
sol1 = np.linalg.solve(A1, B1)

A2 = np.array([[10.2, -3.2], [10.3, 7.3]])
B2 = np.array([149, 234])
sol2 = np.linalg.solve(A2, B2)

A3 = np.array([[-5.8, 16], [10.3, 7.3]])
B3 = np.array([83, 234])
sol3 = np.linalg.solve(A3, B3)

plt.scatter(sol1[0], sol1[1])
plt.scatter(sol2[0], sol2[1])
plt.scatter(sol3[0], sol3[1])

plt.text(sol1[0], sol1[1], ' A')
plt.text(sol2[0], sol2[1], ' B')
plt.text(sol3[0], sol3[1], ' C')

plt.title("All lines in one figure")
plt.xlabel("x1")
plt.ylabel("x2")
plt.legend()
plt.grid()

plt.subplot(3, 2, 2)
plt.plot(x, y1)
plt.title("10.2x1 - 3.2x2 = 149")
plt.grid()

plt.subplot(3, 2, 4)
plt.plot(x, y2)
plt.title("-5.8x1 + 16x2 = 83")
plt.grid()

plt.subplot(3, 2, 6)
plt.plot(x, y3)
plt.title("10.3x1 + 7.3x2 = 234")
plt.grid()

print("A:", sol1)
print("B:", sol2)
print("C:", sol3)

plt.tight_layout()

plt.savefig("result_like_example.png")

plt.show()