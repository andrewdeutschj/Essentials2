class WeekDayError(Exception):
    pass


class Weeker:
    daylist = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

    def __init__(self, day):
        if day not in Weeker.daylist:
            raise WeekDayError
        self.__day = day


    def __str__(self):
        return self.__day


    def add_days(self, n):
        self.__daynbr = Weeker.daylist.index(self.__day)
        self.__newdaynbr = (self.__daynbr + n) % 7
        self.__day = Weeker.daylist[self.__newdaynbr]
        self.__daynbr = Weeker.daylist.index(self.__day)


    def subtract_days(self, n):
        self.__newdaynbr = (n - self.__daynbr) % 7
        self.__day = Weeker.daylist[self.__newdaynbr]


try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")
