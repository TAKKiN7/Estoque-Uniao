class Autoridade_User():
    def __init__(self):
        self._autoridade : str = "Defualt"
        self._user : str = "user"


    @property
    def autoridade(self):
        return self._autoridade


    @autoridade.setter
    def autoridade(self, autoridade : str):
        self._autoridade = autoridade


    @property
    def user(self):
        return self._user
    
    @user.setter
    def user(self, user : str):
        self._user = user


user_autoridade : Autoridade_User = Autoridade_User()