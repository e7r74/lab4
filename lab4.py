# # print ("TASK 1.1 ")
# try:
#     user_input = input("string: ")
#     tuple_output = tuple(user_input)
#     print(tuple_output)
# except:
#     print("Error")
# print("функцию input() для получения строки от пользователя. Затем мы используем функцию tuple() для преобразования строки в кортеж.Если в процессе выполнения программы возникает ошибка, мы выводим сообщение “Error”.")
# print("TASK 1.2")
# my_tuple = ('T', 'h', 'e', 'B', 'i', 'g', 'B', 'e', 'n')
# my_string = ''.join(my_tuple)
# print(my_string)
# print("В первой строке мы создаем кортеж my_tuple. Затем мы используем функцию join() для преобразования кортежа в строку.")
# print("TASK 1.3")
# tuple_A = int(input("A"))
# tuple_B = int(input("B"))
# tuple_C = tuple_A[:len(tuple_A)//2] + tuple_B[len(tuple_B)//2:]
# print(tuple_C)
# print("для получения целых чисел tuple_A и tuple_B от пользователя. Затем мы используем срезы, чтобы выбрать первую половину элементов из tuple_A и вторую половину элементов из tuple_B. Затем мы объединяем эти две половины вместе, чтобы создать новый кортеж tuple_C.")
# print("TASK 1.4")
# def count_occurrences(t: tuple):
#     return tuple((x, t.count(x)) for x in set(t))
# t1 = (55, 6, 777, 54, 6, 76, 7777, 1, 777, 6)
# print("Sample Input 1:")
# print(t1)
# print("Sample Output 1:")
# print("Elements and their occurrences:")
# print(count_occurrences(t1))
# t2 = ('55', '6', '777', 54, 6, 7777, 9, 777, 6)
# print("Sample Input 2:")
# print(t2)
# print("Sample Output 2:")
# print("Elements and their occurrences:")
# print(count_occurrences(t2))
# t3 = ((1,2,3), (['A', 'B']), (1,2,3), (['A']))
# print("Sample Input 3:")
# print(t3)
# print("Sample Output 3:")
# print("Elements and their occurrences:")
#
# print(count_occurrences(t3))

# # print("TASK 1.5")
# t1 = (55, 6, 777, 70.0, '7', 'A')
# print("Sample Output :")
# print((t1[0], t1[1], t1[2]))
# print((t1[3],))
# print((t1[4], t1[5]))
# print("В первом операторе print() код выводит кортеж, содержащий первые три элемента t1. Во втором операторе print() код выводит кортеж, содержащий только четвертый элемент t1. В третьем операторе print() код выводит кортеж, содержащий пятый и шестой элементы t1.")
# print("TASK 2.1")
# s1 = 'TheBigBen'
# print("Sample Output :")
# print("Created set is:")
# print({c for c in s1})
# print("выражение {c for c in s1} для создания множества, содержащего все уникальные символы в строке s1.")
# print("TASK 2.2")
# set_A = {1,2,3,4,5}
# set_B = {5,7,8,9,2,10}
#
# print("Sample Output 1:")
# print(set_A.symmetric_difference(set_B))
# print(" print() код выводит симметричную разницу set_A и set_B, которая представляет собой набор элементов, которые находятся либо в set_A, либо в set_B, но не в обоих.")
# print("TASK 2.3")
#
# set_A = {1,2,3,4,5}
# set_B = {5,7,8,9,2,10}
#
# print("Sample Output 1:")
# print(set_A - set_B)
# print("мы создаем множества set_A и set_B. Затем мы используем оператор -, чтобы вычислить разность между множествами set_A и set_B.")
# print("TASK 2.4")
# set_A = {1, 2, 3, 4, 7}
# set_B = {8, 7, 9, 4, 2, 0, 10}
# set_C = {4, 0, 1}
#
# for element in set_C:
#     if element in set_A:
#         set_A.remove(element)
#         set_B.add(element)
#
# print("Updated set_C =", set_C)
# print("три набора set_A, set_B и set_C. Затем мы используем цикл for для перебора каждого элемента в set_C. Если текущим элементом является inset_A, мы удаляем его из set_A и добавляем в set_B.  print() для отображения обновленного set_C")
# print("TASK2.5")
# import itertools
#
# A = {1,2,3,4,5,6}
# n = 3
# m = 5
# result = [set(combo) for combo in itertools.combinations(A, n)][:m]
# print("Sample Output 1:")
# print(result)
# print(" A и два целых числа n и m. Затем код использует функцию combinations() из модуля itertools для генерации всех возможных комбинаций из n элементов из A. Затем код выбирает первые m комбинаций из списка всех возможных комбинаций и сохраняет их в новом списке, называемом result.код выводит содержимое результата.")
# # print("TASK 3.1")
# from collections import defaultdict
# cars_list = [('BMW', 'X6'), ('Toyota', 'Yaris'), ('Fiat', '500'), ('Fiat', 'Panda'), ('Toyota', 'Camry 30')]
# print("Sample Input 1:")
# print(cars_list)
# groups = defaultdict(list)
# for manufacturer, model in cars_list:
#     groups[manufacturer].append(model)
# print("Sample Output 1:")
# for manufacturer, models in groups.items():
#     print(f"{manufacturer} {len(models)}")
#     for model in models:
#         print(f"- {model}")
# print("В первых двух строках мы импортируем класс defaultdict из модуля collections и создаем список cars_list. Затем мы используем цикл for, чтобы перебрать каждый элемент в списке cars_list. В каждой итерации цикла мы добавляем текущую модель автомобиля в список моделей для текущего производителя автомобиля в словаре groups.for, чтобы перебрать каждый элемент в словаре groups. В каждой итерации цикла мы выводим на экран количество моделей для текущего производителя автомобиля, а затем перебираем каждую модель автомобиля и выводим ее на экран.")
