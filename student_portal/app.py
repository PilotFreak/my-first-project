from flask import Flask
from flask import render_template
from flask import request
from models import Student
from models import Course

name = "main"


app = Flask(name)

students={}

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/add_student')
def add_student():
  return render_template('add_student.html')
@app.route('/add_student', methods=['POST'])
def submit():
  student=students.get(request.form['name'])
  if student==None:
    student=Student()
    student.name = request.form['name']
    student.age = request.form['age']

  student.add_grade(request.form['course'],request.form['grade'])
  students[student.name]=student


  return  index()


@app.route('/view_grades')
def view_grades():
  return render_template('grades.html',students=students)



if name == 'main':
  app.run(debug=True)