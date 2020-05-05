import random
import time


class Remote:

    def __init__(self, tv_status="Close", tv_volume=0, channel_list=["Trt"], channel="Trt"):

        print("Creating remote class...")
        self.tv_status = tv_status
        self.tv_volume = tv_volume
        self.channel_list = channel_list
        self.channel = channel

    def volume_decrease_increase(self):

        while True:
            character = input("for the volume to decrease '<', for the volume increase '>' , and for the exit = exit ")

            if character == "<":
                if self.tv_volume != 0:  # if tv volume not equal 0
                    self.tv_volume -= 1  # then decrease the volume
                    print("Volume", self.tv_volume)
            elif character == ">":
                if self.tv_volume != 32:
                    self.tv_volume += 1
                    print("Volume", self.tv_volume)
            else:
                print("Update The Tv Volume", self.tv_volume)
                break

    def tv_close(self):
        print("Tv Shut Down")
        time.sleep(1)

        self.tv_status = "Close"

    def tv_open(self):
        time.sleep(1)
        print("Tv Opened")

        self.tv_status = "Open"

    def __str__(self):  # we can use the str method to print the Remote class in a format
        return "Tv Status : {}\nVolume : {}\nChannel : {}\nCurrent Channel : {}\n".format(self.tv_status,
                                                                                          self.tv_volume,
                                                                                          self.channel_list,
                                                                                          self.channel)

    def __len__(self):
        return len(self.channel_list)

    def random_channel(self):

        randoms = random.randint(0, len(self.channel_list) - 1)

        self.channel = self.channel_list[randoms]
        print("Current Channel:", self.channel)

    def add_channel(self, channel):
        print("Adding Channel", channel)
        self.channel_list.append(channel)

    def del_channel(self, channel):
        self.channel_list.remove(channel)
        print("Extracted Channel : ", channel)


remote = Remote()


def print_key_info():
    print("*" * 30, """
    
    Television Application
    
    1. Open the Tv
    
    2. Close the Tv
    
    3. Television Information
    
    4. Quantity of Channel
    
    5. Add Channel
    
    6. Chose the random channel
    
    7. Decrease volume or Increase volume
       for the exit click 'q'
    
    8. Channel Deletion

     """, "*" * 30)


print_key_info()

while True:

    process = input("Please choose the process : ")

    if remote.tv_status == 'Close':
        if process == '1':
            remote.tv_open()
        elif process == '2':
            print("tv already closed")
        else:
            print("Please turn on the tv")

    elif remote.tv_status == 'Open':

        if process == '1':
            print("Tv already opened")
        elif process == '2':
            remote.tv_close()
            print_key_info()
        elif process == '3':
            print(remote.__str__())
        elif process == '4':
            print("Channel list: ", len(remote))
        elif process == '5':
            channel = input("You want to add the channel separate with a comma ',' ")
            adding = channel.split(",")
            for i in adding:
                remote.add_channel(i)
            print("Updating channel list.")
        elif process == '6':
            remote.random_channel()
        elif process == "7":
            remote.volume_decrease_increase()
        elif process == "8":
            a = input("Write the name or names of the channel you want to delete : ")
            deleting = a.split(",")
            for i in deleting:
                remote.del_channel(i)
            print("Updating channel list.")
        else:
            print("Invalid Process")
