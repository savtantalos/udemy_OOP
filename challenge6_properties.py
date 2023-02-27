class Tablet:
    tablet_models = {'lite':{'base_storage': 32, 'memory': 2},
                     'pro':{'base_storage': 64, 'memory': 3},
                     'max':{'base_storage': 128, 'memory': 4}}
    max_memory = 1024
    def __init__(self, model):
        model = model.lower().strip()
        if not model in list(self.tablet_models.keys()):
            raise ValueError(f"The model  you have imported is not valid")
        specs = self.tablet_models[model]
        self.model = model
        self._base_storage = specs['base_storage']
        self._added_storage = 0
        self._memory = specs['memory']

    def __repr__(self):
        return f"Tablet: model = {self.model}, base storage = {self._base_storage}, memory = {self._memory}, additional storage = {self._added_storage}"
    def add_storage(self,value):
        if value <0:
            raise ValueError('You cannot insert negative added storage')
        if self._added_storage + value > self.max_memory:
            raise ValueError(f'The combination of added memory {value} with the base memory of {self.model}'
                             f'which is {self._base_storage}, exceeds the overall max memory we can provide{self.max_memory}.')

        self._added_storage +=value


    @property
    def storage(self):

        return self._base_storage + self._added_storage

    @storage.setter
    def storage(self,value):
        # self._storage = self.base_storage + self.added_storage + value
        if value >1024:
            raise ValueError(f'We do not offer a storage greater than {self.max_memory}MB')
        self._added_storage = None
        self._added_storage = value - self._base_storage

    @property
    def memory(self):
        return self._memory

    @property
    def base_storage(self):
        return self._base_storage

x = Tablet('pro')
x.storage = 100
print(x.__repr__())


