# Django REST Framework — API Practice

A hands-on practice project built with **Django REST Framework (DRF)** to explore core REST API concepts. The project contains three independent mini-apps — **Students**, **Employee**, and **Blogs** — each demonstrating a different level of DRF usage, from function-based views all the way to generic class-based views with filtering and pagination.

---

## What This Project Covers

| Concept | Where Used |
|---|---|
| Function-based API views (`@api_view`) | Students app |
| Class-based `APIView` | Employee app (commented reference) |
| Generic views (`ListCreateAPIView`, `RetrieveUpdateDestroyAPIView`) | Employee & Blogs apps |
| `ModelSerializer` | All apps |
| Nested serializers | Blogs — comments nested inside blog response |
| Custom pagination (`PageNumberPagination`) | Employee app |
| `django-filters` — custom `FilterSet` | Employee app |
| Search and ordering filters | Blogs app |

---

## Apps

### 1. Students
Demonstrates the basics using **function-based views**.

- `GET /api/students/` — list all students
- `POST /api/students/` — create a student
- `GET /api/students/<student_id>/` — retrieve a student
- `PUT /api/students/<student_id>/` — update a student
- `DELETE /api/students/<student_id>/` — delete a student

**Model fields:** `student_id`, `name`, `branch`

---

### 2. Employee
Demonstrates **generic class-based views** with custom filtering and pagination.

- `GET /api/employee/` — list all employees (paginated, filterable)
- `POST /api/employee/` — create an employee
- `GET /api/employee/<emp_id>/` — retrieve an employee
- `PUT /api/employee/<emp_id>/` — update an employee
- `DELETE /api/employee/<emp_id>/` — delete an employee

**Model fields:** `emp_id`, `position`, `salary`

**Filtering options (via django-filters):**

| Query Param | Description |
|---|---|
| `po` | Filter by position (case-insensitive contains) |
| `salary` | Filter by salary range |
| `id_min` | Minimum employee ID |
| `id_max` | Maximum employee ID |

**Pagination:** Page-number based — `?page_number=1&page_size=10` (max 100 per page)

> The `APIView` class-based implementation is also preserved in the views file (commented out) as a learning reference.

---

### 3. Blogs
Demonstrates **nested serializers**, **search**, and **ordering** filters.

- `GET /blogs/` — list all blogs (with nested comments, searchable, orderable)
- `POST /blogs/` — create a blog
- `GET /blogs/<id>/` — retrieve a blog
- `PUT /blogs/<id>/` — update a blog
- `DELETE /blogs/<id>/` — delete a blog
- `GET /comments/` — list all comments
- `POST /comments/` — create a comment
- `GET /comments/<id>/` — retrieve, update, or delete a comment

**Model fields:**
- Blog: `title`, `content`, `created_at`
- Comment: `blog` (FK), `text`, `created_at`

**Search:** `?search=keyword` — searches across `title` and `content`

**Ordering:** `?ordering=title` or `?ordering=-created_at`

Each blog response includes its related comments as a **nested array** via `CommentSerializer`.

---

## Project Structure

```
Api-Practice/
└── rest_main/
    ├── api/              # Shared views wiring students + employee endpoints
    │   ├── views.py
    │   ├── serializers.py
    │   ├── paginators.py
    │   └── urls.py
    ├── blogs/            # Blog + Comment models, nested serializers
    ├── students/         # Student model
    ├── employee/         # Employee model + custom FilterSet
    ├── rest_main/        # Project settings and root URLs
    └── manage.py
```

---

## Tech Stack

| Layer | Technology |
|---|---|
| Framework | Django 6, Django REST Framework |
| Filtering | django-filter |
| Database | SQLite |
| Language | Python 3 |

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/shadows12-star/Api-Practice.git
cd Api-Practice/rest_main
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install django djangorestframework django-filter
```

### 4. Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run the server

```bash
python manage.py runserver
```

---

## API Endpoints Summary

| Method | Endpoint | Description |
|---|---|---|
| GET / POST | `/api/students/` | List / create students |
| GET / PUT / DELETE | `/api/students/<id>/` | Student detail |
| GET / POST | `/api/employee/` | List / create employees |
| GET / PUT / DELETE | `/api/employee/<id>/` | Employee detail |
| GET / POST | `/blogs/` | List / create blogs |
| GET / PUT / DELETE | `/blogs/<id>/` | Blog detail |
| GET / POST | `/comments/` | List / create comments |
| GET / PUT / DELETE | `/comments/<id>/` | Comment detail |

---

## Learning Notes

This project intentionally explores multiple approaches to the same problem:

- **Students** uses `@api_view` — great for understanding the raw request/response cycle
- **Employee** uses generic views — less boilerplate, more DRF conventions
- The commented `APIView` code in `api/views.py` is kept as a reference showing the step between the two styles

---

## License

This project is open source for learning purposes. MIT License recommended.
