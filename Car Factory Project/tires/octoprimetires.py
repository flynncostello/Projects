

class OctoprimeTires:
    def __init__(self, tire_wears):
        self.tire_wear_list = tire_wears
    
    def needs_service(self):
        total = 0
        for tire in self.tire_wear_list:
            total += tire
        
        if total >= 3:
            return True # Needs to be serviced
        return False