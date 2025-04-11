import orjson


class Storage:
    def __init__(self, filename: str = '.transactions.json'):
        self.file = open(filename, 'r+', encoding='utf-8')
        self.main_key = 'transactions'

    def read(self) -> str:
        self.file.seek(0)
        return self.file.read()

    def insert(self, *i: dict) -> None:
        data = {self.main_key: list(i)}
        
        self.clear()
        self.file.write(orjson.dumps(data, option=orjson.OPT_INDENT_2).decode('utf-8'))
        self.save()

    def clear(self):
        self.file.seek(0)
        self.file.truncate()

    def save(self):
        self.file.seek(0)
        self.file.flush()

    def close(self):
        self.file.close()

