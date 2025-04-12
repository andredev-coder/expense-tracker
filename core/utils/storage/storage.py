from abc import ABC, abstractmethod
from typing import List, Dict


class Storage(ABC):
    @abstractmethod
    def load(self) -> List[Dict]:
        pass

    @abstractmethod
    def save(self, *i: Dict) -> None:
        pass


