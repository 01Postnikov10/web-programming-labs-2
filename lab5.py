from werkzeug.security import check_password_hash, generate_password_hash
from flask import Blueprint, render_template, request, redirect, session
import psycopg2


lab5 = Blueprint('lab5', __name__)


def dbConnect():
    conn = psycopg2.connect(
        host='127.0.0.1',
        database='knowledge_base_for_kirill',
        user='kirill_knowledge_base',
        password='24215',
        port='5432')

    return conn

def dbClose(cursor, connection):
    cursor.close()
    connection.close()


@lab5.route('/lab5/')
def main():
    visibleUser = 'Аноним'
    if 'visibleUser' in session:
        visibleUser = session['visibleUser']
    return render_template('lab5_main.html', username=visibleUser)


@lab5.route('/lab5/users')
def users():
    conn = dbConnect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM users;")

    result = cur.fetchall()

    print(result)

    dbClose(conn, cur)

    return render_template('lab5_users.html', users=result)


@lab5.route('/lab5/register', methods=['GET', 'POST'])
def register():
    errors=[]

    if request.method == 'GET': 
        return render_template('lab5_register.html', errors=errors)
    
    username = request.form.get('username')
    password = request.form.get('password')

    if not (username or password):
        errors.append('Пожалуйста, заполните все поля')
        print(errors)
        return render_template('lab5_register.html', errors=errors)
    
    hashPassword = generate_password_hash(password)
    
    conn = dbConnect()
    cur = conn.cursor()

    cur.execute(f"SELECT username FROM users WHERE username = '{ username}';")

    if cur.fetchone() is not None:
        errors.append('Пользователь с данным именем уже существует')
        conn.close()
        cur.close()
        return render_template('lab5_register.html', errors=errors)

    cur.execute(f"INSERT INTO users (username, password) VALUES ('{username}', '{hashPassword}');")

    conn.commit()
    conn.close()
    cur.close()

    return redirect('/lab5/login')


@lab5.route('/lab5/login', methods=['GET', 'POST'])
def loginPage():
    errors = []
    if request.method == "GET":
        return render_template("lab5_login.html", errors = errors)


    username = request.form.get("username")
    password = request.form.get("password")


    if not (username or password):
        errors.append('Пожалуйста, заполните все поля')
        return render_template('lab5_login.html', errors=errors)


    conn = dbConnect()
    cur = conn.cursor()

    cur.execute(f"SELECT id,password FROM users WHERE username = '{ username}';")

    result = cur.fetchone()
    print(result)

    if result is None:
        errors.append('Неправильный логин или пароль')
        dbClose(cur, conn)
        return render_template("lab5_login.html", errors = errors)

    userID, hashPassword = result

    if check_password_hash(hashPassword, password):
        session['id'] = userID
        session['username'] = username
        session['visibleUser'] = username
        dbClose(cur,conn)
        return redirect("/lab5")
    else:
        errors.append("Неправильный логин или пароль")
        return render_template("lab5_login.html", errors=errors)


@lab5.route('/lab5/new_article', methods=['GET', 'POST'])
def createArticle():
    errors=[]

    userID = session.get('id')

    if userID is not None:
        if request.method == 'GET':
            return render_template('lab5_new_article.html')
        if request.method == 'POST':
            text_article = request.form.get('text_article')
            title = request.form.get('title_article')

            if len(text_article) == 0:
                errors.append('Заполните текст')
                return render_template('lab5_new_article.html', errors = errors)
            conn = dbConnect()
            cur = conn.cursor()

            cur.execute(f"INSERT INTO articles(user_id, title, article_text) VALUES ({userID}, '{title}', '{text_article}') RETURNING id")
            new_article_id = cur.fetchone()[0]
            conn.commit()


            dbClose(cur,conn)
            return redirect(f"/lab5/articles/{new_article_id}")
    return redirect("/lab5/login")


@lab5.route("/lab5/articles/<string:article_id>")
def getArticle(article_id):
    userID = session.get("id")

    if userID is not None:
        conn = dbConnect()
        cur = conn.cursor()

        cur.execute("SELECT title, article_text FROM articles WHERE id = %s and user_id = %s", (article_id, userID))

        articleBody = cur.fetchone()

        dbClose(cur, conn)

        if articleBody is None:
            return "Not found!"
        
        text = articleBody[1].splitlines()

        return render_template("lab5_articleN.html", article_text=text,
        article_title=articleBody[0], username=session.get("username"))
    

@lab5.route('/lab5/article_list')

def checkArticle():

    userID = session.get('id')

    if userID is not None:
        conn = dbConnect()
        cur = conn.cursor()

        cur.execute(f"SELECT title, article_text FROM articles WHERE user_id = {userID}")
        lists = cur.fetchall()


        return render_template('lab5_article_user_list.html', lists = lists)
    return redirect("/lab5/login")


@lab5.route('/lab5/logout', methods=['GET', 'POST'])
def deleteCode():
    session.clear()
    return redirect("/lab5/login")