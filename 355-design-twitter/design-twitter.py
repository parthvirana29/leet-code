import heapq
class Twitter:

    def __init__(self):
        self.user_follows = {}
        self.user_tweets = {}
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.user_tweets:
            self.user_tweets[userId] = []
        self.timestamp += 1
        self.user_tweets[userId].append((-self.timestamp, tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        # if user has a tweet then get the list of 10 most recent tweets and add them to the heap
        if userId in self.user_tweets:
            heap.extend(self.user_tweets[userId][-10:])
        
        if userId in self.user_follows:
            for followeeId in self.user_follows[userId]:
                # follow the same technique as above. add 10 most recent tweets of all the user's followees
                if followeeId in self.user_tweets:
                    heap.extend(self.user_tweets[followeeId][-10:])
        heapq.heapify(heap)
        feed = []
        # while there is items in heap and not 10 latest posts have been found, keep popping from the heap and append the tweetId to the feed
        while (heap and len(feed) < 10):
            feed.append(heapq.heappop(heap)[1])
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.user_follows:
            self.user_follows[followerId] = set()
        if followerId != followeeId:
            self.user_follows[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.user_follows and followeeId in self.user_follows[followerId]:
            self.user_follows[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)