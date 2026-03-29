class User:
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.name = user_name
        self.followers = 0
        self.following = 0
        print(f"User created with name {self.name.title()} having {self.followers} followers.")

    def follow(self, user):
        user.followers += 1
        self.following +=1


user1 = User("025", "user1")

user2 = User("036", "user2")

user3 = User("052", "user3")

user2.follow(user1)
user1.follow(user2)
user3.follow(user1)

print(user2.followers)
print(user2.following)
print(user1.followers)
print(user1.following)
