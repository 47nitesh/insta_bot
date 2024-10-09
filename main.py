from instabot import Bot

from PIL import Image

# Create a bot instance
bot = Bot()

# Login to your Instagram account
username = input("Enter your Instagram username: ")
password = input("Enter your Instagram password: ")
try:
    bot.login(username=username, password=password)
    print("Login successful.")
except Exception as e:
    print(f"Login failed: {e}")
    exit()

# Follow a user
user_to_follow = input("Enter the username of the user you want to follow: ")
bot.follow(user_to_follow)
print(f"Followed {user_to_follow}.")

# Like the last 'n' posts of a user
user_to_like = input("Enter the username of the user whose posts you want to like: ")
amount = int(input("How many posts do you want to like? "))
bot.like_user(user_to_like, amount=amount)
print(f"Liked {amount} posts from {user_to_like}.")

# Upload a photo
photo_to_be_upload = input("Give the path of the photo to upload: ")
upload_response = bot.upload_photo(photo_to_be_upload,caption="I love pyhton")
if upload_response:
    print("Photo uploaded successfully.")
else:
    print("Photo upload failed.")

# Comment on the last post of a user
user_to_comment = input("Enter the username of the user you want to comment on: ")
comment_text = input("Enter your comment: ")
bot.comment(user_to_comment, comment_text)
print(f"Commented on {user_to_comment}'s last post.")

# Optionally, unfollow a user
user_to_unfollow = input("Enter the username of the user you want to unfollow (or press Enter to skip): ")
if user_to_unfollow:
    bot.unfollow(user_to_unfollow)
    print(f"Unfollowed {user_to_unfollow}.")

# Logout
bot.logout()
print("Logged out successfully.")
