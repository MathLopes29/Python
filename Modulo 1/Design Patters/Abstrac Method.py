from abc import ABC, abstractmethod

# Interface Abstrata para produtos A e B:
class AbstractProductA(ABC):
    @abstractmethod
    def operation_a(self) -> str:
        pass

class AbstractProductB(ABC):
    @abstractmethod
    def operation_b(self) -> str:
        pass

# Classes concretas de produtos A1 e A2
class ConcreteProductA1(AbstractProductA):
    def operation_a(self) -> str:
        return "ConcreteProductA1"

class ConcreteProductA2(AbstractProductA):
    def operation_a(self) -> str:
        return "ConcreteProductA2"

# Classes concretas de produtos B1 e B2
class ConcreteProductB1(AbstractProductB):
    def operation_b(self) -> str:
        return "ConcreteProductB1"

class ConcreteProductB2(AbstractProductB):
    def operation_b(self) -> str:
        return "ConcreteProductB2" 


#######################################################
# Interface Abstrata de Fabrica Abstrata
class AbstractFactory(ABC):
    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass

    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass

# Classe concretas da Fabrica Abstrada
class ConcreteFactory1(AbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA1()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB1()

class ConcreteFactory2(AbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA2()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB2()
    
#############################################################
# Cliente
class Client:
    def __init__(self, factory: AbstractFactory) -> None:
        self._product_a = factory.create_product_a()
        self._product_b = factory.create_product_b()

    def run(self) -> None:
        print(self._product_a.operation_a())
        print(self._product_b.operation_b())

# Cria um cliente com a fábrica concreta 1
client1 = Client(ConcreteFactory1())
client1.run()

# Cria um cliente com a fábrica concreta 2
client2 = Client(ConcreteFactory2())
client2.run()

