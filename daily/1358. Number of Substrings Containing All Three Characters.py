import numpy as np
_INDICES = np.arange(1, 50_001, dtype=np.uint16)
_WORK = np.zeros((100, 50_001), dtype=np.uint16)

class Solution:
    def numberOfSubstrings(
        self,
        s: str,
        indices=_INDICES,
        work=_WORK,
        np=np,
    ) -> int:
        n = len(s)

        if n < 256:
            total = last_a = last_b = last_c = 0

            for position, ch in enumerate(s, 1):
                if ch == "a":
                    total += last_b if last_b < last_c else last_c
                    last_a = position
                elif ch == "b":
                    total += last_a if last_a < last_c else last_c
                    last_b = position
                else:
                    total += last_a if last_a < last_b else last_b
                    last_c = position

            return total

        chars = np.frombuffer(s.encode(), dtype=np.uint8)

        places = work[97:100, :n + 1]
        places.fill(0)

        positions = indices[:n]

        work[chars, positions] = positions

        np.maximum.accumulate(places, axis=1, out=places)

        np.minimum(places[0], places[1], out=places[0])
        np.minimum(places[0], places[2], out=places[0])

        return int(places[0].sum(dtype=np.uint64))