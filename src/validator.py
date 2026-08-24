class Validator:
    def __init__(self) -> None:
        pass

    def validate_email(self, email: str) -> bool:

        if email.count("@") != 1:
            return False

        user, domain = email.split("@")
        return "." in domain

    def validate_password(self, password: str) -> bool:
        return bool(len(password) >= 8 and any(char.isdigit() for char in password))
