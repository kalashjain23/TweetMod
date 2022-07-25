import sight_engine
import twitter_upload

while True:
    print("\nx-x-x-x-x-x-x-x-x-x\n")
    tweet = input("Enter your tweet: ")
    mod_tweet = sight_engine.text_mod(tweet)

    if(tweet == mod_tweet):
        twitter_upload.tweeting(tweet)
        print("\nYour Tweet is live!!\n")
        chance = input("Make another tweet? (y/n): ")
        if(chance.lower() == 'y' or chance.lower() == 'yes'):
            pass
        else:
            print("\nx-x-x-x-x-x-x-x-x-x\n")
            break
    else:
        print("\nYour tweet is against the guidelines. Please make appropriate tweets..!!\n")
        chance = input("Make another tweet? (y/n): ")
        if(chance.lower() == 'y' or chance.lower() == 'yes'):
            pass
        else:
            print("\nx-x-x-x-x-x-x-x-x-x\n")
            break
