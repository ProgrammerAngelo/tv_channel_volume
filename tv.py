class tv:
#add a data for instance variables
    def __init__(self):
        #set the deffault settings
        self.channel = 1
        self.volume = 1
        self.tv_on = False
#method for power on
    def turn_on(self):
        self.tv_on = True
#method for power off
    def turn_off(self):
        self.tv_on = False
#method for getting the channel
    def get_channel(self):
        return self.channel
#method for setting the channel to 1-120
    def set_channel(self,channel):
        if self.tv_on and 1 <= channel <= 120:
            self.channel = channel
#method for getting the volume
    def get_volume(self):
        return self.volume
#method for setting the volume to 1-7
    def set_volume(self, volume):
        if self.tv_on and 1 <= volume <= 7:
            self.volume = volume
#method for increasing the channel by 1 if the tv is on and if the current channel is less than 120
    def channel_up(self):
        if self.tv_on and self.channel < 120:
            self.channel += 1
#method for decreasing the channel by 1 if  the tv is on and if the current channel is greater than 1
    def channel_down(self):
        if self.tv_on and self.channel > 1:
            self.channel -=1
#method for increasing the volume by 1 if the tv is on and if the current volume is less than 7
    def volume_up(self):
        if self.tv_on and self.volume < 7:
            self.volume +=1
#method for decreasing the volume if the tv is on and if the current volume is greater than 1
    def volume_down(self):
        if self.tv_on and self.channel > 1:
            self.volume -= 1