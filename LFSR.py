from collections import deque
from time import time_ns

MIN_REGISTER_LENGTH = 10
MAX_REGISTER_LENGTH = 32


class LFSR:
    def __init__(
        self,
        REGISTER_LENGTH=MIN_REGISTER_LENGTH,
        seed=None,
    ) -> None:
        self._REGISTER_LENGTH = REGISTER_LENGTH
        assert isinstance(
            seed, (type(None), int)
        ), "seed should be a positive int with register length"
        if seed is None:
            seed = int(str(time_ns()))
        self._register_bank = deque(int(value) for value in f"{seed:32b}")

    @property
    def REGISTER_LENGTH(self) -> str:
        return self._REGISTER_LENGTH

    @REGISTER_LENGTH.setter
    def REGISTER_LENGTH(self, REGISTER_LENGTH: str):
        assert (
            isinstance(REGISTER_LENGTH, int)
            or REGISTER_LENGTH < MIN_REGISTER_LENGTH
            or MAX_REGISTER_LENGTH > REGISTER_LENGTH
        ), f"REGISTER_LENGTH should be an int > {self.MIN_REGISTER_LENGTH} and int <= {self.MAX_REGISTER_LENGTH}"
        print("Setting register length")
        self._REGISTER_LENGTH = REGISTER_LENGTH

    def generate(self):
        self._register_bank.appendleft(
            self._register_bank[-2] ^ self._register_bank[-1]
        )
        output = self._register_bank.pop()
        return output

    @property
    def register_bank_repr(self):
        return "".join(map(lambda value: str(value), self._register_bank))
