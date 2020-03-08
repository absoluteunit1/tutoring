class Townhouse:

    building = "home"

    def __init__(self, color, address):

        self.color = color
        self.address = address
    
    def description(self, description):
        return description


tH1 = Townhouse('red', 2)

tH2 = Townhouse('blue', 4)

print(tH1.color, tH2.address)
print(tH1.address)
print()
print(tH2.color)
print(tH2.address)


print(tH1.description("Nice family home"))
print(tH2.description("Nice home for a couple"))

