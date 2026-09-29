class Device:
    def __init__(self):
        self.__state="OFF" #private attribute which cannot be accessed by external code and can only be modified using the start or stop methods
    
    def start(self):
        if self.__state=="ON":
            return False
        self.__state="ON"
        return True
   
    def stop(self):
        if self.__state=="OFF":
            return False
        self.__state="OFF"
        return True
   
    #getter method for reading the current state of device
    def get_state(self):
        return self.__state
    
    

class Motor(Device):
    def __init__(self):
        super().__init__()

    #method overriding
    def start(self):
        result=super().start()
        if result is True:
            print("Motor has started")
        return result

    def stop(self):
        result=super().stop()
        if result is True:
            print("Motor has stopped")
        return result

class Light(Device):
    def __init__(self):
        super().__init__()
    
    def start(self):
        result=super().start()
        if result is True:
            print("Light switched on")
        return result

    def stop(self):
        result=super().stop()
        if result is True:
            print("Light switched off")
        return result

