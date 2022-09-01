from app.models.calculator import Calculator
class CalculatorService(object):
    def __init__(self) -> None:
        pass
        
    def calculate(self, first, second):
        calculator = Calculator(first, second)
        return f'{calculator.first} + {calculator.second} = {calculator.sum()}   {calculator.first} - {calculator.second} = {calculator.subtract()}   {calculator.first} * {calculator.second} = {calculator.multi()}   {calculator.first} / {calculator.second} = {calculator.divide()}'
        