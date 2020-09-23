import requests

# Для успешного вызова методов API необходимы:

# Корректные заголовки Accept и Content-Type. API QIWI Кошелька поддерживает только один MIME-тип: application/json. Любое другое значение приведет к ошибке формата данных.
# URL, составленный согласно требованиям к нужному запросу.
# OAuth-токен, выданный вам для доступа к вашему QIWI кошельку. Для некоторых запросов его не потребуется.

# Профиль пользователя
def get_profile(api_access_token):
    s7 = requests.Session()
    s7.headers['Accept']= 'application/json'
    s7.headers['authorization'] = 'Bearer ' + api_access_token
    p = s7.get('https://edge.qiwi.com/person-profile/v1/profile/current?authInfoEnabled=true&contractInfoEnabled=true&userInfoEnabled=true')
    return p.json()

# Следущий этап - идентификация пользователяю
def get_identification(api_access_token, my_login):
    s = requests.Session()
    s.headers['authorization'] = 'Bearer ' + api_access_token # Ввести токен пользователя
    res = s.get('https://edge.qiwi.com/identification/v1/persons/'+my_login+'/identification') # my_login - номер телефона пользователя
    return res.json()

# Проверить лимиты кошелька

# Все лимиты QIWI Кошелька
def limits(login, api_access_token):
    types = [ 'TURNOVER', 'REFILL', 'PAYMENTS_P2P', 'PAYMENTS_PROVIDER_INTERNATIONALS', 'PAYMENTS_PROVIDER_PAYOUT', 'WITHDRAW_CASH']
    s = requests.Session()
    s.headers['Accept']= 'application/json'
    s.headers['Content-Type']= 'application/json'
    s.headers['authorization'] = 'Bearer ' + api_access_token
    parameters = {}
    for i, type in enumerate(types):
        parameters['types[' + str(i) + ']'] = type
    b = s.get('https://edge.qiwi.com/qw-limits/v1/persons/' + login + '/actual-limits', params = parameters)
    return b.json()

# История платежей - сумма за диапазон дат
def payment_history_summ_dates(my_login, api_access_token, start_Date, end_Date):
    s = requests.Session()
    s.headers['authorization'] = 'Bearer ' + api_access_token
    parameters = {'startDate': start_Date,'endDate': end_Date}
    h = s.get('https://edge.qiwi.com/payment-history/v2/persons/' + my_login + '/payments/total', params = parameters)
    return h.json()

my_login = input('Введите ваш номер телефона: ')
api_access_token = input('Введите ваш token: ')
start_Date = input('Введите дату начала периода в формате ГГГГ-ММ-ДДTчч:мм:ссTZD: ')
end_Date = input('Введите дату конца периода в формате ГГГГ-ММ-ДДTчч:мм:ссTZD: ')

print(payment_history_summ_dates(my_login, api_access_token, start_Date, end_Date))