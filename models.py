from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

# Initialize SQLAlchemy
db = SQLAlchemy()


# ---------------- USER TABLE ---------------- #

class User(UserMixin, db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(100), nullable=False)

    email = db.Column(db.String(120), unique=True, nullable=False)

    password = db.Column(db.String(255), nullable=False)

    # Relationship with Task table
    tasks = db.relationship(
        "Task",
        backref="user",
        lazy=True,
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<User {self.username}>"


# ---------------- TASK TABLE ---------------- #

class Task(db.Model):

    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(200), nullable=False)

    category = db.Column(db.String(100), nullable=False)

    priority = db.Column(db.String(20), nullable=False)

    due_date = db.Column(db.String(30), nullable=False)

    status = db.Column(
        db.String(20),
        nullable=False,
        default="Pending"
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    def __repr__(self):
        return f"<Task {self.title}>"