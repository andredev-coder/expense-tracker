import orjson
from typing import List, Dict
from .storage import Storage


class JSONFileStorage(Storage):
    def __init__(self, filename: str = '.transactions.json'):
        self.file = open(filename, 'r+', encoding='utf-8')
        self.main_key = 'transactions'

    def load(self) -> List[Dict]:
        self.file.seek(0)
        return orjson.loads(self.file.read())[self.main_key]
    
    def save(self, *i: Dict) -> None:
        data = {self.main_key: list(i)}
        
        self.clear()
        self.file.write(orjson.dumps(data, option=orjson.OPT_INDENT_2).decode('utf-8'))
        
        self.flush()

    def clear(self) -> None:
        self.file.seek(0)
        self.file.truncate()

    def flush(self) -> None:
        self.file.seek(0)
        self.file.flush()

    def close(self) -> None:
        self.file.close()
