from sortedcontainers import SortedDict

class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    # TODO: Add the missing method to compare two Player objects based on their score.
    def __lt__(self, other):
        return (self.score, self.name) < (other.score, other.name)

    def __gt__(self, other):
        return (self.score, self.name) > (other.score, other.name)

    # TODO: Also, remember to define how two Player objects are checked for equality.
    def __eq__(self, other):
        return (self.score, self.name) == (other.score, other.name)

    def __ne__(self, other):
        return (self.score, self.name) != (other.score, other.name)
    
    def __hash__(self):
        return hash((self.name, self.score))

tournament = SortedDict()
# TODO: Add two Player objects to the tournament. Use name as 'Amy' with score 87 and 'Brad' with score 75. Assign them placements accordingly.
tournament[Player('Amy', 87)] = 1
tournament[Player('Brad', 75)] = 2

# Your code here to print the players' details
for player in tournament:
    print(f"{player.name} gets score {player.score}, ranked: {tournament[player]}")
