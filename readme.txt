# FastAPI CRUD Application

This is a simple CRUD (Create, Read, Update, Delete) API built using **FastAPI**, **Pydantic**, and run with **Uvicorn**. It serves as a foundational template for building RESTful services with Python.

## 🚀 Features

- Create, Read, Update, Delete operations
- Data validation using Pydantic models
- Fast and lightweight server with Uvicorn
- Organized and clean project structure

---

## 🛠 Tech Stack

- **FastAPI** – for building the API
- **Pydantic** – for data validation
- **Uvicorn** – ASGI server to run the FastAPI app

---

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/fastapi-crud-app.git
   cd fastapi-crud-app


Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


pip install -r requirements.txt


uvicorn main:app --reload

