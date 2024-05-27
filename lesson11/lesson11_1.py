
class Phone:
    brand = ""
    model = ""
    issue_year = ''

    def __init__(self, brand, model,issue_year) -> None:
        self.brand = brand
        self.model = model
        self.issue_year = issue_year
    
    def receive_call(self, name):
        print(f"<{self.brand}-{self.model}> - Call {name}")
    
    def get_info(self):
       return (self.brand, self.model,self.issue_year)
    
    def __str__(self):    
        return f" Brand: {self.brand}\n Model: {self.model}\n Issue year: {self.issue_year}\n"
        
        

samsung = Phone('samsung', 'A50', '2022')    

samsung.receive_call('Alexandr')
print(samsung.get_info())
print(samsung)
