class product :

    def __init__(self,name,**kwargs):
        super().__init__(**kwargs)
        self.name=name

    def display(self):
        return f'{self.name}'
