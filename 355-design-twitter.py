class Twitter:

    def __init__(self):
        self.counter = itertools.count(step = -1)
        self.tweets = collections.defaultdict(list)
        self.followers = collections.defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        # append to list is amortized O(1)
        self.tweets[userId].append((next(self.counter), tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        # max(O(users^2) or O(tweets) or O(log(tweets)))
        tweets = []
        names = [userId]
        for key in self.followers:
            if userId in self.followers[key]:
                names.append(key)
        for name in names:
            for t in self.tweets[name]:
                heapq.heappush(tweets, t)
        top10 = []
        while len(top10) < 10 and tweets:
            top10.append(heapq.heappop(tweets)[1])
        return top10
        
        
    def follow(self, followerId: int, followeeId: int) -> None:
        # followerID starts following followee ID
        # Adding to hashmap is O(1)
        self.followers[followeeId].add(followerId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # followerID stops following followeeID
        # set().discard raises no error if DNE
        # set().remove() raises error if DNE
        # python & jave sets under the hood use hashmaps O(1)
        self.followers[followeeId].discard(followerId)



# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)