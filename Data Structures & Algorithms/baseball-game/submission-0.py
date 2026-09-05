class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = [] 
        for i in range(len(operations)):
            print(record)
            if operations[i] == "+":
                record.append(record[len(record) - 1] + record[len(record) - 2])
            elif operations[i] == "D":
                record.append(record[len(record) - 1] * 2)
            elif operations[i] == "C":
                record = record[0:len(record) - 1]
            else:
                record.append(int(operations[i]))
        return sum(record)