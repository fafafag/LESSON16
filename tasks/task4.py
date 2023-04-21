class User:
    def __init__(self, login, password):
        self.login = login
        self.password = password

    def view(self):
        print("Я - User. Могу просматривать содержимое")


class Moderator(User):
    def __init__(self, login, password, group_id):
        super().__init__(login, password)
        self.group_id = group_id

    def view(self):
        print("Я - Moderator. Могу просматривать содержимое")

    def redact(self):
        print("Я - Moderator. Могу редактировать содержимое")


user = User("user_login", "user_password")
moderator = Moderator("moderator_login", "moderator_password", "group_id_123")

user.view()
moderator.view()
moderator.redact()