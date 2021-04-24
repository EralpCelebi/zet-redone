class Data:
    def __init__(self, data: dict) -> None:
        self.data = data
    
    def Get(self, target):
        try:
            return self.data[target]
        except:
            return False

    def Set(self, target, value) -> bool:
        try:
            self.data[target] = value
            return True
        except:
            return False
