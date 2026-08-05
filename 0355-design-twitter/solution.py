class Twitter:

    def __init__(self):
        self.tweets = []
        self.adjacency_list = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append((userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = self.tweets
        following = self.adjacency_list[userId]

        result = []
        append = result.append

        for i in range(len(tweets) - 1, -1, -1):
            author, tweet = tweets[i]

            if author == userId or author in following:
                append(tweet)
                if len(result) == 10:
                    break

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.adjacency_list[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.adjacency_list[followerId].discard(followeeId)
