
# Импорт необходимых библиотек

# Основания библиотека
from flask import Flask
# Позволяет получать запросы
from flask import request
# Позволяет преобразовывать python словарь в json
from flask.json import jsonify

#  Тело сервиса

# Подготовка приложения к работе
APP = Flask(__name__)

# Описание функции
# в '/...' записан адрес функции
# methods=['GET', 'POST', ...] - http-методы, которые принимает функция
@APP.route('/', methods=['GET'])
def index(): # тут может быть любое название, суть в том, что метод APP.route принимает эту функцию (index) на вход
    # создаем словарь
    answer = {}
    # Записываем туда информацию (ключ может быть любым! как и значение, впрочем)
    answer['message'] = 'hello student!'
    # Вызывая функцию jsonify(...) преобразуем answer в формат JSON
    return jsonify(answer)

# Обратите внимание, что тут другой адрес функции, и название. Реализуется http-метод GET
@APP.route('/hello', methods=['GET'])
def hello(): 
    answer = {}
    answer['message_1'] = 'hello student!'
    answer['message_2'] = 'It is a nice day today! Isn`t it?'
    return jsonify(answer)

# Обратите внимание, что тут другой адрес функции, и название. Реализуется http-метод POST
@APP.route('/yourmsg', methods=['POST'])
def yourmsg():
    # Получили посланный документ и преобразовали из JSON в словарь python
    jdict = request.get_json(force=True)
    mes = jdict['message']
    answer = {}
    answer['message'] = "Your message is: '{}'".format(mes)
    return jsonify(answer)

# Обратите внимание, что тут другой адрес функции, и название. Реализуется http-метод POST
@APP.route('/story', methods=['POST'])
def story():
    # Получили посланный документ и преобразовали из JSON в словарь python
    jdict = request.get_json(force=True)
    answer = {}
    answer['message'] = "Hello {} {}! Your age is {}. You are so young! Your favourite PL is {}".format(jdict['surname'],
                                                                                                        jdict['name'],
                                                                                                        jdict['age'],
                                                                                                        jdict['fav_pl']
                                                                                                       )
    return jsonify(answer)

# Обратите внимание, что тут другой адрес функции, и название. Реализуется http-метод POST
@APP.route('/intexample', methods=['POST'])
def intexample():
    # Получили посланный документ и преобразовали из JSON в словарь python
    jdict = request.get_json(force=True)
    mes = int(jdict['integer'])
    answer = {}
    answer['message'] = str(mes - 2)
    return jsonify(answer)


# Запускаем веб-сервис

APP.run()
