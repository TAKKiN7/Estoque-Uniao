class Autoridade_User():
    def __init__(self):
        self._autoridade : str = "Normal"

    @property
    def autoridade(self):
        return self._autoridade


    @autoridade.setter
    def autoridade(self, autoridade : str):
        self._autoridade = autoridade





user_autoridade : Autoridade_User = Autoridade_User()