#add a method for importing class variables
from tv import TV
def main():
    #instances of tv class
    tv1 = TV()
    tv2 = TV()
#add a operation for TV1
    tv1.turn_on() #for turning on the TV
    tv1.set_channel(30) #for setting the channel to channel 30
    tv1.set_volume(3) #for setting the volume to volume 3
#add a operation for TV2
    tv2.turn_on() #for turning on the TV
    tv2.set_channel(3) #for setting the channel to channel 3
    tv2.set_volume(2) #for setting the volume to volume 2

    print(f"TV1's channel is {tv1.get_channel()}\nTV1's the volume is {tv1.get_volume()}") #for printing the channel and volume for TV1
    print(f"TV2's channel is {tv2.get_channel()}\nTV2's the volume is {tv2.get_volume()}") #for printing the channel and volume for TV2
if __name__ == "__main__":
    main()
