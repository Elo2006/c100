class Card(object):
    def __init__(self, model, color, company, speed):
        self.color = color
        self.model = model
        self.company = company
        self.speed = speed
        
o1 = Card("Prius", "grey", "Toyota", 200)
o2 = Card("RX 350", "black", "Lexus", 250)

print(o1.color)
print(o2.company)