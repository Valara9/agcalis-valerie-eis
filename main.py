from flask import Flask, render_template, request, redirect
from users import Users
from employees import Employees

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check-user', methods=['POST'])
def check_user():
    username = request.form["username"]
    password = request.form["password"]

    result = Users.check_user(username, password)

    if result:
        return redirect('/employee-list')
    else:
        return render_template("index.html")


@app.route('/employee-list')
def employee_list():
    employees = Employees.get_all()
    return render_template('employee.html' , employees=employees)
    
if __name__ == '__main__':
    app.run()