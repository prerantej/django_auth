# Django Authentication Project

## Project Overview

This project is a Django-based web application that provides user authentication functionalities including login, logout, registration, and password reset. The application is built with a clear and structured approach, ensuring ease of use and maintainability.

## Libraries and Modules Used

### 1. Django
- **Django Framework**: The primary framework used to develop this application, which provides the necessary tools and libraries for web development.
- **django.contrib.admin**: Enables the admin interface for managing the app.
- **django.contrib.auth**: Provides the authentication framework, including views and models for user login, logout, and password management.
- **django.contrib.contenttypes**: Required by the Django permissions framework.
- **django.contrib.sessions**: Manages sessions across requests.
- **django.contrib.messages**: Enables message framework for one-time notifications.
- **django.contrib.staticfiles**: Manages static files (CSS, JavaScript, images).

### 2. Email Handling
- **SMTP Service**: An SMTP service like SendGrid is used for sending password reset emails. SMTP settings are configured in the Django settings file.

### 3. Environment Variables (Optional)
- **python-decouple**: Used for managing environment variables. (Optional if not using a `.env` file)

## Functionality and Features

### 1. User Authentication
- **Login**: Users can log in using their username/email and password.
  - **View**: `app/views.py` - `login_view`
  - **Template**: `app/templates/app/login.html`
  - **URL**: `/login/`

- **Logout**: Users can log out from their session.
  - **View**: `app/views.py` - `logout_view`
  - **URL**: `/logout/`

### 2. User Registration
- **Signup**: New users can register by providing necessary details like username, email, and password.
  - **View**: `app/views.py` - `signup_view`
  - **Template**: `app/templates/app/signup.html`
  - **URL**: `/signup/`

### 3. Password Management
- **Forgot Password**: Users can request a password reset link sent to their email.
  - **View**: `app/views.py` - `forgot_password_view`
  - **Template**: `app/templates/app/forgot_password.html`
  - **URL**: `/forgot-password/`

- **Reset Password**: Users can reset their password using the link sent to their email.
  - **View**: `app/views.py` - `reset_password_view`
  - **Template**: `app/templates/app/reset_password.html`
  - **URL**: `/reset-password/<uidb64>/<token>/`

### 4. Profile Management
- **Profile**: Users can view and update their profile information.
  - **View**: `app/views.py` - `profile_view`
  - **Template**: `app/templates/app/profile.html`
  - **URL**: `/profile/`

## Running the Project

### 1. Running the Server
Start the development server:
```bash
python manage.py runserver
```
Open your web browser and go to `http://127.0.0.1:8000/`.

## SMTP Configuration

To enable password reset functionality, configure the following settings in `myproject/settings.py`:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.your-email-provider.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@example.com'
EMAIL_HOST_PASSWORD = 'your-email-password'
```

Replace the placeholder values with your SMTP provider's details.

## Page Functionalities

### Login Page
- **URL**: `/login/`
- **Functionality**: Allows users to log in using their email and password.
- **Template**: `app/templates/app/login.html`
- **Key Components**:
  - Email input
  - Password input
  - CSRF token for security

### Logout Page
- **URL**: `/logout/`
- **Functionality**: Logs users out of their session.
- **No Template Needed**: Redirects to the login page after logout.

### Signup Page
- **URL**: `/signup/`
- **Functionality**: Allows new users to register.
- **Template**: `app/templates/app/signup.html`
- **Key Components**:
  - Username input
  - Email input
  - Password input
  - Confirm password input
  - CSRF token for security

### Forgot Password Page
- **URL**: `/forgot-password/`
- **Functionality**: Allows users to request a password reset link.
- **Template**: `app/templates/app/forgot_password.html`
- **Key Components**:
  - Email input
  - CSRF token for security

### Reset Password Page
- **URL**: `/reset-password/<uidb64>/<token>/`
- **Functionality**: Allows users to reset their password using the link sent to their email.
- **Template**: `app/templates/app/reset_password.html`
- **Key Components**:
  - New password input
  - Confirm new password input
  - CSRF token for security

### Profile Page
- **URL**: `/profile/`
- **Functionality**: Allows users to view and update their profile information.
- **Template**: `app/templates/app/profile.html`
- **Key Components**:
  - Display of user information (e.g., username, email)
  - Inputs for updating user information
  - CSRF token for security

## Conclusion

This Django project provides a comprehensive user authentication system with essential features like login, logout, registration, and password management. The structure and use of libraries/modules ensure the project is robust and maintainable. The README file gives an overview of the project setup, key functionalities, and the necessary configuration steps to get the application running.
