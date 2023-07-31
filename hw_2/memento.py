class Memento:
    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state


class Originator:
    def __init__(self):
        self._state = None

    def set_state(self, state):
        self._state = state

    def save_to_memento(self):
        return Memento(self._state)

    def restore_from_memento(self, memento):
        self._state = memento.get_state()


if __name__ == "__main__":

    # Использование паттерна:
    originator = Originator()
    originator.set_state("State 1")

    # Сохраняем состояние
    memento = originator.save_to_memento()

    originator.set_state("State 2")

    # Восстанавливаем состояние
    originator.restore_from_memento(memento)
    print(originator._state)  # Выведет "State 1"
