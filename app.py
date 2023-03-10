# #Module, #Component
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# /// = relative path, //// = absolute path
# #Database (distinctive Jacksonian Concept 2)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# #Database
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)

# #responseMethod (distinctive Jacksonian concept 3), #Routing
@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")
    new_todo = Todo(title=title, complete=False)
    # #Sessions (distinctive Jacksonian Concept 1)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("home"))

# #responseMethod, #Routing
@app.route("/update/<int:todo_id>")
def update(todo_id):
    # #Property
    todo = Todo.query.filter_by(id=todo_id).first()
    # #Property
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("home"))

# #responseMethod, #Routing
@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    # #Property (shared Jacksonian concept 3)
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("home"))

# #responseMethod, #Routing
@app.route('/')
def home():
    todo_list = Todo.query.all()
    # #Component
    return render_template("base.html", todo_list=todo_list)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True)