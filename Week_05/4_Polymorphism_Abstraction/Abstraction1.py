# ==========================================================
# ABSTRACT CLASS - CORRECT PROGRAM
# ==========================================================

# from abc import ABC, abstractmethod

# class Bank(ABC):
#     def database(self):
#         print("Database is Connected")

#     @abstractmethod
#     def security(self):
#         pass

# class Desktop(Bank):
#     def desk(self):
#         print("Desktop Application")

# d = Desktop()
# d.desk()

# TypeError: Can't instantiate abstract class Desktop without an implementation for abstract method 'security'

# ==========================================================
# ABSTRACT CLASS - CORRECT PROGRAM
# ==========================================================
from abc import ABC, abstractmethod

class Bank(ABC):
    def database(self):
        print("Database is Connected")

    @abstractmethod
    def security(self):
        pass

class Desktop(Bank):

    def desk(self):
        print("Desktop Application")

    def security(self):
        print("Desktop Security")

d = Desktop()
d.desk()
d.database()
d.security()