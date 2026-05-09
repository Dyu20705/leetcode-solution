class Solution:
    def scoreValidator(self, events: list[str]) -> list[int]:
        score = 0
        counter = 0

        for event in events:
            if event == "W":
                counter += 1
                if counter == 10:
                    break

            elif event == "WD" or event == "NB":
                score += 1

            elif len(event) == 1:
                c = ord(event) - 48
                if 1 <= c <= 6:
                    score += c

        return [score, counter]
