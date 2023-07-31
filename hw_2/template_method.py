class AbstractClass:
    def template_method(self):
        self.step_one()
        self.step_two()

    def step_one(self):
        pass

    def step_two(self):
        pass


class ConcreteClassA(AbstractClass):
    def step_one(self):
        print("ConcreteClassA: Step one")

    def step_two(self):
        print("ConcreteClassA: Step two")


class ConcreteClassB(AbstractClass):
    def step_one(self):
        print("ConcreteClassB: Step one")

    def step_two(self):
        print("ConcreteClassB: Step two")


if __name__ == "__main__":
    # Использование паттерна:
    concrete_a = ConcreteClassA()
    concrete_a.template_method()
    # Выведет:
    # ConcreteClassA: Step one
    # ConcreteClassA: Step two

    concrete_b = ConcreteClassB()
    concrete_b.template_method()
    # Выведет:
    # ConcreteClassB: Step one
    # ConcreteClassB: Step two
