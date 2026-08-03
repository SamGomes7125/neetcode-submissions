class Twitter:

    def __init__(self):
        self.followers = {}
        self.tweets = {}
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp += 1
        if userId not in self.tweets:
            self.tweets[userId] = [(self.timestamp, tweetId)]
        else:
            self.tweets[userId].append((self.timestamp, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        news = []
        maxHeap = []

        # Ensure follower set exists and user follows themselves
        if userId not in self.followers:
            self.followers[userId] = set()
        self.followers[userId].add(userId)

        # 1. Grab the latest tweet from each followee
        for followeeId in self.followers[userId]:
            if followeeId in self.tweets and len(self.tweets[followeeId]) > 0:
                index = len(self.tweets[followeeId]) - 1
                count, tweetId = self.tweets[followeeId][index]
                heapq.heappush(maxHeap, (-count, tweetId, followeeId, index - 1))

        # 2. Extract top 10 most recent tweets across all followees
        while maxHeap and len(news) < 10:
            neg_count, tweetId, followeeId, next_index = heapq.heappop(maxHeap)
            news.append(tweetId)
            
            if next_index >= 0:
                count, prev_tweetId = self.tweets[followeeId][next_index]
                heapq.heappush(maxHeap, (-count, prev_tweetId, followeeId, next_index - 1))

        return news

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followers:
            self.followers[followerId] = set()
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followers or followerId == followeeId:
            return 
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)