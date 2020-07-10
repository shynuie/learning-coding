class Stock:
    def __init__(self, data):
        self.bull = 0
        self.bear = 0
        self.data = data
        self.output = []
        self.price_b = data[0]
        print(self.data)

    def a(self):
        for price in self.data:
            if price > self.price_b:
                self.bull += 1
                self.bear = 0
            elif price < self.price_b:
                self.bull = 0
                self.bear += 1
            else :
                self.bull = 0
                self.bear = 0
            self.price_b = price
            if self.bull >= 3:
                self.output.append(1)
            elif self.bear >= 3:
                self.output.append(-1)
            else:
                self.output.append(0)


def main(data):
    s1 = Stock(data)
    s1.a()
    print(s1.output)

main((9422, 9468, 9512, 9524, 9550, 9450, 9410, 9368))