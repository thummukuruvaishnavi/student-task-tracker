# 🎓 Student Task Manager

A simple Student Task Manager built using Flask and SQLite.

## Features

- Add Tasks
- Edit Tasks
- Delete Tasks
- Mark Task as Completed
- Store tasks in SQLite Database
- Clean and Responsive UI

---

## Technologies Used

- Python
- Flask
- SQLite
- HTML
- CSS

---

## Installation

### Step 1

Clone or Download the project.

### Step 2

Create Virtual Environment

Windows

```bash
python -m venv venv
```

Activate Environment

```bash
venv\Scripts\activate
```

---

### Step 3

Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Step 4

Run the Project

```bash
python app.py
```

---

### Step 5

Open Browser

```
http://127.0.0.1:5000
```

---

## Folder Structure

```
Student_Task_Manager
│
├── app.py
├── requirements.txt
├── README.md
├── database.db
│
├── templates
│   ├── index.html
│   ├── add.html
│   └── edit.html
│
└── static
    └── style.css
```

---

## Database

SQLite

Table Name

```
Task
```

Fields

| Field | Type |
|--------|------|
| id | Integer |
| title | String |
| description | Text |
| due_date | String |
| status | String |

---

## Project Screens

- Home Page
- Add Task
- Edit Task
- Completed Tasks

---

## Future Improvements

- Login System
- User Authentication
- Task Categories
- Priority Levels
- Notifications
- Dark Mode
- Search Tasks
- Calendar View
- Email Reminders

---

## Author

Vaishnavi

B.Tech Computer Science Engineering

Student Task Manager using Flask & SQLite
