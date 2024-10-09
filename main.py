from instabot import Bot

# Create a bot instance
bot = Bot()

# Login to your Instagram account
bot.login(username="your_username", password="your_password")

# Follow a user
bot.follow("user_to_follow")

# Like the last 5 posts of a user
bot.like_user("user_to_like", amount=5)

# Optionally, you can also unfollow users
bot.unfollow("user_to_unfollow")

# Logout
bot.logout()
