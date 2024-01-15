from flask import Blueprint, redirect, url_for
lab1 = Blueprint('lab1', __name__)


@lab1.route('/')
@lab1.route('/index')
def start():
    return redirect('/menu', code=302)


@lab1.route('/menu')
def menu():
    return '''
    <!doctype html>
    <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    <html>
        <head>
            <title>НГТУ, ФБ, Лабораторные работы</title>
        </head>
        <body>
            <header>
                НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
            </header>
            <main>
                <div>
                    <a href='/lab1'>Первая лабораторная</a>
                </div>
                <div>
                    <a href='/lab2'>Вторая лабораторная</a>
                </div>
                <div>
                    <a href='/lab3'>Третья лабораторная</a>
                </div>
                    <a href='/lab4'>Четвертая лабораторная</a>
                </div>
                <div>
                    <a href='/lab5'>Пятая лабораторная</a>
                </div>
            </main>
            <footer>
                Постников Кирилл Николаевич, ФБИ-14, 3 курс, 2023
            </footer>
        </body>
    </html>
    '''


@lab1.route('/lab1')
def lab():     
    return '''
    <!doctype html>
    <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    <html>
        <head>
            <title>Постников Кирилл Николаевич, лабораторная 1</title>
        </head>
        <body>
            <header>
                НГТУ, ФБ, Лабораторная работа 1
            </header>
            <main>
                <h1>Web-сервер на flask</h1>

                <div>
                    Flask — фреймворк для создания веб-приложений на языке
                    программирования Python, использующий набор инструментов
                    Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
                    называемых микрофреймворков — минималистичных каркасов
                    веб-приложений, сознательно предоставляющих лишь самые базовые возможности.
                </div>
                    <a href='/menu'>Меню</a>
                    <h2>Реализованные роуты</h2>
                    <ul>
                        <li>
                            <a href='lab1/oak'>Дуб</a>
                        </li>
                        <li>
                            <a href='lab1/student'>Студент</a>
                        </li>
                        <li>
                            <a href='lab1/python'>Python</a>
                        </li>
                        <li>
                            <a href='lab1/crypto'>Crypto</a>
                        </li>
                    </ul>
            </main>
            <footer>
                &copy; Кирилл Постников, ФБИ-14, 3 курс, 2023
            </footer>
        </body>
    </html>
    '''


@lab1.route('/lab1/oak')
def oak():
    return '''
    <!doctype html>
    <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    <html>
        <body>
            <header>
                НГТУ, ФБ, Лабораторная работа 1
            </header>
            <main>
                <h1>Дуб</h1>
                <img src="'''+ url_for('static', filename='oak.jpg') +'''">
            </main>
            <footer>
                &copy; Кирилл Постников, ФБИ-14, 3 курс, 2023
            </footer>
        </body>
    </html>
    '''


@lab1.route('/lab1/student')
def student():
    return '''
    <!doctype html>
    <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    <html>
        <body>
            <header>
                НГТУ, ФБ, Лабораторная работа 1
            </header>
            <main>
                <h1 class='student'>Постников Кирилл Николаевич</h1>
                <img class='logo' src="'''+ url_for('static', filename='nstu_logo.jpg') +'''">
            </main>
            <footer>
                &copy; Кирилл Постников, ФБИ-14, 3 курс, 2023
            </footer>
        </body>
    </html>
'''


@lab1.route('/lab1/python')
def python():
    return '''
    <!doctype html>
    <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    <html>
        <body>
            <header>
                НГТУ, ФБ, Лабораторная работа 1
            </header>
            <main>
                <div>
                    <p>Python не требует явного объявления переменных, является регистро-зависим 
                    (переменная var не эквивалентна переменной Var или VAR — это три разные переменные) 
                    объектно-ориентированным языком.</p>
                    <p>Python содержит такие структуры данных как списки (lists), кортежи (tuples) и словари
                    (dictionaries). Списки — похожи на одномерные массивы 
                    (но вы можете использовать Список включающий списки — многомерный массив), 
                    кортежи — неизменяемые списки, словари — тоже списки, но индексы могут быть любого типа, 
                    а не только числовыми. "Массивы" в Python могут содержать данные любого типа, 
                    то есть в одном массиве может могут находиться числовые, строковые и другие типы данных. 
                    Массивы начинаются с индекса 0, а последний элемент можно получить по индексу -1 
                    Вы можете присваивать переменным функции и использовать их соответственно.</p>
                </div>
                <img class='python' src="'''+ url_for('static', filename='python.png') +'''">
            </main>
            <footer>
                &copy; Кирилл Постников, ФБИ-14, 3 курс, 2023
            </footer>
        </body>
    </html>
'''


@lab1.route('/lab1/crypto')
def crypto():
    return '''
    <!doctype html>
    <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    <html>
        <body>
            <header>
                НГТУ, ФБ, Лабораторная работа 1
            </header>
            <main>
                <img class='crypto' src="'''+ url_for('static', filename='binance.jpg') +'''">
                <div>
                    <p>Binance заключила соглашение о продаже всего своего российского бизнеса компании CommEX. 
                    С целью обеспечения планомерного перехода существующих пользователей на другую платформу, 
                    процесс отключения займет до одного года. Все активы текущих российских пользователей в 
                    безопасности и надежно защищены.</p>

                    <p>“Смотря в будущее, мы признаем, что работа в России несовместима со стратегией Binance по 
                    соблюдению требований”, — сказал Ной Перлман, директор по соблюдению нормативных требований. 
                    “Мы по-прежнему уверены в долгосрочном развитии индустрии Web3 на глобальном уровне и собираемся 
                    направить нашу энергию на развитие Binance в более чем ста странах, где мы ведем нашу деятельность”.</p>

                    <p>В ходе организованной и последовательной миграции пользователей Binance совместно с CommEX примут 
                    все необходимые меры для информирования пользователей о процедуре переноса их активов на платформу 
                    CommEX. Новые пользователи, прошедшие процедуру верификации персональных данных, будут частично 
                    перенаправлены на платформу CommEX.</p>

                    <p>В течение следующих нескольких месяцев Binance закроет биржевые сервисы и прочие бизнес-направления
                    в России, прилагая все усилия для обеспечения бесперебойного взаимодействия с пользователем во время 
                    этого перехода.</p>

                    <p>Несмотря на то, что финансовые подробности сделки остаются конфиденциальными, следует отметить, 
                    что в рамках этого соглашения Binance полностью прекращает свою деятельность в России. 
                    В отличие от сделок, ранее осуществленных международными компаниями в России, в рамках данной 
                    сделки у Binance не останется права на получение части прибыли после продажи и возможности 
                    обратного выкупа долей в бизнесе.</p>
                </div>
            </main>
            <footer>
                &copy; Кирилл Постников, ФБИ-14, 3 курс, 2023
            </footer>
        </body>
    </html>
'''
