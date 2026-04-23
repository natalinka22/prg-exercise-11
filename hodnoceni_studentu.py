class HodnoceniStudentu:
    def __init__(self, scores):
        self.scores = list(scores)
        self._sorted_scores = None

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)

    def get_grade(self, index):
        score = self.scores[index]

        if score >= 90:
            return 'A'
        elif score >= 80:
            return 'B'
        elif score >= 70:
            return 'C'
        elif score >= 60:
            return 'D'
        elif score >= 50:
            return 'E'
        else:
            return 'F'

    def find(self, score):
        indexes = []
        index = 0

        while index < len(self.scores):
            if self.scores[index] == score:
                indexes.append(index)
            index = index + 1

        return indexes

    def get_sorted(self):
        scores = list(self.scores)
        n = len(scores)

        i = 0
        while i < n:
            swapped = False
            j = 0

            while j < (n - 1 - i):
                if scores[j] > scores[j + 1]:
                    scores[j], scores[j + 1] = scores[j + 1], scores[j]
                    swapped = True
                j = j + 1

            if swapped is False:
                break

            i = i + 1

        return scores

    def average(self):
        if self.count() == 0:
            return 0.0

        total = 0
        index = 0
        while index < len(self.scores):
            total = total + self.scores[index]
            index = index + 1

        return total / self.count()

    def best(self):
        sorted_scores = self.get_sorted()
        if len(sorted_scores) == 0:
            return None

        return sorted_scores[-1]

    def worst(self):
        sorted_scores = self.get_sorted()
        if len(sorted_scores) == 0:
            return None

        return sorted_scores[0]

    def pass_rate(self):
        if self.count() == 0:
            return 0.0

        passed = 0
        index = 0
        while index < len(self.scores):
            if self.scores[index] >= 50:
                passed = passed + 1
            index = index + 1

        return passed / self.count()

    def find_sorted(self, score):
        if self._sorted_scores is None:
            self._sorted_scores = self.get_sorted()

        left = 0
        right = len(self._sorted_scores) - 1

        while left <= right:
            middle = (left + right) // 2
            value = self._sorted_scores[middle]

            if value == score:
                return middle

            if value < score:
                left = middle + 1
            else:
                right = middle - 1

        return None

    def __str__(self):
        return f"HodnoceniStudentu: {self.count()} studentu, prumer {self.average():.1f}"




