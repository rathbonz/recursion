def stair_climber(n):
    if n == 0:
        return 1

    elif n < 0:
        return 0

    else: 
        return stair_climber(n - 3) + stair_climber(n - 2) + stair_climber(n - 1)

print(stair_climber(3))

