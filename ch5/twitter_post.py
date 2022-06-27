import tweepy

# 트위터 API 인증 정보 작성 --- (1)
api_key = '자신의 인증 정보'
api_secret = '자신의 인증 정보'
access_token = '자신의 인증 정보'
access_secret = '자신의 인증 정보'
        
# 트위터 객체 생성 --- (2)
auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

# 트윗을 게시 --- (3)
api.update_status('Python으로 트윗 업로드하기')

