class Cart:
    def __init__(self,name,price,image,qty):
        self.name=name
        self.price=price
        self.image=image
        self.qty=qty
    def showName(self):
        return self.name

    def showPrice(self):
        return self.price

    def showImage(self):    
        return self.image

    def showQty(self):
        return self.qty

    def showProduct(self):
        return {"name":self.name,"price":self.price,"qty":self.qty,"image":self.image}