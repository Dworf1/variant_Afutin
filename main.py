# Создаем двумерный список
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

# Итерируемся по каждому элементу и находим максимальное значение
max_elem = matrix[0][0]
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] > max_elem:
            max_elem = matrix[i][j]

# Выводим результат
print('Наибольший элемент в двумерном списке:', max_elem)
