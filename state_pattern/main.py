
from state_pattern.apple_state import AppleState
from state_pattern.banana_state import BananaState
from state_pattern.state_machine import StateMachine


if __name__ == "__main__":
    state_machine = StateMachine(AppleState())
    state_machine.print()

    state_machine = StateMachine(BananaState())
    state_machine.print()
