

class CarriganTires:
    def __innit__(self, tire_wears):
        self.tire_wear_list = tire_wears
    
    def needs_service(self):
        for tire_value in self.tire_wear_list:
            if tire_value >= 0.9:
                return True
        return False


            