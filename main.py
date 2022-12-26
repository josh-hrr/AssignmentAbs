from abc import abstractmethod, ABC

class TouchScreenLaptop(ABC):
  def __init__(self, model, year):
    self.model = model
    self.year = year

  @abstractmethod
  def scroll(self):
    pass

  @abstractmethod
  def click(self):
    pass

class HP(TouchScreenLaptop):
  def __init__(self, model, year):
    super().__init__(model, year)

  def scroll(self):
    super().scroll()
    print('Scrolling HP!') 

class DELL(TouchScreenLaptop):
  def __init__(self, model, year):
    super().__init__(model, year)

  def scroll(self):
    super().scroll()
    print('Scrolling DELL!') 

class HPNotebook(TouchScreenLaptop): 
  def __init__(self, model, year):
    super().__init__(model, year)

  def click(self):
    super().click()
    print('Click HP!')

  def scroll(self):
    super().scroll()
    print('Scrolling HP!') 

class DELLNotebook(TouchScreenLaptop): 
  def __init__(self, model, year):
    super().__init__(model, year)

  def click(self):
    super().click()
    print('Click DELL!') 

  def scroll(self):
    super().scroll()
    print('Scrolling DELL!') 


HP1 = HPNotebook('testing objt1', 2022) 
print(HP1.click())
print(HP1.scroll())

DELL1 = DELLNotebook('testing objt2', 2020)
print(DELL1.click())
print(DELL1.scroll())
