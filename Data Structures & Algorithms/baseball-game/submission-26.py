class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record, result = [], 0 
        for i in operations:
            if i == '+':
                result+= record[-2]+record[-1]
                record.append(record[-2] + record[-1])
            elif i == 'D':
                result += (2*record[-1])
                record.append(2 * record[-1])
            elif i == 'C':
                result-= record.pop()
            else:
                result += int(i)
                record.append(int(i))
        return result#sum(record) # we could remove this final sum pass, by adding a variable which tracks a running total after each operation