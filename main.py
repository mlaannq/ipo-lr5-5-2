str1 = str(input("Введите первую строку: ") )# запршиваем у пользователя первую строку
str2 = str(input("Введите вторую строку: ")) # запрашиваем у пользоваткля вторую строку
sort_str1 = sorted(str1.lower()) # преоброзовываем первую строку в нижний регистр и сортируем
sort_str2 = sorted(str2.lower()) # преоброзовываем вторую строку в нижний регистр и сортируем
if sort_str1 == sort_str2: # смотрим равны ли символы строк
	print("Анограммы") # выводим если строки анограммы
else: # если строки не равны
	print("Не анограммны") # выводим если они не анограммны

