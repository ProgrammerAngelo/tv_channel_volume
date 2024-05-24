class tv:
#add a data for instance variables
    def __init__(self):
        #set the deffaukt settings
        self.channel = 1
        self.volume = 1
        self.tv_on = False
#add a method for power on
    def turn_on(self):
        self.tv_on = True
#add a method for power off
    def turn_off(self):
        self.tv_on = False
#add a method for getting the channel
    def get_channel(self):
        return self.channel
#method for setting the channel to 1-120
    def set_channel(self,channel):
        if self.tv_on and 1 <= channel <= 120:
            self.channel = channel
#add a method for getting the volume