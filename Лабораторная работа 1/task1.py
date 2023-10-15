numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
sum1 = sum(numbers[:4])
sum2 = sum(numbers[5:])
sum_ = sum1 + sum2
average_ = sum_ / len(numbers)
numbers[4] = average_
# TODO заменить значение пропущенного элемента средним арифметическим

print("Измененный список:", numbers)
