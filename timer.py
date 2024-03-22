def pad(s):
    digits = s
    if len(digits) == 1:
        digits = '0' + digits

    return digits

class Timer:
    def __init__(self, hr = 0, mn = 0, sec = 0):
        self.__hr = hr
        self.__mn = mn
        self.__sec = sec

    def __str__(self):
        return pad(str(self.__hr)) + ":" + pad(str(self.__mn)) + ":" + pad(str(self.__sec))


    def next_second(self):
        if self.__sec == 59:
            self.__sec = 00
            if self.__mn == 59:
                self.__mn = 00
                if self.__hr == 23:
                    self.__hr = 00
                else:
                    self.__hr += 1
            else:
                self.__mn += 1
        else:
            self.__sec +=1


    def prev_second(self):
        if pad(str(self.__sec)) == "00":
            self.__sec = 59
            if pad(str(self.__mn)) == "00":
                self.__mn = 59
                if pad(str(self.__hr)) == "00":
                    self.__hr = 23
                else:
                    self.__hr -= 1
            else:
                self.__mn -= 1
        else:
            self.__sec -= 1


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
