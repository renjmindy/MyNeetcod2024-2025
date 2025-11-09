class FitnessTrackingSystem:
    def __init__(self):
        self.users = {}
        self.scheduled_events = {}

    def add_activity(self, user_id: str, activity_type: str, distance: int) -> bool:
        if user_id not in self.users:
            self.users[user_id] = {}
        if activity_type in self.users[user_id] or distance < 0:
            return False
        self.users[user_id][activity_type] = distance
        
        total_distance = 0
        if user_id in self.scheduled_events:
            for event in self.scheduled_events[user_id]:
                if event['activity_type'] == activity_type:
                    total_distance += event['distance']
        
            self.users[user_id][activity_type] += total_distance
                    
        return True

    def update_activity(self, user_id: str, activity_type: str, distance: int) -> bool:
        if user_id in self.users and activity_type in self.users[user_id]:
            self.users[user_id][activity_type] += distance
            return True
        return False

    def get_activity(self, user_id: str, activity_type: str) -> int:
        if user_id in self.users and activity_type in self.users[user_id]:
            return self.users[user_id][activity_type]
        return None

    def activity_summary(self, user_id: str) -> dict:
        if user_id in self.users:
            return self.users[user_id]
        return None
        
    def schedule_event(self, timestamp: int, user_id: str, activity_type: str, distance: int, event_time: int) -> bool:
        if event_time < timestamp: return False
        
        self.scheduled_events.setdefault(user_id, []).append({
            "activity_type": activity_type, 
            "distance": distance, 
            "event_time": event_time
        })
        return True
        
    def get_agenda(self, user_id: str, from_time: int, to_time: int) -> list:
        agenda = []
        for event in self.scheduled_events[user_id]:
            if event['event_time'] >= from_time and event['event_time'] <= to_time:
                agenda.append(event)
                
        agenda = sorted(agenda, key=lambda x:x['event_time'])
        
        return agenda
