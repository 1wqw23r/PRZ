import numpy as np
from sklearn.neural_network import MLPRegressor

# Создание данных дляя обучения
# входные данные (пример)
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1],
    [2, 3],
    [-1, 4],
    [5, -2],
    [-3, -4]
])

# Целевые значения формулы - x1+0.5x2+2
y = X[:,0] + 0.5 * X[:,1] + 2

# Создание модели полносвязной НС
mlp = MLPRegressor(hidden_layer_sizes=(5,), activation='relu', max_iter=10000, random_state=42)

# Обучение модели
mlp.fit(X, y)

# Работа модели
test_samples = np.array([
    [3, 4],
    [-2, 8],
    [0, 0],
    [10, -10]
])

predictions = mlp.predict(test_samples)

for i, sample in enumerate(test_samples):
    actual = sample[0] + 0.5 * sample[1] + 2
    predicted = predictions[i]
    print(f"Вход: {sample}")
    print(f"Формула действительно: {actual}")
    print(f"Модель предсказания: {predicted}\n")