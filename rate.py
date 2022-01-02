# inputs
initial_value = float(input("Precio Incial: "))
current_value = float(input("Precio Final: "))
years = float(input("Años: "))
dividend_value = float(input("Dividendo anual (%): "))


# Process
annualized_return = ((current_value / initial_value) ** (1 / years)) - 1
annualized_return = annualized_return * 100
total_return = annualized_return + dividend_value


# Outputs
print("Retorno Anualizado: " + "{:,.2f}".format(annualized_return) + "%")
print("Retorno Total: " + "{:,.2f}".format(total_return) + "%")
