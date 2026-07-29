from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from models import db, User, Task

app = Flask(__name__)

# Configuration
app.config["SECRET_KEY"] = "student_task_manager_secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize Database
db.init_app(app)

# Login Manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# ---------------- HOME ---------------- #

@app.route("/")
def home():
    return render_template("index.html")


# ---------------- REGISTER ---------------- #

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        existing_user = User.query.filter_by(email=email).first()

        if existing_user:
            flash("Email already exists.", "danger")
            return redirect(url_for("register"))

        hashed_password = generate_password_hash(password)

        new_user = User(
            username=username,
            email=email,
            password=hashed_password
        )

        db.session.add(new_user)
        db.session.commit()

        flash("Registration Successful!", "success")

        return redirect(url_for("login"))

    return render_template("register.html")


# ---------------- LOGIN ---------------- #

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):

            login_user(user)

            flash("Login Successful!", "success")

            return redirect(url_for("dashboard"))

        flash("Invalid Email or Password", "danger")

    return render_template("login.html")


# ---------------- LOGOUT ---------------- #

@app.route("/logout")
@login_required
def logout():

    logout_user()

    flash("Logged out successfully.", "info")

    return redirect(url_for("home"))


# ---------------- DASHBOARD ---------------- #

@app.route("/dashboard")
@login_required
def dashboard():

    tasks = Task.query.filter_by(user_id=current_user.id).all()

    total_tasks = len(tasks)

    completed_tasks = Task.query.filter_by(
        user_id=current_user.id,
        status="Completed"
    ).count()

    pending_tasks = Task.query.filter_by(
        user_id=current_user.id,
        status="Pending"
    ).count()

    return render_template(
        "dashboard.html",
        tasks=tasks,
        total_tasks=total_tasks,
        completed_tasks=completed_tasks,
        pending_tasks=pending_tasks
    )


# ---------------- ADD TASK ---------------- #

@app.route("/add-task", methods=["GET", "POST"])
@login_required
def add_task():

    if request.method == "POST":

        title = request.form.get("title")
        category = request.form.get("category")
        priority = request.form.get("priority")
        due_date = request.form.get("due_date")

        task = Task(
            title=title,
            category=category,
            priority=priority,
            due_date=due_date,
            status="Pending",
            user_id=current_user.id
        )

        db.session.add(task)
        db.session.commit()

        flash("Task Added Successfully!", "success")

        return redirect(url_for("dashboard"))

    return render_template("add_task.html")
# ---------------- EDIT TASK ---------------- #

@app.route("/edit/<int:id>", methods=["GET", "POST"])
@login_required
def edit_task(id):

    task = Task.query.get_or_404(id)

    # Make sure users can only edit their own tasks
    if task.user_id != current_user.id:
        flash("You are not authorized to edit this task.", "danger")
        return redirect(url_for("dashboard"))

    if request.method == "POST":

        task.title = request.form.get("title")
        task.category = request.form.get("category")
        task.priority = request.form.get("priority")
        task.due_date = request.form.get("due_date")

        db.session.commit()

        flash("Task Updated Successfully!", "success")

        return redirect(url_for("dashboard"))

    return render_template("edit_task.html", task=task)


# ---------------- COMPLETE TASK ---------------- #

@app.route("/complete/<int:id>")
@login_required
def complete_task(id):

    task = Task.query.get_or_404(id)

    task.status = "Completed"

    db.session.commit()

    flash("Task Completed!", "success")

    return redirect(url_for("dashboard"))


# ---------------- DELETE TASK ---------------- #

@app.route("/delete/<int:id>")
@login_required
def delete_task(id):

    task = Task.query.get_or_404(id)

    db.session.delete(task)

    db.session.commit()

    flash("Task Deleted!", "danger")

    return redirect(url_for("dashboard"))


# ---------------- PROFILE ---------------- #

@app.route("/profile")
@login_required
def profile():

    total_tasks = Task.query.filter_by(
        user_id=current_user.id
    ).count()

    completed_tasks = Task.query.filter_by(
        user_id=current_user.id,
        status="Completed"
    ).count()

    pending_tasks = Task.query.filter_by(
        user_id=current_user.id,
        status="Pending"
    ).count()

    return render_template(
        "profile.html",
        total_tasks=total_tasks,
        completed_tasks=completed_tasks,
        pending_tasks=pending_tasks
    )

# ---------------- MAIN ---------------- #

if __name__ == "__main__":

    with app.app_context():
        db.create_all()

    app.run(debug=True)