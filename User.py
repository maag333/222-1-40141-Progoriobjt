from _typeshed import Self


class User:

    """ id = 100
    full_name = "Full name"
    personal_email = "personal_email@.com" """

    def _init_(self, id, full_name, personal_name):
        self.id = id
        self.full_name = full_name,
        self.personal_email = personal_email

object_user = User("01220300007","Mario Alcoccer","maag333@gmail.com") 
print(object_user)
print("0" + str(object_user.id))
print(object_user.full_name)
print(object_user.personal_email)