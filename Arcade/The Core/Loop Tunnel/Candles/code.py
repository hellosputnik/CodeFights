def candles(candlesNumber, makeNew):
    leftovers = 0
    total     = 0

    while candlesNumber or leftovers >= makeNew:
        leftovers += candlesNumber
        total     += candlesNumber

        candlesNumber = leftovers / makeNew
        leftovers     = leftovers % makeNew

    return total

