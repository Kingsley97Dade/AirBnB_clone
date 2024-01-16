<<<<<<< HEAD
#!/usr/bin/python3

"""User Module:
Inherits from Superclass BaseModel
"""

from models.base_model import BaseModel


class User(BaseModel):
    """User class that inherits from BaseModel.
    This creates the profile for user"""
    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""
=======
#!/usr/bin/python3

"""User Module:
Inherits from Superclass BaseModel
"""

from models.base_model import BaseModel


class User(BaseModel):
    """User class that inherits from BaseModel.
    This creates the profile for user"""
    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""
>>>>>>> 3b07b26a2690f448f938087e6d78c3202fb4f5ea
