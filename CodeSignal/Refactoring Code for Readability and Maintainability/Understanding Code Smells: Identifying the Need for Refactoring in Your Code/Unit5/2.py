class Player:
    def __init__(self, name, power):
        self.name = name
        self.power = power

class Monster:
    def __init__(self, score=0, impact=0, monster=0):
        self.score = score
        self.impact = impact
        self.monter = monster
    def score_change(self, player):
        pass
    def compute_game_score(self):
        pass
    def calculate_total_impact(self, player):
        pass
        
class Orc(Monster):
    def __init__(self, score=0, impact=0, strength=0):
        self.score = score
        self.impact = impact
        self.strength = strength
    def score_change(self, player):
        if player.power > self.strength:
            return player.power - self.strength
        else:
            return self.strength - player.power
    def compute_game_score(self):
        self.score += self.score_change(player)
        return self.score
    def calculate_total_impact(self):
        if player.power > self.strength:
            self.impact += player.power - self.strength
        else:
            self.impact -= self.strength - player.power
        return self.impact
        
class Dragon(Monster):
    def __init__(self, score=0, impact=0, toughness=0):
        self.score = score
        self.impact = impact
        self.toughness = toughness
    def score_change(self, player):
        if player.power > self.toughness:
            return player.power - self.toughness
        else:
            return self.toughness - player.power
    def compute_game_score(self):
        self.score += self.score_change(player)
        return self.score
    def calculate_total_impact(self):
        if player.power > self.toughness:
            self.impact += (player.power - self.toughness * 2)
        else:
            self.impact -= (self.toughness * 2 - player.power)
        return self.impact

#    def score_change(self, monster):
#        if self.power > monster:
#            return self.power - monster
#        else:
#            return monster - self.power
        
#    def compute_game_score(self):
#        score = 0
#        for monster in self.monsters:
#            if monster['type'] == 'orc':
#                score += self.score_change(monster['strength'])
#            elif monster['type'] == 'dragon':
#                score += self.score_change(monster['toughness'])
#        return score

#    def calculate_total_impact(self):
#        total_impact = 0
#        for monster in self.monsters:
            # Each monster is now a dictionary with 'type' and 'strength' or 'toughness' key
#            if monster['type'] == 'orc':
#                if self.power > monster['strength']:
#                    total_impact += self.power - monster['strength']
#                else:
#                    total_impact -= monster['strength'] - self.power
#            elif monster['type'] == 'dragon':
#                if self.power > monster['toughness']:
#                    total_impact += (self.power - monster['toughness'] * 2)
#                else:
#                    total_impact -= (monster['toughness'] * 2 - self.power)
#        return total_impact


# Example usage
player = Player("John", 120)
monsters = [{'type': 'orc', 'strength': 100}, {'type': 'dragon', 'toughness': 150}, {'type': 'orc', 'strength': 80}]
monster_list = [Orc(0, 0, 100), Dragon(0, 0, 150), Orc(0, 0, 80)]

total_score, total_impact = 0, 0
for monster in monster_list:
    monster.score_change(player)
    total_score += monster.compute_game_score()
    total_impact += monster.calculate_total_impact()

#total_impact = player.calculate_total_impact()
print(f"Total Combat Impact: {total_impact}")
