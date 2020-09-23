#Импорт всех функций модуля SimpleQIWI
import json, csv, calendar, time, requests
from SimpleQIWI import *

# Профиль пользователя инициализация
print("Введите токен:")
token = input()         # https://qiwi.com/api
print("Введите телефон:")
phone = input()

# ввод новой переменной api связывающий параметры доступа tokena с программой

api = QApi(token=token, phone=phone)

# Вывод баланса пользователя на экран
print(api.balance)
print(api.payments)