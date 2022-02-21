###Начало кода###
import requests #Библиотеки

login = input('Введите номер:  ') #Авторизация в консольке
password= input('Введите пароль:  ')

session = requests.Session()

def auth(login:str, password:str, two_fa:bool = False, code:str=None):
    return session.get(f'https://oauth.vk.com/token', params={
        'grant_type': 'password',
        'client_id': '6146827',
        'client_secret': 'qVxWRF1CwHERuIrKBnqe',
        'username': login,
        'password': password,
        'v': '5.131',
        '2fa_supported': '1',
        'force_sms': '1' if two_fa else '0',
        'code': code if two_fa else None
    }).json()

response = auth(login, password)

if 'validation_sid' in response:
    session.get("https://api.vk.com/method/auth.validatePhone", params={'sid': response['validation_sid'],'v': '5.131'})
    response = auth(login, password) #Если включена двухфакторка, то попросит тебя потрогать код из смс04ки
    code = input('Введите код из смс:  ')
    response = auth(login, password, two_fa=True, code=code)   

print(response)
###Конец кода###