class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        if operations is False:
            return 0
        for i in operations:
            if i == '+':
                record.append(record[-2] + record[-1])
            elif i == 'C':
                record.pop()
            elif i == 'D':
                record.append(2 * record[-1])
            else:
                record.append(int(i))
            print(record)
        return sum(record)