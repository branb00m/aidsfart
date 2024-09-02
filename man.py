import instagrapi

client = instagrapi.Client()

while True:
    user_login = input('Enter your account username: ')
    password_login = input('Enter your password login: ')

    if not user_login or len(user_login) < 2:
        print('User login is empty')
        continue

    if not password_login or len(password_login) == 0:
        print('Password login is empty!')
        continue

    logged_in = client.login(user_login, password_login)
    if logged_in is False:
        print('There was trouble logging in!')
        continue

    following = {v.username: k for k, v in client.user_following(client.user_id).items()}
    followers = {v.username: k for k, v in client.user_followers(client.user_id).items()}

    for _following in following:
        if _following not in followers:
            print(_following)

    del following
    del followers
