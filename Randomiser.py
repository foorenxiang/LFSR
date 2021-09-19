from LFSR import LFSR


class Randomiser:
    def __init__(self) -> None:
        self._LFSR = LFSR()

    def generate(self):
        run_generator_this_many_times = self._LFSR.REGISTER_LENGTH
        accumulated_number = int(
            "".join(
                str(self._LFSR.generate()) for _ in range(run_generator_this_many_times)
            ),
            2,
        )
        return accumulated_number
