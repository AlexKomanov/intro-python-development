def inspect(func):
    def wrapper_func(*args, **kwargs):
        print(f"Running {func.__name__}")
        values = func(*args, **kwargs)
        print(f"Result: {values}")

    return wrapper_func


@inspect
def combine(a, b):
    return a + b


combine(3, 2)


class User:
    base_url = 'https://example.com/api'

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @classmethod
    def query(cls, query_string):
        return cls.base_url + '?' + query_string

    @staticmethod
    def name():
        return "Alex Komanov"

    @property
    def full_name(self):
        return f"Your name is: {self.first_name} {self.last_name}"


print(User.name)
print(User.name())

print(User.query('previewRelease=false'))

user = User("User", "User")

print(user.full_name)

