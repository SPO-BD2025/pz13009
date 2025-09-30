import pulp

# Создаем задачу на максимум
prob = pulp.LpProblem("Max_Problem", pulp.LpMaximize)

# Переменные
x = pulp.LpVariable('x', cat='Continuous')
y = pulp.LpVariable('y', cat='Continuous')

# Целевая функция
prob += y - x

# Ограничения
prob += y >= 0
prob += x + y <= 1
prob += x - 4*y >= -2

# Решение
prob.solve()

# Вывод результатов
print(f"x = {pulp.value(x)}")
print(f"y = {pulp.value(y)}")
print(f"Значение целевой функции: {pulp.value(prob.objective)}")
