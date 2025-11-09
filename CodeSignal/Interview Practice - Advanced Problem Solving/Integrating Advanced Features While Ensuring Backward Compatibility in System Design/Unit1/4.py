class SocialMedia:

    def __init__(self):
        self.posts = {}
        self.user_reactions = {}
        self.groups = {}
        self.group_posts = {}

    def create_post(self, post_id: str, content: str) -> bool:
        if post_id in self.posts:
            return False
        self.posts[post_id] = {'content': content, 'reactions': {}}
        return True

    def delete_post(self, post_id: str) -> bool:
        if post_id not in self.posts:
            return False
        del self.posts[post_id]
        return True

    def react_to_post(self, user_id: str, post_id: str, reaction_type: str) -> bool:
        if post_id not in self.posts or user_id in self.user_reactions.get(post_id, {}):
            return False
        reactions = self.posts[post_id]['reactions']
        reactions[reaction_type] = reactions.get(reaction_type, 0) + 1
        self.user_reactions.setdefault(post_id, {})[user_id] = reaction_type
        return True

    def get_reaction_summary(self, post_id: str):
        if post_id not in self.posts:
            return None
        return self.posts[post_id]['reactions'].copy()
        
    def create_group(self, group_id: str, operator_id: str) -> bool:
        if group_id in self.groups: return False
        self.groups[group_id] = {"operator": operator_id, "members": [operator_id]}
        #self.groups.setdefault(group_id, {"operator": operator_id, "members": [operator_id]})
        return True
        
    def add_member(self, group_id: str, user_id: str, operator_id: str) -> bool:
        if group_id in self.groups and self.groups[group_id]['operator'] == operator_id and user_id not in self.groups[group_id]['members']:
            self.groups[group_id]['members'].append(user_id)
            return True
        else: return False
        
    def share_post_to_group(self, post_id: str, group_id: str, user_id: str) -> bool:
        if post_id in self.posts and group_id in self.groups and user_id in self.groups[group_id]['members']:
            self.group_posts.setdefault(group_id, []).append(post_id)
            return True
        return False
        
    def get_group_posts(self, group_id: str) -> list[str]:
        if group_id in self.group_posts:
            return self.group_posts[group_id].copy()
        else: return None
