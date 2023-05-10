entered_array = input("Введите список чисел через пробел: ").split()
array = [int(i) for i in entered_array]
print("Вы ввели следующие числа: ", array)

while True:
    try:
        element = int(input("Введите одно число от 0 до 999: "))
        if element < 0 or element > 999:
            raise Exception
        break
    except ValueError:
        print("Введите целое число!")
    except Exception:
        print("Введенное число меньше 1 или больше 999")

array.append(element)

count = 0
for i in range(1, len(array)):
    x = array[i]
    idx = i
    while idx > 0 and array[idx-1] > x:
        array[idx] = array[idx-1]
        idx -= 1
        count += 1
    array[idx] = x

def binary_search(array, element, left, right):
    if left > right:
        return False
    middle = (right + left) // 2
    if element == array[middle + 1]:
        return middle
    elif element < array[middle + 1]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)

a = array.index(element)
b_search = binary_search(array, element, 0, len(array))

print("Список после сортировки и дополнения: ", array)
print("Счетчик итераций при сортировке элементов списка: ", count)
print("Номер позиции добавленного в список элемента: ", a)

if b_search > 0:
    print("Ответ: номер позиции элемента, который меньше введенного пользователем числа: ",
          binary_search(array, element, 0, len(array)))
else:
    print("Перед введенным числом элементы в списке отсутствуют!")
