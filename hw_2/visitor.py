class Visitor:
    def visit_element_a(self, element_a):
        pass

    def visit_element_b(self, element_b):
        pass


class ConcreteVisitor(Visitor):
    def visit_element_a(self, element_a):
        print("Visitor is processing ElementA")

    def visit_element_b(self, element_b):
        print("Visitor is processing ElementB")


class ElementA:
    def accept(self, visitor):
        visitor.visit_element_a(self)


class ElementB:
    def accept(self, visitor):
        visitor.visit_element_b(self)


if __name__ == "__main__":
    # Использование паттерна:
    visitor = ConcreteVisitor()

    element_a = ElementA()
    element_a.accept(visitor)  # Выведет "Visitor is processing ElementA"

    element_b = ElementB()
    element_b.accept(visitor)  # Выведет "Visitor is processing ElementB"
