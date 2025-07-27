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
