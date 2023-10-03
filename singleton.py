# singleton.py
class Singleton:
    _instance = None #static variable

#check instance
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
            cls._instance.init_singleton()
        return cls._instance

#data initialization
    def init_singleton(self):
        self.some_data = None