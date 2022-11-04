
class AnnualReturn():

    def __init__(self):
        self.get_values()
        self.calculate_return()
        self.display_return()
        
    def get_values(self):
        self.initial_value = float(input("Initial Price: "))
        self.current_value = float(input("Final Price: "))
        self.years = float(input("Years: "))
    
    def calculate_return(self):
        self.annualized_return = ((self.current_value / self.initial_value) ** (1 / self.years)) - 1
        self.annualized_return = self.annualized_return * 100

    def display_return(self):
        print("Annualized return: " + "{:,.2f}".format(self.annualized_return) + "%")

if __name__ == "__main__":
    print('Calculate the Annual Rate of Return of an investment.')
    oAnnualReturn = AnnualReturn()