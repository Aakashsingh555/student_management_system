# Student Management System

A web-based **Student Management System** developed using **Python and Django** to manage student information and provide a foundation for academic and administrative management.

The project is being developed collaboratively as part of a Django internship project, with development work organized through Git and GitHub.

## 📌 Project Overview

The Student Management System is designed to centralize student-related information and provide a structured interface for managing academic records.

The current project includes separate Django applications for students, academics, accounts, attendance, fees, notices, payments, and reports. The system is being developed incrementally, with features added and improved throughout the development process.

## 🚀 Current Features

### Student Management

* Add new students
* View student records
* Edit student information
* Delete student records
* Associate students with courses
* Student form validation through Django ModelForms
* Student confirmation before deletion

The current `Student` model contains:

* Name
* Email
* Phone
* Course

Student email addresses are unique, and students are linked to the existing `Course` model through a foreign-key relationship.

### Dashboard

The dashboard currently provides:

* Dashboard overview
* Recent student records
* Student ID
* Student name
* Student course
* Student status display
* Responsive dashboard layout

The recent-student table is connected to database records. Some dashboard statistics are currently placeholders and are planned to become dynamically calculated from the database.

### Academic Management

The `academics` application currently contains models for:

* Courses
* Subjects

The `Course` model includes:

* Course name
* Course code
* Course duration

The `Subject` model includes:

* Course relationship
* Subject name
* Subject code
* Semester
* Credit hours

### Additional Modules

The project structure also includes applications for:

* Accounts
* Attendance
* Fees
* Notices
* Payments
* Reports

These modules provide the foundation for additional Student Management System functionality and will be developed progressively.

## 🛠️ Technologies Used

* **Python**
* **Django**
* **HTML5**
* **Tailwind CSS**
* **JavaScript**
* **SQLite / Django-supported database during development**
* **Git**
* **GitHub**

## 📂 Project Structure

```text
student_management_system/
│
├── academics/
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   ├── admin.py
│   └── ...
│
├── accounts/
│   ├── migrations/
│   ├── views.py
│   ├── admin.py
│   └── ...
│
├── attendance/
│   ├── migrations/
│   └── ...
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── fees/
│   └── ...
│
├── notices/
│   └── ...
│
├── payments/
│   └── ...
│
├── reports/
│   └── ...
│
├── students/
│   ├── migrations/
│   ├── templates/
│   │   └── students/
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── admin.py
│
├── templates/
│   ├── base.html
│   └── dashboard.html
│
├── manage.py
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Aakashsingh555/student_management_system.git
```

Move into the project directory:

```bash
cd student_management_system
```

### 2. Create a virtual environment

On Windows:

```bash
python -m venv venv
```

Activate it using Command Prompt:

```bash
venv\Scripts\activate
```

Or using Git Bash:

```bash
source venv/Scripts/activate
```

### 3. Install Django

If a `requirements.txt` file is available:

```bash
pip install -r requirements.txt
```

Otherwise, install Django directly:

```bash
pip install django
```

### 4. Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a superuser

```bash
python manage.py createsuperuser
```

Follow the prompts to create the administrator account.

### 6. Run the development server

```bash
python manage.py runserver
```

The application will normally be available at:

```text
http://127.0.0.1:8000/
```

## 🔗 Current URL Structure

The project currently routes the root URL to the dashboard and includes the student application under `/students/`.

```text
/                    → Dashboard
/admin/              → Django Admin
/students/           → Student Management
```

Additional application URLs can be added as their respective modules are implemented.

## 👨‍💻 Development Workflow

The project uses Git and GitHub for version control and team collaboration.

### Main Branch

The `main` branch should contain the stable, integrated version of the project.

Team members should avoid directly developing features on `main`.

### Feature Branches

Each developer should create a separate branch for their assigned task.

Example:

```bash
git checkout -b feature/student-search
```

Other examples:

```text
feature/dashboard-dynamic
feature/student-backend
feature/student-ui
feature/authentication
feature/academics
```

### Commit Changes

After completing a meaningful piece of work:

```bash
git add .
git commit -m "Add student search functionality"
```

Push the branch:

```bash
git push -u origin feature/student-search
```

### Pull Requests

After completing the assigned task:

1. Push the feature branch.
2. Open a Pull Request on GitHub.
3. Describe what was changed.
4. Reference the related GitHub Issue.
5. Ask another team member to review the changes.
6. Test the feature.
7. Merge the Pull Request into `main`.
8. Close the related Issue.

