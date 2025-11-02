class Player:
    def __init__(self, name, power, monsters):
        self.name = name
        self.power = power
        self.monsters = monsters

    def score_change(self, monster):
        if self.power > monster:
            return self.power - monster
        else:
            return monster - self.power
        
    def compute_game_score(self):
        score = 0
        for monster in self.monsters:
            if monster['type'] == 'orc':
                score += self.score_change(monster['strength'])
            elif monster['type'] == 'dragon':
                score += self.score_change(monster['toughness'])
        return score

    def calculate_total_impact(self):
        total_impact = 0
        for monster in self.monsters:
            # Each monster is now a dictionary with 'type' and 'strength' or 'toughness' key
            if monster['type'] == 'orc':
                if self.power > monster['strength']:
                    total_impact += self.power - monster['strength']
                else:
                    total_impact -= monster['strength'] - self.power
            elif monster['type'] == 'dragon':
                if self.power > monster['toughness']:
                    total_impact += (self.power - monster['toughness'] * 2)
                else:
                    total_impact -= (monster['toughness'] * 2 - self.power)
        return total_impact

# Example usage
monsters = [{'type': 'orc', 'strength': 100}, {'type': 'dragon', 'toughness': 150}, {'type': 'orc', 'strength': 80}]
player = Player("John", 120, monsters)

total_impact = player.calculate_total_impact()
print(f"Total Combat Impact: {total_impact}")
