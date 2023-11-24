from flask import Flask

from UserDAO import UserDAO

app = Flask(__name__)


@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/users")
def show_users():
    dao = UserDAO('deb.db')
    users = dao.find_all()

    html = ''
    for user in users:
        html += f'''
       <tr>
            <td>{user.id}</td>
            <td>{user.first_name}</td>
            <td>{user.last_name}</td>
            <td>{user.email}</td>
        </tr>
'''

    return f"<table>{html}</table>"
