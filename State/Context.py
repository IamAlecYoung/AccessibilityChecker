from State import State
from State.StateOutput import StateOutputs
from State.StatePages import StatePages

class Context:

    _state = None

    def __init__(self, state:State) -> None:
        self.setState(state)

        #self.__state_output = StateOutputs()
        #self.__state_pages = StatePages()

    def setState(self, state: State):

        print(f"Context: Transitioning to {type(state).__name__}")
        self._state = state
        self._state.context = self

    def doSomething(self):
        self._state.doSomething()
    
    # @property
    # def state_outputs(self):
    #     return self.__state_output

    # @property
    # def state_pages(self):
    #     return self.__state_pages


