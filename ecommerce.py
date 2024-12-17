class product:
  def __init__(self, name, price, stock):
    self.name = name
    self.price = price
    self.stock = stock
    
  def purchase(self, quantity):
    if quantity <= self.stock:
      self.stock = quantity
      print(f"{quantity} units of {self.name} purchased.")
    else:
      print(f"insufficient stock for {self.name}.")
      
product = product("Vitamin c suppliment", 10.99, 50)

product.purchase(5)