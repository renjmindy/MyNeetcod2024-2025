class Player:
    def __init__(self, name, level):
        self._name = name
        self._level = level
        
class Challenge(Player):
    def __init__(self, name, level):
        self._name = name
        self._difficulty = level
    def calculate_total_adventure_score(self, player):
        
        if player._level >= self._difficulty:
            return player._level - self._difficulty
        else: return -1

#def calculate_total_adventure_score(player_info, challenges_info):
#    total_score = 0
#    for challenge in challenges_info:
#        challenge_level = challenge['difficulty']
#        player_level = player_info['level']
        # Inline calculation for individual challenge score
#        if player_level >= challenge_level:
#            total_score += player_level - challenge_level
#        else:
#            total_score -= 1  # Penalizing for challenges that are too hard
    # Ensuring the total score doesn't go below zero
#    total_score = max(total_score, 0)
#    return total_score

# Representing the player and challenges with dictionaries
player = {'name': 'Eldric', 'level': 25}
challenges = [
    {'name': 'Cave of Shadows', 'difficulty': 20},
    {'name': 'The Enchanted Forest', 'difficulty': 15},
    {'name': 'Dark Abyss', 'difficulty': 30}
]

person = Player(player['name'], player['level'])
final_score = 0
for challenge in challenges:
    cha = Challenge(challenge['name'], challenge['difficulty'])
    final_score += cha.calculate_total_adventure_score(person)

# Inline calls and calculations
#final_score = calculate_total_adventure_score(player, challenges)
print(f"Final Adventure Score for {player['name']}: {final_score}")
