# https://leetcode.com/problems/design-browser-history/

# https://leetcode.com/submissions/detail/442388681/
# 01/12/2021 23:58  

class BrowserHistory:

    def __init__(self, homepage: str):
        self.timeline = [homepage]
        self.curr = 0

    def visit(self, url: str) -> None:
        if self.curr == len(self.timeline) - 1:
            self.timeline.append(url)
            self.curr += 1
        else:
            self.timeline = self.timeline[:self.curr + 1]
            self.timeline.append(url)
            self.curr += 1

    def back(self, steps: int) -> str:
        if steps > self.curr:
            self.curr = 0
            return self.timeline[0]
        self.curr -= steps
        return self.timeline[self.curr]

    def forward(self, steps: int) -> str:
        if steps + self.curr >= len(self.timeline):
            self.curr = len(self.timeline) - 1
            return self.timeline[-1]
        self.curr += steps
        return self.timeline[self.curr]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)