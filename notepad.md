# Python perf 21/11

https://notepad.re/pythonperf

Frédéric GAURAT

https://github.com/fgaurat/pythonperf_20112023

	"Python main function": {
		"prefix": "pymain",
		"body": [
			// "#!/usr/bin/env python",
			// "",
			// "import os",
			// "import sys",
			// "from pprint import pprint",
			"if __name__=='__main__':",
			"\tmain()",
			"",
		],
		"description": "Log output to console"
	}

			// "",
			"def main():",
			"\tpass$1",
			"",

https://docs.python.org/3/tutorial/index.html
https://docs.python.org/3/tutorial/introduction.html#lists

https://wiki.python.org/moin/TimeComplexity

https://peps.python.org/pep-0008/

https://fr.wikipedia.org/wiki/Zen_de_Python

https://docs.python.org/3/library/functions.html

https://en.wikipedia.org/wiki/Design_Patterns (Gang of Four book)

https://stackoverflow.com/questions/62019960/difference-between-pass-statement-and-3-dots-in-python
https://stackoverflow.com/questions/55274977/when-is-the-usage-of-the-python-ellipsis-to-be-preferred-over-pass

https://www.cts-strasbourg.eu/export/sites/default/Parameters/Spring-par-la-pratique-Ed2.pdf

https://docs.python.org/3/library/abc.html

https://www.stashofcode.fr/comment-marche-fonction-super-de-python/

https://sqlitebrowser.org/

https://docs.python.org/3/library/csv.html
https://docs.python.org/3/library/csv.html#csv.DictReader

https://docs.python.org/3/library/sqlite3.html

https://www.oracle.com/java/technologies/design-patterns-catalog.html

https://docs.python.org/3/library/contextlib.html#contextlib.ContextDecorator

https://www.toptal.com/developers/gitignore/

```bash
pip install beautifulsoup4 requests
```

https://logs.eolem.com/

https://fr.python-requests.org/en/latest/

powershell -ep bypass

PS> Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope LocalMachine

```bash
set-executionpolicy remotesigned
```

https://www.crummy.com/software/BeautifulSoup/bs4/doc/#quick-start

https://www.crummy.com/software/BeautifulSoup/bs4/doc/#navigating-the-tree

https://docs.python.org/3/library/multiprocessing.html

https://docs.python.org/fr/3/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor

http://latentflip.com/loupe/?code=JC5vbignYnV0dG9uJywgJ2NsaWNrJywgZnVuY3Rpb24gb25DbGljaygpIHsKICAgIHNldFRpbWVvdXQoZnVuY3Rpb24gdGltZXIoKSB7CiAgICAgICAgY29uc29sZS5sb2coJ1lvdSBjbGlja2VkIHRoZSBidXR0b24hJyk7ICAgIAogICAgfSwgMjAwMCk7Cn0pOwoKY29uc29sZS5sb2coIkhpISIpOwoKc2V0VGltZW91dChmdW5jdGlvbiB0aW1lb3V0KCkgewogICAgY29uc29sZS5sb2coIkNsaWNrIHRoZSBidXR0b24hIik7Cn0sIDUwMDApOwoKY29uc29sZS5sb2coIldlbGNvbWUgdG8gbG91cGUuIik7!!!PGJ1dHRvbj5DbGljayBtZSE8L2J1dHRvbj4%3D

https://docs.python.org/fr/3/library/asyncio.html#module-asyncio

https://www.python-httpx.org/async/

https://docs.celeryq.dev/en/stable/getting-started/introduction.html#celery-is

```bash
celery -A celery_task worker --loglevel=info -P solo
```

https://flask.palletsprojects.com/en/3.0.x/

https://flask.palletsprojects.com/en/3.0.x/quickstart/#a-minimal-application

https://www.jetbrains.com/help/pycharm/settings-emmet.html

```html
@app.route("/users")
def show_users():
html=""
dao = UserDAO('formation.db')

users = dao.findAll()
for user in users:
html+=f"""
<tr>
    <td>{user.id}</td>
    <td>{user.first_name}</td>
    <td>{user.last_name}</td>
    <td>{user.email}</td>
</tr>
"""

return f"
<table>{html}</table>"
```

---

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Users</title>
</head>
<body>

<table>
    <thead>
    <tr>
        <td>#</td>
        <td>first_name</td>
        <td>last_name</td>
        <td>email</td>
    </tr>
    </thead>
    <tbody>

    {%for user in users%}
    <tr>
        <td>{{user.id}}</td>
        <td>{{user.first_name}}</td>
        <td>{{user.last_name}}</td>
        <td>{{user.email}}</td>
    </tr>
    {%endfor%}

    </tbody>
</table>

</body>
</html>
```

---

https://getbootstrap.com/



---

```python
@app.route("/users")
def show_users():
    html = ""
    dao = UserDAO('formation.db')
    users = dao.findAll()

    # from flask import Flask,render_template
    return render_template("users_list.html", users=users)
```

    
---

https://docs.streamlit.io/library/get-started

https://docs.streamlit.io/library/api-reference/widgets/st.text_input

https://docs.streamlit.io/library/api-reference/widgets/st.button

st.set_page_config(layout="wide")

https://www.gradio.app/

https://notepad.re/treeview

https://github.com/hoffstadt/DearPyGui



---

```python
from main_window import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)


def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()


```

```bash
pyside6-uic.exe main.ui -o main_qt.py
```

---

https://numpy.org/doc/stable/user/absolute_beginners.html#how-to-create-a-basic-array

https://pandas.pydata.org/docs/user_guide/10min.html

https://www.youtube.com/@MachineLearnia

https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html

https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html

---

```python
def has_survived(model, pclass=3, sex=0, age=47):
    x = np.array([pclass, sex, age]).reshape(1, 3)
    print(np.array([pclass, sex, age]))
    print(x)
    return model.predict(x)


p = has_survived(model, pclass=1, sex=0, age=25)
```


