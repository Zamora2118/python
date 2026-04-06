class Television:
    '''
    This is the main part that will end up controlling the power, volume, mute, and channels
    '''
    MIN_VOLUME =0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        '''
        The following below are the TV's default values as power is off, not muted, min volume, and min channel
        '''
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self):
        '''
        This turns the TV on or off
        :return:
        '''
        self.__status = not self.__status

    def mute(self):
        '''
        This turns the mute on or off if the TV is on
        :return:
        '''
        if self.__status:
            self.__muted = not self.__muted
    def channel_up(self):
        '''
        This turns the channel up by 1 and also wraps if its at max
        :return:
        '''
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self):
        '''
        This turns the channel down by 1 and also wraps if its at min
        :return:
        '''
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self):
        '''
        This turns the volume up by 1 and also wraps to the min if its at max
        :return:
        '''
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self):
        '''
        This turns the volume down by 1 and also wraps to the max if its at min
        :return:
        '''
        if self.__status:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self: str) -> str:
        '''
        This method will return a string representation of the object
        :return: string with the power, channel, volume
        '''
        if self.__muted:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
