class ProductOfNumbers(object):

    def __init__(self):
        self.prefix_product = [1]

    def add(self, num):
        if num == 0:
            self.prefix_product = [1]
        else:
            self.prefix_product.append(self.prefix_product[-1] * num)  
        
    def getProduct(self, k):
        if k >= len(self.prefix_product):
            return 0
        return self.prefix_product[-1] // self.prefix_product[-(k + 1)]