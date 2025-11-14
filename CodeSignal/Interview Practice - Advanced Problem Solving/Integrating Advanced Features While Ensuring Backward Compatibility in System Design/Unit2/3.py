class NoteTakingApp:
    def __init__(self):
        self.notes = {}
        self.tags = {}
        self.shares = {}
        self.versions = {}

    def add_note(self, title: str, content: str) -> str:
        note_id = str(len(self.notes) + 1)
        self.notes[note_id] = {"title": title, "content": content, "tags": []}
        return note_id

    def get_note(self, note_id: str) -> dict:
        if note_id in self.notes:
            return {"title": self.notes[note_id]["title"], "content": self.notes[note_id]["content"]}
        return None

    def add_tag(self, note_id: str, tag: str) -> bool:
        if note_id in self.notes:
            self.notes[note_id]["tags"].append(tag)
            if tag in self.tags:
                self.tags[tag].append(note_id)
            else:
                self.tags[tag] = [note_id]
            return True
        return False

    def get_notes_by_tag(self, tag: str) -> list:
        if tag in self.tags:
            return [{"note_id": note_id, "title": self.notes[note_id]["title"], "content": self.notes[note_id]["content"]} for note_id in self.tags[tag]]
        return []

    def share_note(self, note_id: str, user_id: str, access_level: str) -> bool:
        if note_id in self.notes and access_level in ["read", "write"]:
            if note_id not in self.shares:
                self.shares[note_id] = {}
            self.shares[note_id][user_id] = access_level
            return True
        return False

    def get_shared_notes(self, user_id: str) -> list:
        result = []
        for note_id, users in self.shares.items():
            if user_id in users:
                access_level = users[user_id]
                result.append({"note_id": note_id, "title": self.notes[note_id]["title"], "content": self.notes[note_id]["content"], "access_level": access_level})
        return result
        
    def add_version(self, note_id: str, title: str, content: str, tags: list) -> bool:
        if note_id in self.notes:
            if title != self.notes[note_id]['title'] or content != self.notes[note_id]['content'] or tags != self.notes[note_id]['tags']:
            
                self.versions.setdefault(note_id, []).append({"title": self.notes[note_id]['title'], "content": self.notes[note_id]['content'], "tags": self.notes[note_id]['tags'].copy()})
                
                self.notes[note_id]['title'] = title
                self.notes[note_id]['content'] = content
                self.notes[note_id]['tags'] = tags
                
            return True
            
        return False
        
    def undo_version(self, note_id: str) -> bool:
        if note_id in self.versions:
            self.notes[note_id]['title'] = self.versions[note_id][-1]['title']
            self.notes[note_id]['content'] = self.versions[note_id][-1]['content']
            self.notes[note_id]['tags'] = self.versions[note_id][-1]['tags']
            self.versions[note_id].pop()
            return True
            
        return False
