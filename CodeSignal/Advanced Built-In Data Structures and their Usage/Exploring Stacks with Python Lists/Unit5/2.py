from collections import deque

class BrowserHistory:
    def __init__(self):
        # TODO: Initialize two deques, one for history and one for future navigations
        self.history = deque()
        self.future = deque()
    
    def visit(self, url):
        # TODO: Add the visited URL to the history and clear the future
        self.history.append(url)
        if self.future: self.future.clear()
    
    def back(self, steps):
        # TODO: Move the specified number of steps back in the history, if possible, and update the future accordingly
        for i in range(steps):
            if self.history:
                url_history = self.history.pop()
                self.future.append(url_history)
            else: break
    
    def forward(self, steps):
        # TODO: Move the specified number of steps forward in the history, if possible, and update the history accordingly
        for i in range(steps):
            if self.future:
                url_future = self.future.popleft()
                self.history.append(url_future)
            else: break
        
# TODO: Use the BrowserHistory class to simulate visiting some URLs, then going back and forward in the history
uList = ['a.com', 'b.com', 'c.com']
browser = BrowserHistory()
for u in uList: browser.visit(u)
print(browser.history)
browser.back(3)
print(browser.history)
browser.forward(2)
print(browser.history)
print(browser.future)
