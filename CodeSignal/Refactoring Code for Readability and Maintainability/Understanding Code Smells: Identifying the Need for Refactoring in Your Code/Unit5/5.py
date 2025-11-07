class Player:
    def __init__(self, level):
        self._level = level
        
class Challenge(Player):
    def __init__(self, player):
        pass
        
class Puzzle(Challenge):
    def __init__(self, difficulty):
        self._difficulty = difficulty
    def calculate_total_points(self, player):
        return max(0, player._level - self._difficulty)
        
class Battle(Challenge):
    def __init__ (self, enemy_power):
        self._enemy_power = enemy_power
    def calculate_total_points(self, player):
        if player._level > self._enemy_power:
            return player._level - self._enemy_power
        else:
            return 0

#def calculate_total_points(player_level, challenges):
#    total_points = 0
#    for challenge in challenges:
#        if challenge['type'] == 'puzzle':
#            difficulty = challenge['difficulty']
#            total_points += max(0, player_level - difficulty)
#        elif challenge['type'] == 'battle':
#            enemy_power = challenge['enemy_power']
#            if player_level > enemy_power:
#                total_points += player_level - enemy_power
#            else:
#                total_points += 0
#    return total_points

player_level = 75
challenges = [
    {'type': 'puzzle', 'difficulty': 50},
    {'type': 'battle', 'enemy_power': 70},
    {'type': 'puzzle', 'difficulty': 60},
    {'type': 'battle', 'enemy_power': 80}
]

player = Player(75)
challenge = Challenge(player)

adventure_points = 0
for cha in challenges:
    if cha['type'] == 'puzzle':
        puzzle = Puzzle(cha['difficulty'])
        adventure_points += puzzle.calculate_total_points(player)
    elif cha['type'] == 'battle':
        battle = Battle(cha['enemy_power'])
        adventure_points += battle.calculate_total_points(player)

#adventure_points = calculate_total_points(player_level, challenges)
print(f"Total Points Earned: {adventure_points}")
