from abc import ABC, abstractmethod

# Abstract product A
class Engine(ABC):

    @abstractmethod
    def start_engine(self):
        pass

class SUVEngine(Engine):

    def start_engine(self):
        print('assembling SUV Engine')

class SedanEngine(Engine):

    def start_engine(self):
        print('assembling SEDAN Engine')

class HatchbackEngine(Engine):

    def start_engine(self):
        print('assembling HATCHBACK Engine')

# Abstract product B
class Body(ABC):

    @abstractmethod
    def assemble_body(self):
        pass

class SUVBody(Body):

    def assemble_body(self):
        print('Assembling SUV body')

class SedanBody(Body):

    def assemble_body(self):
        print('Assembling sedan body')

class HatchbackBody(Body):

    def assemble_body(self):
        print('Assembling hatchback body')

# Abstract product C
class Interior(ABC):

    @abstractmethod
    def install_interior(self):
        pass

class SUVInterior(Interior):

    def install_interior(self):
        print('Installing SUV interior')

class SedanInterior(Interior):

    def install_interior(self):
        print('Installing sedan interior')

class HatchbackInterior(Interior):

    def install_interior(self):
        print('Installing hatchback interior')

# Abstract Factory
class CarFactory(ABC):

    @abstractmethod
    def create_engine(self):
        pass

    @abstractmethod
    def create_body(self):
        pass

    @abstractmethod
    def create_interior(self):
        pass

# Concrete Factory
class SUVFactory(CarFactory):

    def create_engine(self):
        return SUVEngine()

    def create_body(self):
        return SUVBody()

    def create_interior(self):
        return SUVInterior()

# Concrete Factory
class SedanFactory(CarFactory):

    def create_engine(self):
        return SedanEngine()

    def create_body(self):
        return SedanBody()

    def create_interior(self):
        return SedanInterior()

# Concrete Factory
class HatchbackFactory(CarFactory):

    def create_engine(self):
        return HatchbackEngine()

    def create_body(self):
        return HatchbackBody()

    def create_interior(self):
        return HatchbackInterior()

#Client
class CarDealer:

    def __init__(self, factory):
        self.engine = factory.create_engine()
        self.body = factory.create_body()
        self.interior = factory.create_interior()

    def assemble_car(self):
        print('Starting car assembly...')
        self.engine.start_engine()
        self.body.assemble_body()
        self.interior.install_interior()
        print('Car assembly completed.')

# Driver code
suv_factory = SUVFactory()
sedan_factory = SedanFactory()
hatchback_factory = HatchbackFactory()

suv_dealer = CarDealer(suv_factory)
sedan_dealer = CarDealer(sedan_factory)
hatchback_dealer = CarDealer(hatchback_factory)

suv_dealer.assemble_car()
sedan_dealer.assemble_car()
hatchback_dealer.assemble_car()
