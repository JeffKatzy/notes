class Bundle:
    def price(self):
        if self.weight < 5:
            return 10
        else:
            return 10 + (self.weight - 5)*1.5