## 🎫 GitHub Issue / Ticket System

Starting from Week 3, development tasks will be managed using GitHub Issues.

Each meaningful task should have its own Issue.

Example:

```text
Title:
Make Dashboard Statistics Dynamic

Assignee:
Gaurav

Label:
backend

Branch:
feature/dashboard-dynamic
```

### Project Board

The team will use the following workflow:

```text
TODO
   ↓
IN PROGRESS
   ↓
REVIEW
   ↓
DONE
```

### Ticket Rules

* Create an Issue before starting a task.
* Assign the Issue to one primary team member.
* Use a feature branch for the task.
* Keep commits focused and understandable.
* Open a Pull Request when the work is ready.
* Review and test the changes before merging.
* Move the Issue through the Project Board.
* Do not consider a task complete until it has been reviewed, merged, and tested.
* If multiple members need to modify the same file, communicate first to avoid merge conflicts.
* Do not directly overwrite another member's work.

## 👥 Team Roles

The project is developed collaboratively by the internship team.

### Project Manager / Full Stack

Responsible for:

* Task planning
* GitHub Issues
* GitHub Project Board
* Task assignment
* Dashboard integration
* Pull Request review
* Git conflict coordination
* Overall project coordination

### Backend Developers

Responsible for:

* Django models
* Views
* Forms
* URLs
* Business logic
* Database-related functionality

### Frontend Developer

Responsible for:

* HTML templates
* Tailwind CSS
* User interface
* Form presentation
* Responsive layouts

### QA / Testing

Responsible for:

* Functional testing
* Finding bugs
* Reproducing bugs
* Creating GitHub bug Issues
* Verifying fixes

### Documentation

Responsible for:

* Development documentation
* Progress reports
* Testing documentation
* Screenshots
* Weekly work records

## 🧪 Testing

Testing is performed progressively as features are completed.

Important areas for testing include:

* Student creation
* Student listing
* Student editing
* Student deletion
* Form validation
* Course selection
* Dashboard data
* Authentication
* Academic functionality
* Navigation
* Responsive UI

Bugs should be documented using GitHub Issues with:

1. Problem description
2. Steps to reproduce
3. Expected result
4. Actual result
5. Screenshot, if useful
6. Assigned developer

## 📈 Current Development Status

The project is currently in active development.

### Completed / Existing

* Django project structure
* Multiple Django applications
* Academic Course and Subject models
* Student model
* Student ModelForm
* Student list functionality
* Student creation
* Student update
* Student deletion
* Student deletion confirmation page
* Student-related templates
* Dashboard
* Dynamic recent-student table
* Git/GitHub version control

### Planned / Under Development

* Dynamic dashboard statistics
* Complete authentication flow
* Improved student search
* Expanded academic management
* Attendance functionality
* Fees and payment functionality
* Notices
* Reports
* More comprehensive testing
* UI improvements
* Complete integration of the remaining Django applications

## 📋 Week 3 Development Focus

The main objectives for Week 3 are:

1. Stabilize and test the existing Student CRUD functionality.
2. Make dashboard statistics database-driven.
3. Complete the authentication flow.
4. Improve Student Management UI.
5. Review and extend the Academics module.
6. Perform systematic QA testing.
7. Introduce GitHub Issues and Project Board.
8. Use feature branches and Pull Requests.
9. Maintain project documentation.

## 🤝 Contribution Guidelines

Before starting work:

```bash
git pull origin main
```

Create a feature branch:

```bash
git checkout -b feature/your-feature-name
```

After completing the task:

```bash
git add .
git commit -m "Describe the change"
git push -u origin feature/your-feature-name
```

Then create a Pull Request and wait for review before merging.

## 📌 Team Development Principle

> **One Issue → One owner → One feature branch → Focused commits → Pull Request → Review → Test → Merge → Done**

The team should prioritize communication when working on shared files and should avoid directly modifying the same file independently without coordination.

## 📄 Project Purpose

This project is being developed as a collaborative Django internship project to provide practical experience in:

* Python
* Django
* Web application development
* Database-driven applications
* Git and GitHub
* Team collaboration
* Issue tracking
* Code review
* Software testing
* Project documentation

## 📜 License

This project is currently intended for educational and internship purposes.
