class NegativeAgeError(Exception):
    """Exception raised for negative user age."""

    def _init_(self, age, message="Age cannot be negative"):
        self.age = age
        self.message = message
        super()._init_(self.message)

    def _str_(self):
        return f"{self.message}: {self.age}"

def get_user_age():
    try:
        user_age = int(input("enter age"))
    except BaseException:
        print("balbla")
    if user_age < 0:
        raise NegativeAgeError("age can not be negative")
    return user_age


