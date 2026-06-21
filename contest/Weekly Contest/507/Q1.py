class Solution:
    def maxDistance(self, moves: str) -> int:
        return (
            abs(moves.count("R") - moves.count("L"))
            + abs(moves.count("U") - moves.count("D"))
            + moves.count("_")
        )