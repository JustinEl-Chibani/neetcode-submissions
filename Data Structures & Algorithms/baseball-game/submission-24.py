class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for i in operations:
            if i == '+':
                record.append(record[-2] + record[-1])
            elif i == 'D':
                record.append(2 * record[-1])
            elif i == 'C':
                record.pop()
            else:
                record.append(int(i))
        return sum(record) # we could remove this final sum pass, by adding a variable which tracks a running total after each operation