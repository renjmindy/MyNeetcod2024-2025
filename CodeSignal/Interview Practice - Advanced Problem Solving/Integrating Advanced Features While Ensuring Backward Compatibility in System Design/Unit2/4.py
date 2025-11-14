class SocialMediaPlatform:
    def __init__(self):
        self.posts = {}  # post_id -> {content: str, timestamp: int, likes: int, comments: []}
        self.comments = {}  # comment_id -> {content: str, timestamp: int}
        self.comment_edit_history = {}
        self.post_edit_history = {}

    def create_post(self, post_id: str, content: str, timestamp: int) -> bool:
        if post_id in self.posts:
            return False
        self.posts[post_id] = {'content': content, 'timestamp': timestamp, 'likes': 0, 'comments': []}
        return True

    def edit_post(self, post_id: str, new_content: str) -> bool:
        if post_id not in self.posts:
            return False
        self.post_edit_history.setdefault(post_id, []).append(self.posts[post_id]['content']) 
        self.posts[post_id]['content'] = new_content
        return True

    def delete_post(self, post_id: str) -> bool:
        if post_id not in self.posts:
            return False
        del self.posts[post_id]
        return True

    def like_post(self, post_id: str) -> bool:
        if post_id not in self.posts:
            return False
        self.posts[post_id]['likes'] += 1
        return True

    def top_n_liked_posts(self, n: int) -> list:
        return sorted(self.posts.keys(), key=lambda pid: (-self.posts[pid]['likes'], self.posts[pid]['timestamp']))[:n]

    def comment_on_post(self, post_id: str, comment_id: str, content: str, timestamp: int) -> bool:
        if post_id not in self.posts:
            return False
        self.comments[comment_id] = {'content': content, 'timestamp': timestamp}
        self.posts[post_id]['comments'].append(comment_id)
        return True

    def top_n_commented_posts(self, n: int) -> list:
        return sorted(self.posts.keys(), key=lambda pid: (-len(self.posts[pid]['comments']), self.posts[pid]['timestamp']))[:n]
        
    def edit_comment(self, post_id: str, comment_id: str, new_comment: str) -> bool:
        if post_id in self.posts and comment_id in self.comments:
            self.comment_edit_history.setdefault(comment_id, []).append(self.comments[comment_id]['content'])
            self.comments[comment_id]['content'] = new_comment
            return True
            
        return False
        
    def rollback_post_edit(self, post_id: str) -> bool:
        if post_id in self.posts and post_id in self.post_edit_history and len(self.post_edit_history[post_id]):
            self.posts[post_id]['content'] = self.post_edit_history[post_id][-1]
            self.post_edit_history[post_id].pop()
            return True
        return False
        
    def rollback_comment_edit(self, post_id: str, comment_id: str) -> bool:
        if post_id in self.posts and comment_id in self.comments and comment_id in self.comment_edit_history and len(self.comment_edit_history[comment_id]):
            self.comments[comment_id]['content'] = self.comment_edit_history[comment_id][-1]
            self.comment_edit_history[comment_id].pop()
            return True
        return False
    
