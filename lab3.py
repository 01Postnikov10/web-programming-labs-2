from flask import Blueprint, render_template, request
lab3 = Blueprint('lab3', __name__)

@lab3.route('/lab3/')
def lab():
    return render_template('lab3.html')


@lab3.route('/lab3/form1/')
def form1():
    errors = {}
    user = request.args.get('user')
    if user == '':
        errors['user'] = 'Заполните поле!'

    age = request.args.get('age')
    if age == '':
        errors['age'] = 'Заполните поле!'
        
    sex = request.args.get('sex')
    return render_template('form1.html', user=user, age=age, sex=sex, errors=errors)


@lab3.route('/lab3/order/')
def order():
    return render_template('order.html')


@lab3.route('/lab3/pay/')
def pay():
    price = 0
    drink = request.args.get('drink')
    if drink == 'cofee':
        price = 120
    elif drink == 'black-tea':
        price = 80
    else:
        price = 70

    if request.args.get('milk') == 'on':
        price += 30
    if request.args.get('sugar') == 'on':
        price += 10
    return render_template('pay.html', price=price)


@lab3.route('/lab3/succes/')
def succes():
    return render_template('succes.html')


@lab3.route('/lab3/booking/')
def booking():
    errors = {}
    bags = {}
    user = request.args.get('user')
    if user == '':
        errors['user'] = '*'

    age = request.args.get('age')
    if age == '':
        errors['age'] = '*'

    if request.args.get('bag') == 'on':
        bags['bag'] = 'Проезд с багажом'
    else:
        bags['bag'] = 'Проезд без багажа'

    tarif = request.args.get('tarif')
        
    point_a = request.args.get('point_a')
    if point_a == '':
        errors['point_a'] = '*'
    
    point_b = request.args.get('point_b')
    if point_b == '':
        errors['point_b'] = '*'

    date = request.args.get('date')
    if date == '':
        errors['date'] = '*'

    position = request.args.get('position')
    return render_template('booking.html', 
                           errors=errors, user=user, age=age, tarif=tarif, point_a=point_a, 
                           point_b=point_b, date=date, position=position, bags=bags)
