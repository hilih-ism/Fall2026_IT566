from abc import ABC, abstractmethod


class PersistenceWrapper(ABC):

    @abstractmethod
    def save_expense(self, collection, expense):
        pass

    @abstractmethod
    def load_expenses(self, collection):
        pass

    @abstractmethod
    def load_all_expenses(self):
        pass