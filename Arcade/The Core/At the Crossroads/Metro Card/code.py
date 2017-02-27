def metroCard(lastNumberOfDays):
    # Handle the special case for February.
    if lastNumberOfDays == 28 or lastNumberOfDays == 29:
        return [31]

    if lastNumberOfDays == 30:
        # April     => May
        # June      => July
        # September => October
        # November  => December
        return [31]

    if lastNumberOfDays == 31:
        # January  => February
        # March    => April
        # May      => June
        # July     => August
        # October  => November
        # December => January
        return [28, 30, 31]

