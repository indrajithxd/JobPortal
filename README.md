# Job Portal API

A Job Portal REST API built using **Python, Django and Django REST Framework (DRF)**.

The application allows users to manage job postings and submit applications for available opportunities.

## 🚀 Technologies Used

- Python
- Django
- Django REST Framework
- SQLite
- REST API
- VS Code REST Client

## ✨ Features

### Job Management
- Create new job postings.
- Retrieve all available jobs.
- Retrieve individual job details.
- Update existing job postings.
- Delete job postings.

### Application Management
- Submit applications for job postings.
- Validate whether the requested job exists.
- Store candidate details and cover letters.
- Manage application status and recruiter remarks.
- Retrieve submitted applications.

## 📁 Project Structure

```text
JobPortal/
│
├── jobportal/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── jobs/
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
│
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone <your-repository-url>
```

### 2. Navigate to the project directory

```bash
cd JobPortal
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

Windows:

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Apply database migrations

```bash
python manage.py migrate
```

### 7. Run the development server

```bash
python manage.py runserver
```

The API will be available at:

`http://127.0.0.1:8000/`

## 🔗 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/jobs/` | Retrieve all jobs |
| POST | `/jobs/` | Create a job |
| GET | `/jobs/<id>/` | Retrieve a job |
| PUT | `/jobs/<id>/` | Update a job |
| DELETE | `/jobs/<id>/` | Delete a job |
| GET | `/applications/` | Retrieve applications |
| POST | `/applications/` | Submit an application |

## 🧪 API Testing

APIs are tested using the VS Code REST Client extension.

## 📚 Learning Objectives

- Understanding Django REST Framework.
- Implementing APIView-based views.
- Working with Django ORM.
- Creating and validating serializers.
- Understanding ForeignKey relationships.
- Implementing CRUD operations.
- Handling API requests and responses.

## 🔮 Future Enhancements

- User registration and authentication.
- Recruiter and candidate roles.
- Resume upload functionality.
- Candidate application tracking.
- Recruiter dashboard.
- Application status management.
- Custom permissions and authorization.

---

**Developed as a Django REST Framework learning project.**