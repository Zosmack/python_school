from operator import truediv
import player


def finish():
    if (playerOne.player.live == 0):
        return True
    if (playerTwo.player.live == 0):
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
    if (play):
        playerOne.player.attack()
        print("one")
        play = False
    else:
        print("two")
        play = False
    break  # noch entfernen
