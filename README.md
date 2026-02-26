# 🛡 API Guard – Intelligent Authentication System (FastAPI)

A production-style authentication backend built using **FastAPI**, **JWT**, and **SQLAlchemy**.

This project simulates the foundation of a corporate-grade API protection system that can later be extended with:

* API Key Management
* Rate Limiting
* Abuse Detection
* Role-Based Access Control
* Analytics & Monitoring

---

## 🚀 Features

* 🔐 User Registration
* 🔑 Secure Login with JWT Authentication
* 🔒 Protected Routes
* 🗄 SQLite Database with SQLAlchemy ORM
* 🔑 Password Hashing using bcrypt
* 🧠 Dependency Injection (FastAPI pattern)
* 📦 Modular Project Structure

---

## 🛠 Tech Stack

* **FastAPI**
* **SQLAlchemy**
* **SQLite**
* **Passlib (bcrypt)**
* **python-jose (JWT)**
* **Uvicorn**

---

## 📂 Project Structure

```
api_guard/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── auth.py
│   └── routes/
│        └── users.py
│
├── api_guard.db
└── requirements.txt
```

---

## ▶️ Run Locally

### 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/api_guard.git
cd api_guard
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run Server

```bash
uvicorn app.main:app --reload
```

### 4️⃣ Open API Docs

```
http://127.0.0.1:8000/docs
```

---

## 🔐 Authentication Flow

1. Register a new user
2. Login to receive JWT token
3. Use the token in the Authorize button
4. Access protected route `/me`

---

## 🧠 Learning Objectives

This project demonstrates:

* JWT-based authentication
* Secure password hashing
* Database session management
* Dependency injection
* Clean backend architecture
* REST API design

---

## 🔮 Future Enhancements

* API Key generation system
* Rate limiting middleware
* Abuse detection logic
* PostgreSQL migration
* Redis integration
* Admin analytics dashboard

---

## 📜 License

This project is built for educational and portfolio purposes.
