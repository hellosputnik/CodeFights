def growingPlant(upSpeed, downSpeed, desiredHeight):
    return desiredHeight / (upSpeed - downSpeed) if upSpeed < desiredHeight else 1

