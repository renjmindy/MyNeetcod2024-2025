class Hero:
    def __init__(self, name, strength, magic, encounters):
        self._name = name
        self._strength = strength
        self._magic = magic
        self._encounters = encounters
        
class Arin(Hero):
    def adventure_journey(self):
        total_damage = 0
        for encounter in self._encounters:
            #print(encounter)
            enemy_strength, magic_barrier = encounter
            physical_damage = self._strength - enemy_strength
            magical_damage = self._magic - magic_barrier
            damage = physical_damage + magical_damage if physical_damage > 0 and magical_damage > 0 else 0
            total_damage += damage
        return total_damage
            
arin = Arin('Arin', 10, 5, [(8, 3), (12, 7), (5, 2)])

#def adventure_journey(name, strength, magic, encounters):
#    total_damage = 0
#    for encounter in encounters:
#        enemy_strength, magic_barrier = encounter
#        physical_damage = strength - enemy_strength
#        magical_damage = magic - magic_barrier
#        damage = physical_damage + magical_damage if physical_damage > 0 and magical_damage > 0 else 0
#        total_damage += damage
#    return total_damage

# Character and encounters setup
#hero_name = "Arin"
#hero_strength = 10
#hero_magic = 5
#adventure_path = [
#    (8, 3),  # Tuple format: (enemy_strength, magic_barrier)
#    (12, 7),
#    (5, 2)
#]

# Calculating the journey's outcome
#journey_damage = adventure_journey(hero_name, hero_strength, hero_magic, adventure_path)
print(f"{hero_name} dealt a total of {arin.adventure_journey()} damage during the adventure!")
