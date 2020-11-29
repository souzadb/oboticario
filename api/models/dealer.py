class DealerModel(object):
    def __init__(self, dealer):
        self.name = dealer['name']
        self.cpf = dealer['cpf']
        self.email = dealer['email']
        self.password = dealer['password']