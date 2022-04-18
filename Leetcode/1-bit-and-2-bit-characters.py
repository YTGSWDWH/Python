def isOneBitCharacter(bits):
    pr = 0
    while pr < len(bits)-1:
        if bits[pr] == 0:
            pr = pr + 1
        else:
            pr = pr + 2
    if pr == len(bits):
        return False
    else:
        return True