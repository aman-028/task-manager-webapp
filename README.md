# 📝 Task Manager Web App (Django + Bootstrap)

A full-stack **Task Management Web Application** built using Django and Bootstrap.  
Users can **register, log in, and manage their personal tasks** with priority, status, search, filters, and analytics.

---

## 🚀 Features

✔ User registration, login & logout  
✔ User-specific tasks (each user sees only their own tasks)  
✔ Create, edit, and delete tasks  
✔ Task fields:
- Title & description  
- Due date  
- Status (To Do / In Progress / Done)  
- Priority (High / Medium / Low)

✔ **Search** tasks by title/description  
✔ **Filter** tasks by status and priority (filter chips)  
✔ **Statistics dashboard**
- Total tasks (based on filter)
- Completed / In Progress / To Do
- High / Medium / Low priority counts

✔ Modern UI with **Bootstrap 5**  
✔ Fully responsive (desktop & mobile)

---

## 🛠 Tech Stack

| Technology | Purpose |
|----------|---------|
| Python | Programming language |
| Django | Backend web framework |
| SQLite | Database |
| Bootstrap 5 | Frontend styling |
| HTML + CSS | Templates & UI |
| Git + GitHub | Version control & hosting |

---

## 📂 Project Structure

task_manager_django/
├─ manage.py
├─ taskmanager/
│ ├─ settings.py
│ ├─ urls.py
├─ tasks/
│ ├─ models.py
│ ├─ views.py
│ ├─ urls.py
│ ├─ templates/
│ └─ tasks/
│ ├─ base.html
│ ├─ login.html
│ ├─ register.html
│ ├─ task_list.html
│ ├─ task_form.html
│ └─ task_confirm_delete.html
└─ venv/ (ignored)


---

## 📌 How to Run the Project Locally

```bash
# 1. Clone the repository
git clone https://github.com/aman-028/task-manager-webapp.git
cd task-manager-webapp

# 2. Create virtual environment
python -m venv venv

# 3. Activate it
venv\Scripts\activate     # Windows
# source venv/bin/activate # Linux/Mac

# 4. Install dependencies
pip install django

# 5. Apply migrations
python manage.py migrate

# 6. Create superuser (optional, for /admin/)
python manage.py createsuperuser

# 7. Start server
python manage.py runserver


📈 Future Improvements (Planned)

REST API using Django REST Framework (DRF)

Kanban board view (drag & drop tasks)

Email reminders for due tasks

Dark mode UI

Deploy to Render / Railway / DigitalOcean

💡 About the Developer

Author: Aman
🚀 Passionate about full-stack web development and learning by building real projects.