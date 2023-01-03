def all_combinations(playernumber):
    for player1 in range(1, playernumber+1):
        for player2 in range(player1+1, playernumber+1):
            print("Player", player1, "vs.", player2)


all_combinations(3)
