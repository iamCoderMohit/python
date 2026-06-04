class countries():
    def __init__(self,name,population,arearank):
        self.name=name
        self.population=population
        self.arearank=arearank

    def info(self):
        return  f"country name= {self.name},country population= {self.population},area vise rank= {self.arearank}"

class India(countries):
    def __init__(self,name,population,arearank,states,languages):
        super().__init__(name,population,arearank)
        self.states=states
        self.languages=languages

    def info2(self):
        print (f"{super().info()}, total states= {self.states}, total official languages= {self.languages}")       

c2=India("india","1.4b",7,29,22)
c2.info2()