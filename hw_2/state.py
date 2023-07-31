class State:
    def do_action(self, context):
        pass


class StateA(State):
    def do_action(self, context):
        print("State A")
        context.set_state(StateB())


class StateB(State):
    def do_action(self, context):
        print("State B")
        context.set_state(StateA())


class Context:
    def __init__(self):
        self._state = StateA()

    def set_state(self, state):
        self._state = state

    def do_action(self):
        self._state.do_action(self)


if __name__ == "__main__":
    # Использование паттерна:
    context = Context()
    context.do_action()  # Выведет "State A"
    context.do_action()  # Выведет "State B"
    context.do_action()  # Выведет "State A" и так далее
