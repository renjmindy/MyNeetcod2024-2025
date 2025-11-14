class EmailSystem:
    def __init__(self):
        self.inboxes = {}  # Stores the emails in user inboxes.
        self.sent_counts = {}  # Counts the sent emails by each user.
        self.sent_emails = {}  # Keeps a record of all sent emails for undo functionality.
        self.users = set()

    def send_email(self, from_user: str, to_user: str, subject: str, body: str) -> bool:
        if from_user in self.users or to_user in self.users: return False
        if to_user not in self.inboxes:
            self.inboxes[to_user] = []
        # Add the email to the recipient's inbox
        self.inboxes[to_user].append({"from": from_user, "subject": subject, "body": body})
        # Increment sent email count
        self.sent_counts[from_user] = self.sent_counts.get(from_user, 0) + 1
        # Record the email in sent_emails for undo functionality
        if from_user not in self.sent_emails:
            self.sent_emails[from_user] = []
        self.sent_emails[from_user].append({"to_user": to_user, "subject": subject, "body": body})
        return True

    def query_inbox(self, user: str) -> list:
        return self.inboxes.get(user, [])

    def sent_emails_count(self) -> dict:
        return self.sent_counts

    def flag_email(self, user: str, subject: str) -> bool:
        if user in self.inboxes:
            for email in self.inboxes[user]:
                if email['subject'] == subject:
                    email['flagged'] = True  # Assuming the email dictionary has a flagged property
                    return True
        return False
        
    def undo_send(self, from_user: str, subject: str) -> bool:
        if from_user in self.sent_emails:
            for i in range(len(self.sent_emails[from_user]) - 1, -1, -1):
                if self.sent_emails[from_user][i]['subject'] == subject:
                    for j in range(len(self.inboxes[self.sent_emails[from_user][i]['to_user']])):
                        if self.inboxes[self.sent_emails[from_user][i]['to_user']][j]['from'] == from_user:
                            self.inboxes[self.sent_emails[from_user][i]['to_user']].pop(j)
                            self.sent_counts[from_user] -= 1
                            if self.sent_counts[from_user] == 0: del self.sent_counts[from_user]
                            self.sent_emails[from_user].pop(i)
                            return True
        return False
                
    def logout_user(self, user: str) -> bool:
        self.users.add(user)
        return True
