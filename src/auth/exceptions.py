from fastapi import HTTPException


class InvalidCredentials(HTTPException):
    def __init__(self):
        super().__init__(status_code=401, detail="Incorrect username or password")


class InvalidAuthenthicationCredential(HTTPException):
    def __init__(self):
        super().__init__(status_code=401, detail="Invalid authentication credential")


class InactiveUser(HTTPException):
    def __init__(self):
        super().__init__(status_code=403, detail="Inactive user")


class NotEnoughPermissions(HTTPException):
    def __init__(self):
        super().__init__(status_code=403, detail="Not enough permissions")


class UserDoesNotExist(HTTPException):
    def __init__(self):
        super().__init__(status_code=404, detail="User does not exist")


class NoData(HTTPException):
    def __init__(self):
        super().__init__(status_code=404, detail="Data was not found")


class NoUserData(HTTPException):
    def __init__(self):
        super().__init__(status_code=404, detail="User data was not found")

class UserAlreadyExists(HTTPException):
    def __init__(self):
        super().__init__(status_code=409, detail="User already exists")


class UserAlreadyActive(HTTPException):
    def __init__(self):
        super().__init__(status_code=409, detail="User is already active")