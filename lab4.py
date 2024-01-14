from flask import Blueprint, render_template, request
lab4 = Blueprint('lab4', __name__)


@lab4.route('/lab4/')
def lab():
    return render_template('lab4.html')


@lab4.route('/lab4/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    
    username = request.form.get('username')
    password = request.form.get('password')
    if username == 'Kirill' and password == '123':
        return render_template('sucess1.html', username=username)
    elif username == '' and password == '':
        error = 'Заполните оба поля'
        return render_template('login.html', error=error, username=username, password=password)
    elif username == '':
        error1 = 'Введите логин'
        return render_template('login.html', error1=error1, username=username, password=password)
    elif password == '':
        error2 = 'Введите пароль'
        return render_template('login.html', error2=error2, username=username, password=password)
    else:
        error = 'Неверный логин и/или пароль'
    return render_template('login.html', error=error, username=username, password=password)


@lab4.route('/lab4/fridge', methods = ['GET', 'POST'])
def fridge():
    temp = request.form.get('temp')
    
    if request.method == 'GET':
        return render_template('fridge.html')
    
    if temp == '':
        error = 'Введите значение'
        return render_template('fridge.html', temp=temp, error=error)
    
    elif float(temp) < -12:
        error = 'Не удалось установить температуру - слишком низкое значение'
        return render_template('fridge.html', temp=temp, error=error)
    
    elif float(temp) > -1:
        error = 'Не удалось установить температуру - слишком высокое значение'
        return render_template('fridge.html', temp=temp, error=error)

    elif -12 <= float(temp) <= -9:
        foot = temp +'°C'
        src3 = 'snow.png'
        return render_template('fridge_temp.html', temp=temp, foot=foot, src3=src3)
    
    elif -8 <= float(temp) <= -5:
        foot = temp +'°C'
        src2 = 'snow.png'
        return render_template('fridge_temp.html', temp=temp, foot=foot, src2=src2)
    
    elif -4 <= float(temp) <= -1:
        foot = temp +'°C'
        src = 'snow.png'
        return render_template('fridge_temp.html', temp=temp, foot=foot, src=src)


@lab4.route('/lab4/zerno/', methods = ['GET', 'POST'])
def zerno():
    error = None
    grain = None
    weight = None
    skidka = ''
    price = 0
    if request.method == 'POST':
        grain = request.form.get('grain')
        weight = request.form.get('weight')

        if weight is None or weight == '':
            error = 'Не введен вес'
        else:
            weight = float(weight)

            if weight <= 0:
                error = 'Неверное значение веса'
            elif weight > 500:
                error = 'Такого объема сейчас нет в наличии'
            else: 
                if grain == 'yachmen':
                    price = 12000*weight
                elif grain == 'oves':
                    price = 8500*weight
                elif grain == 'pshenitsa':
                    price = 8700*weight
                else:
                    price = 14000*weight
                
                if weight > 50 and weight <= 500:
                        price = price*0.9
                        skidka  = 'Применена скидка за большой объём'

    return render_template('zerno.html', error=error, grain=grain, weight=weight, price=price, skidka=skidka)


@lab4.route('/lab4/cookies', methods = ['GET', 'POST'])
def cookies():
    if request.method == 'GET':
        return render_template('cookies.html')
    
    color = request.form.get('color')
    headers = {
        'Set-cookie': 'color=' + color + '; path=/',
        'Location': '/lab4/cookies'
    }
    return '', 303, headers