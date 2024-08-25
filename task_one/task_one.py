import pulp

# Створюємо модель
model = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

# Змінні
x1 = pulp.LpVariable('Limonade', lowBound=0, cat='Continuous')
x2 = pulp.LpVariable('Fruit_Juice', lowBound=0, cat='Continuous')

# Цільова функція
model += x1 + x2, "Total_Production"

# Обмеження
model += 2 * x1 + x2 <= 100, "Water_Constraint"
model += x1 <= 50, "Sugar_Constraint"
model += x1 <= 30, "Lemon_Juice_Constraint"
model += 2 * x2 <= 40, "Fruit_Puree_Constraint"

# Розв'язання задачі
model.solve()

# Виведення результатів
print(f"Status: {pulp.LpStatus[model.status]}")
print(f"Кількість Лимонаду: {x1.varValue}")
print(f"Кількість Фруктового соку: {x2.varValue}")
print(f"Максимальна загальна кількість продуктів: {pulp.value(model.objective)}")
