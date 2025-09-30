import matplotlib.pyplot as plt
import numpy as np

# Область построения
x = np.linspace(-3, 2, 400)
y = np.linspace(-1, 2, 400)
X, Y = np.meshgrid(x, y)

# Построение ограничений
plt.contourf(X, Y, (Y >= 0) & (X + Y <= 1) & (X - 4*Y >= -2), colors='lightgray')

# Линии ограничений
plt.plot(x, np.zeros_like(x), 'k--', label='$y=0$')
plt.plot(x, 1 - x, 'k-', label='$x+y=1$')
plt.plot(x, (x + 2)/4, 'k-', label='$x-4y=-2$')

# Оптимальная точка
plt.plot(-2, 0, 'ro', markersize=8)

plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)

# Оформление графика
plt.xlim(-3, 2)
plt.ylim(-1, 2)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Графическое решение задачи линейного программирования')
plt.legend()
plt.gca().set_aspect('equal', adjustable='box')  # Сохранение пропорций

# Добавление стрелок на осях
plt.arrow(-3, 0, 0.1, 0, head_width=0.05, head_length=0.1, fc='k', ec='k')
plt.arrow(0, -1, 0, 0.1, head_width=0.05, head_length=0.1, fc='k', ec='k')

# Добавление надписи оптимальной точки
plt.text(-2, 0.1, '(-2, 0)', color='red')

# Сохранение графика
plt.savefig('graph.png', bbox_inches='tight')
plt.show()
