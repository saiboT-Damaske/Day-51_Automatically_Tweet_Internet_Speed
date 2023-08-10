from internet_speed_twitter_bot import InternetSpeedTwitterBot

USERNAME = ''
PASSWORD = ''
DOWN_SPEED = 150
UP_SPEED = 20



# -------------
speed_bot = InternetSpeedTwitterBot()
speed_bot.get_internet_speed()
speed_bot.tweet_at_provider(username=USERNAME, password=PASSWORD, down_speed=DOWN_SPEED, up_speed=UP_SPEED)

