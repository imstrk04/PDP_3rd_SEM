'''# Define abstract classes for components
class Engine:
    def start(self):
        pass

class Body:
    def assemble(self):
        pass

class Interior:
    def design(self):
        pass

# Concrete implementations of components
class SedanEngine(Engine):
    def start(self):
        print("Sedan Engine started")

class SUVEngine(Engine):
    def start(self):
        print("SUV Engine started")

class HatchbackEngine(Engine):
    def start(self):
        print("Hatchback Engine started")

class SedanBody(Body):
    def assemble(self):
        print("Sedan body assembled")

class SUVBody(Body):
    def assemble(self):
        print("SUV body assembled")

class HatchbackBody(Body):
    def assemble(self):
        print("Hatchback body assembled")

class SedanInterior(Interior):
    def design(self):
        print("Sedan interior designed")

class SUVInterior(Interior):
    def design(self):
        print("SUV interior designed")

class HatchbackInterior(Interior):
    def design(self):
        print("Hatchback interior designed")

# Abstract Factory
class CarFactory:
    def create_engine(self):
        pass

    def create_body(self):
        pass

    def create_interior(self):
        pass

# Concrete factories
class SedanFactory(CarFactory):
    def create_engine(self):
        return SedanEngine()

    def create_body(self):
        return SedanBody()

    def create_interior(self):
        return SedanInterior()

class SUVFactory(CarFactory):
    def create_engine(self):
        return SUVEngine()

    def create_body(self):
        return SUVBody()

    def create_interior(self):
        return SUVInterior()

class HatchbackFactory(CarFactory):
    def create_engine(self):
        return HatchbackEngine()

    def create_body(self):
        return HatchbackBody()

    def create_interior(self):
        return HatchbackInterior()

# Client code
def produce_car(factory):
    engine = factory.create_engine()
    body = factory.create_body()
    interior = factory.create_interior()

    engine.start()
    body.assemble()
    interior.design()

# Simulation
if __name__ == "__main__":
    try:
        # Create instances of different car models
        sedan_factory = SedanFactory()
        produce_car(sedan_factory)

        suv_factory = SUVFactory()
        produce_car(suv_factory)

        hatchback_factory = HatchbackFactory()
        produce_car(hatchback_factory)

        # Demonstrate raising an exception (e.g., trying to start the Hatchback engine twice)
        hatchback = hatchback_factory.create_engine()
        hatchback.start()  # This should work fine
        hatchback.start()  # This should raise an exception since starting twice is not allowed

    except Exception as e:
        print(f"Exception: {e}")
'''

# Abstract Product: Engine
class Engine:
    def display_info(self):
        pass

# Concrete Products: SedanEngine, SUVEngine, HatchbackEngine
class SedanEngine(Engine):
    def display_info(self):
        return "Sedan Engine"

class SUVEngine(Engine):
    def display_info(self):
        return "SUV Engine"

class HatchbackEngine(Engine):
    def display_info(self):
        return "Hatchback Engine"

# Abstract Product: Body
class Body:
    def display_info(self):
        pass

# Concrete Products: SedanBody, SUVBody, HatchbackBody
class SedanBody(Body):
    def display_info(self):
        return "Sedan Body"

class SUVBody(Body):

    def display_info(self):
        return "SUV Body"

class HatchbackBody(Body):
    def display_info(self):
        return "Hatchback Body"

# Abstract Product: Interior
class Interior:
    def display_info(self):
        pass

# Concrete Products: SedanInterior, SUVInterior, HatchbackInterior
class SedanInterior(Interior):
    def display_info(self):
        return "Sedan Interior"

class SUVInterior(Interior):
    def display_info(self):
        return "SUV Interior"

class HatchbackInterior(Interior):
    def display_info(self):
        return "Hatchback Interior"

# Abstract Factory
class CarFactory:
    def create_engine(self):
        pass

    def create_body(self):
        pass

    def create_interior(self):
        pass

# Concrete Factories: SedanFactory, SUVFactory, HatchbackFactory
class SedanFactory(CarFactory):
    def create_engine(self):
        return SedanEngine()

    def create_body(self):
        return SedanBody()

    def create_interior(self):
        return SedanInterior()

class SUVFactory(CarFactory):
    def create_engine(self):
        return SUVEngine()

    def create_body(self):
        return SUVBody()

    def create_interior(self):
        return SUVInterior()

class HatchbackFactory(CarFactory):
    def create_engine(self):
        return HatchbackEngine()

    def create_body(self):
        return HatchbackBody()

    def create_interior(self):
        return HatchbackInterior()

# Client Code
def assemble_car(factory):
    engine = factory.create_engine()
    body = factory.create_body()
    interior = factory.create_interior()

    print(f"Engine: {engine.display_info()}")
    print(f"Body: {body.display_info()}")
    print(f"Interior: {interior.display_info()}")
    print()

try:
    sedan_factory = SedanFactory()
    suv_factory = SUVFactory()
    hatchback_factory = HatchbackFactory()

    assemble_car(sedan_factory)
    assemble_car(suv_factory)
    assemble_car(hatchback_factory)
except Exception as e:
    print(f"An error occurred: {e}")