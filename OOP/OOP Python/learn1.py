





class Idolgioitre:
    def __init__(self, name, age, features):
        self.name = name
        self.age = age
        self.__features = features
    
    def getFeatures(self):
        return self.__features
    def setFeatures(self, features):
        self.__features = features

class giangHo(Idolgioitre):
    def __init__(self, name, age, features, location):
        super().__init__(name, age, features)
    
    def liveStream(self):
        pass

    def signatureQuote(self):
        print("dmm, ao that day")

class tiktoker(Idolgioitre):
    def __init__(self, name, age, features, action):
        super().__init__(name, age, features)

    def liveStream(self):
        pass

    def scandal(self):
        print("ghen với lê tuấn khang")

obj1 = giangHo("kha banh", 30, "dau cat moi", "trong tu")
obj2 = tiktoker("khiet dan", 25, "be de", "recording")

obj1.signatureQuote()
obj2.scandal()

print(obj1.getFeatures())
obj1.setFeatures("toc banh nhu ll")
print(obj1.getFeatures())


