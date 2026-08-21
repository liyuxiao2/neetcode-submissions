class Twitter:
    # each user will have their own heap 
    # store a hash set, for every user (id : list[followed])
    # another for (id: list[followers])

    #when a user posts a tweet, we first check the hash set, and go through their list of followers, pushing every element onto their heap

    
    def __init__(self):
        self.followed = defaultdict(set) # id : list[int]
        self.feed = defaultdict(list) #id : list[count, heapid]
        self.time = 0

        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.feed[userId].append([self.time, tweetId])
        self.time -= 1
        
        

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minH = []

        self.followed[userId].add(userId)
        for followeeId in self.followed[userId]:
            if followeeId in self.feed:
                index = len(self.feed[followeeId]) - 1
                count, tId = self.feed[followeeId][index]
                heapq.heappush(minH, [count, tId, followeeId, index - 1])
        
        while minH and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minH)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.feed[followeeId][index]
                heapq.heappush(minH, [count, tweetId, followeeId, index - 1])
        return res
        
    
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followed[followerId].add(followeeId)
        
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followed[followerId]:
            self.followed[followerId].remove(followeeId)
