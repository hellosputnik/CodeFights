def validTime(time):
    HH, MM = map(int, time.split(":"))

    return HH < 24 and MM < 60

