# ==========================================================
# ABSTRACTION - Example 1
# ==========================================================
from abc import ABC, abstractmethod

class Bank(ABC):
    def database(self):
        print("Database is Connected")

    @abstractmethod
    def security(self):
        pass

class Mobile(Bank):
    def mob(self):
        print("Mobile Application")

    def security(self):
        print("Mobile Security")

m = Mobile()
m.mob()
m.database()
m.security()