# Production-Ready Django Photo Album Management System

A robust, production-ready photo album management application built with Django, featuring Role-Based Access Control (RBAC), Cloudinary media integration, and a PostgreSQL database.

## 🚀 Live Application
**Live URL:** [https://assignment-no-6.onrender.com](https://assignment-no-6.onrender.com)

## 📋 Features & Architecture

This project strictly adheres to industry-standard architectural guidelines:

* **Class-Based Views (CBVs):** Core CRUD (Create, Read, Update, Delete) operations are handled efficiently using Django's built-in `ListView`, `CreateView`, `UpdateView`, and `DeleteView`.
* **Role-Based Access Control (RBAC):** Integrated with Django's native authentication system. Actions such as uploading, editing, and deleting photos are restricted using `PermissionRequiredMixin`, ensuring only authorized administrators can modify content.
* **Cloud Storage Integration:** Local media storage is completely disabled in the production environment. All image uploads, storage, and delivery are seamlessly handled via the **Cloudinary API** using `django-cloudinary-storage`.
* **Production Deployment:** Deployed to a live **Render** web service connected to a managed **PostgreSQL** database. 
* **Secure Configuration:** Zero sensitive data (Secret Keys, Database URLs, Cloudinary Credentials) is hardcoded into the repository. All secrets are managed securely via Environment Variables (`.env` for local development, Render Environment Settings for production).

## 🛠️ Technology Stack
* **Backend Framework:** Django 6.x (Python 3)
* **Database:** PostgreSQL (Production) / SQLite (Local)
* **Media Management:** Cloudinary API
* **Static File Serving:** WhiteNoise
* **Production Server:** Gunicorn

## 💻 Local Development Setup

To run this project locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/GitSys101/Assignment-No.-6.git
   cd Assignment-No.-6
   ```

2. **Create a virtual environment and install dependencies:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables:**
   Create a `.env` file in the project root and add your configuration:
   ```env
   SECRET_KEY=your_secret_key
   DEBUG=True
   CLOUD_NAME=your_cloudinary_cloud_name
   API_KEY=your_cloudinary_api_key
   API_SECRET=your_cloudinary_api_secret
   ```

4. **Apply Migrations and Run Server:**
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   python manage.py runserver
   ```
