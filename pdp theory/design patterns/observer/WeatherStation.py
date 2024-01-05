class WeatherStation:

    def __init__(self, place, _temp):
        self.obs_list = []
        self.place = place
        self._temp = _temp
    
    def __str__(self):
        return f'Temp at {self.place} is {self.temp} degree Celsius'

    def attach(self, obs):
        self.obs_list.append(obs)
    
    def dettach(self, obs):
        self.obs_list.remove(obs)
    
    @property
    def temp(self):
        return self._temp
    
    @temp.setter
    def temp(self, new_temp):  # Corrected to match the property name
        if new_temp != self._temp:
            self._temp = new_temp
            self.notify()

    
    def notify(self):
        for x in self.obs_list:
            x.update(self)
    
class PhoneDisplay:

    def __init__(self):
        pass

    def update(self, temp):
        print("Phone Display:",temp)

class WindowDisplay:

    def __init__(self) -> None:
        pass
    
    def update(self, temp):
        print("Weather display:",temp)

if __name__ == '__main__':
    w = WeatherStation('Chennai', 27)
    observer1 = PhoneDisplay()
    observer2 = WindowDisplay()

    w.attach(observer1)
    w.attach(observer2)
    w.temp = 26
