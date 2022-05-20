class Car(object):
    def __init__(self,model,color,company,speed):
        self.model = model
        self.color = color
        self.company = company
        self.speed = speed
    
    def start(self):
        print("Started")

    def stop(self):
        print("Stopped")

    def accelarate(self):
        print("accelarating")

Harrier = Car("model","Blue","Tata",200)

print(Harrier.start())
            