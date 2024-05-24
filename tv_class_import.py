#add a method for importing class variables
from tv import TV
def main():
    #instances of tv class
    tv1 = TV()
    tv2 = TV()
#add a operation for tv1
    tv1.turn_on() #for turning on the tv
    tv1.set_channel(30) #for setting the channel to channel 30
    tv1.set_volume(3) #for setting the volume to volume 3
    print(f"TV1's channel is {tv1.get_channel()}\nTV1's the volume is {tv1.get_volume()}")
if __name__ == "__main__":
    main()
#add a operation for tv2