class Strategy:
    def execute(self):
        pass


class ConcreteStrategyA(Strategy):
    def execute(self):
        print("Executing strategy A")


class ConcreteStrategyB(Strategy):
    def execute(self):
        print("Executing strategy B")


class Context:
    def __init__(self, strategy):
        self._strategy = strategy

    def set_strategy(self, strategy):
        self._strategy = strategy

    def execute_strategy(self):
        self._strategy.execute()


if __name__ == "__main__":
    # Использование паттерна:
    context = Context(ConcreteStrategyA())
    context.execute_strategy()  # Выведет "Executing strategy A"

    context.set_strategy(ConcreteStrategyB())
    context.execute_strategy()  # Выведет "Executing strategy B"
