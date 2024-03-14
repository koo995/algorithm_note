class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        # logs을 알맞게 정렬하는 것이 문제이다.
        letters = []
        digits = []
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)

        letters.sort(key=lambda log: (log.split()[1:], log.split()[0]))
        return letters + digits
