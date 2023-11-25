from flask import Blueprint, render_template
lab2 = Blueprint('lab2', __name__)


@lab2.route('/lab2/example/')
def example():
    name = 'Кирилл Постников'
    lab_n = '2'
    group = 'ФБИ-14'
    course = '3 курс'
    fruits = [
        {'name': 'яблоки', 'price': 100},
        {'name': 'груши', 'price': 120},
        {'name': 'апельсины', 'price': 80},
        {'name': 'мандарины', 'price': 95},
        {'name': 'манго', 'price': 321}
    ]
    
    books = [
        {'author': 'Пауло Коэльо', 'name': 'Алхимик', 'genre': 'Роман', 'count': '224'},
        {'author': 'Натаниел Поппер', 'name': 'Цифровое золото: невероятная история Биткойна, или как идеалисты и бизнесмены изобретают деньги заново', 'genre': 'Зарубежная деловая литература', 'count': '390'},
        {'author': 'Поварин С. И.', 'name': 'Искусство спора', 'genre': 'Науч.-поп.', 'count': '104'},
        {'author': 'Джордж Оруэлл', 'name': '1984', 'genre': 'Роман-антиутопия', 'count': '288'},
        {'author': 'Дейл Карнеги', 'name': 'Как завоевывать друзей и оказывать влияние на людей', 'genre': 'Психология', 'count': '352'},
        {'author': 'Игорь Рызов', 'name': 'Кремлевская школа переговоров', 'genre': 'Бизнес и менеджмент', 'count': '416'},
        {'author': 'Нассим Николас Талеб', 'name': 'Черный лебедь. Под знаком непредсказуемости', 'genre': 'Зарубежная публицистика', 'count': '736'},
        {'author': 'Нассим Николас Талеб', 'name': 'Антихрупкость', 'genre': 'Зарубежная публицистика', 'count': '391'},
        {'author': 'Даниэль Канеман', 'name': 'Думай медленно… Решай быстро', 'genre': 'Зарубежная психология', 'count': '706'},
        {'author': 'Ронен Бергман', 'name': 'Восстань и убей первым. Тайная история израильских точечных ликвидаций', 'genre': 'Военное дело. Спецслужбы', 'count': '1171'},
    ]
    return render_template('example.html', 
                            name=name, lab_n=lab_n, group=group,
                            course=course, fruits=fruits, books=books)


@lab2.route('/lab2/')
def lab():
    return render_template('lab2.html')


@lab2.route('/lab2/autos')
def autos():
    return render_template('autos.html')