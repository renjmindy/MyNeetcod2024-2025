class AlarmClock:
    def __init__(self):
        self.alarm_time = "00:00"

    def set_alarm(self, time):
        self.alarm_time = time

    def show_alarm(self):
        return self.alarm_time

# TODO: Extend the AlarmClock with a subclass EnhancedAlarmClock that supports different alarm sounds and volume levels.
# Implement methods to change the alarm sound (`set_sound`) and volume (`set_volume`),
# ensuring they accept only predefined strings for sound ("beep", "ring", "digital")
# and volume ("low", "medium", "high"). Include a method to display the current settings (`get_settings`).
class EnhancedAlarmClock(AlarmClock):
    def __init__(self, sound="beep", volume="medium"):
        super().__init__()
        self.sound = sound
        self.volume = volume
    def set_sound(self, sound):
        if not (sound == 'beep' or sound == 'ring' or sound == 'digital'):
            raise ValueError("Unsupported sound type")
        else: self.sound = sound
    def set_volume(self, volume):
        if not (volume == 'low' or volume == 'medium' or volume == 'high'):
            raise ValueError("Unsupported volume level")
        else: self.volume = volume
    def get_settings(self):
        return f"Alarm Time: {self.alarm_time}, Sound: {self.sound}, Volume: {self.volume}"
