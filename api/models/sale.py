class SaleModel(object):
    def __init__(self, sale):
        self.cod = sale['cod']
        self.value = sale['value']
        self.date = sale['date']
        self.cpf = sale['cpf']
        self.status = sale['status']