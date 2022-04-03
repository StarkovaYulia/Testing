class mirrorClock:

    def __init__(self):
        pass

    def count_time(self, time_in_mirror):
        allTime = 720

        time_in_mirror = list(map(lambda x: int(x), time_in_mirror.split(":")))
        minutes_in_mirrors = time_in_mirror[0] * 60 + time_in_mirror[1]

        if time_in_mirror[0] < 12 and time_in_mirror[0] != 11:
            real_minutes = allTime - minutes_in_mirrors
            hours = str(real_minutes // 60)
            minutes = str(real_minutes % 60)

            if hours == "0":
                hours = "11"

            if len(hours) == 1:
                hours = "0" + hours

            if len(minutes) == 1:
                minutes = "0" + minutes

            return hours + ":" + minutes

        elif time_in_mirror[0] == 11:

            if time_in_mirror[0] == 11 and time_in_mirror[1] == 0:
                return "01:00"

            minutes = str(60 - time_in_mirror[1])

            if len(minutes) == 1:
                minutes = "0" + minutes
            return "12:" + minutes

        elif time_in_mirror[0] == 12:
            if time_in_mirror[1] == 0:
                return "12:00"
            else:
                minutes = str(60 - time_in_mirror[1])
                if len(minutes) == 1:
                    minutes = "0" + minutes
                return "11:" + minutes

    def check_string(self, time):
        time = time.strip()
        legalSymbols = "0123456789:"

        newTime = ""
        for symbol in time:
            if symbol != " " and (symbol not in legalSymbols):
                return None
            elif symbol != " ":
                newTime += symbol

        time = newTime
        if len(time) != 5 or time.find(":", 0) == -1:
            return None

        hours = int(time[0] + time[1])
        minutes = int(time[3] + time[4])

        if hours < 1 or hours > 12:
            return None
        if minutes < 0 or minutes > 59:
            return None

        return time


    def what_is_the_time(self, time_in_mirror=None):

        if time_in_mirror is None or time_in_mirror == "":
            return ""

        if not isinstance(time_in_mirror, str):
            raise ValueError

        if time_in_mirror.isspace():
            raise ValueError

        time_in_mirror = self.check_string(time_in_mirror)
        if time_in_mirror:
            return self.count_time(time_in_mirror)
        else:
            raise ValueError

if __name__ == "__main__":
    clock = mirrorClock()
    mirrorTime = "11:40"
    print(clock.what_is_the_time(mirrorTime))
    pass
