from abc import ABC, abstractmethod

class AttackStrategy(ABC):

    @abstractmethod
    def attack(self):
        pass

class SlideAttack(AttackStrategy):

    def attack(self):
        print('Slide attack')

class JumpAttack(AttackStrategy):

    def attack(self):
        print('Jump attack')

class GameTemplate(ABC):
    def make_game(self, strategy):
        self.start_game()
        strategy.attack()
        self.end_game()

    @abstractmethod
    def start_game(self):
        pass

    @abstractmethod
    def end_game(self):
        pass

class SuperMario(GameTemplate):

    def start_game(self):
        print('Launching game')

    def end_game(self):
        print('Closing game')

# Driver code
attack1 = SlideAttack()
attack2 = JumpAttack()

Mario = SuperMario()
Mario.make_game(attack1)
