from collections import defaultdict
class SQL:

    def __init__(self, names: List[str], columns: List[int]):
        self.d = defaultdict(list)

    def insertRow(self, name: str, row: List[str]) -> None:
        self.d[name].append(row)
        

    def deleteRow(self, name: str, rowId: int) -> None:
        pass

    def selectCell(self, name: str, rowId: int, columnId: int) -> str:
        return self.d[name][rowId-1][columnId-1]
