from operator import truediv
import player


def finish():
    if (playerOne.player.live <= 0):
        return True
    if (playerTwo.player.live <= 0):
        return True
    return False


# Game
print("Player One:")
playerOne = player.Player()
playerOne.chose()

print("Player Two:")
playerTwo = player.Player()
playerTwo.chose()

play = False
if (playerOne.player.initiative > playerTwo.player.initiative):
    play = True

while (finish() == False):
    print()
    print("PlayerOne:")
    playerOne.player.printData()
    print()
    print("PlayerTwo:")
    playerTwo.player.printData()
    print()
    if (play):
        print("PlayerOne Attack:")
        playerTwo.player.getDamage(playerOne.player.attack())
        play = False
    else:
        print("PlayerTwo Attack:")
        playerOne.player.getDamage(playerTwo.player.attack())
        play = True
