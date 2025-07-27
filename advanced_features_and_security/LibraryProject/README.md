# Advanced Features - Role-Based Permissions in LibraryProject

## Custom User Model
A custom user model `CustomUser` was implemented by extending `AbstractUser` in `bookshelf/models.py`.

## Custom Permissions
The `Book` model includes custom permissions defined in its `Meta` class:

```python
class Meta:
    permissions = [
        ("can_create", "Can create book"),
        ("can_edit", "Can edit book"),
        ("can_delete", "Can delete book"),
    ]


# Security Enhancements

### 1. settings.py
- `DEBUG = False`: Hides error details in production.
- `ALLOWED_HOSTS`: Only allows specific hostnames.
- `CSRF_COOKIE_SECURE`, `SESSION_COOKIE_SECURE`: Enforce secure cookies via HTTPS.
- `X_FRAME_OPTIONS`, `SECURE_BROWSER_XSS_FILTER`, `SECURE_CONTENT_TYPE_NOSNIFF`: Prevent XSS, clickjacking, and MIME sniffing.

### 2. templates
- All forms include `{% csrf_token %}` to prevent CSRF attacks.

### 3. views.py
- Views use Django ORM to prevent SQL injection.
- All POST methods are CSRF-protected.


## HTTPS Deployment Notes

In production, the application must be served over HTTPS.
This involves:
- Setting up SSL/TLS certificates (e.g., via Let’s Encrypt)
- Configuring the web server (e.g., Nginx) with SSL
- Enabling Django settings: SECURE_SSL_REDIRECT, CSRF_COOKIE_SECURE, etc.
