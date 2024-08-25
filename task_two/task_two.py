import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

# Визначення функції
def f(x):
    return x**2

# Межі інтегрування
a = 0
b = 2

# Метод Монте-Карло
N = 10000  # Кількість випадкових точок
x_random = np.random.uniform(a, b, N)
y_random = f(x_random)
integral_monte_carlo = (b - a) * np.mean(y_random)

# Точний інтеграл за допомогою SciPy
integral_exact, error = spi.quad(f, a, b)

print(f"Інтеграл (метод Монте-Карло): {integral_monte_carlo}")
print(f"Інтеграл (точний, SciPy): {integral_exact}")

# Висновки
difference = abs(integral_monte_carlo - integral_exact)
print(f"Різниця між результатами: {difference}")

# Графік функції та області інтегрування
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()

# Збереження графіка у файл
plt.savefig('graph.png')

# Відображення графіка
plt.show()
