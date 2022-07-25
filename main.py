from tkinter import *
from tkinter.font import BOLD
import sight_engine
import twitter_upload
import tkinter.messagebox as msg
from PIL import ImageTk,Image

turn = False
root = Tk()
root.title('Tweet Moderator')
root.geometry("700x500")
root.iconbitmap(r'.\icon.ico')


class Tweet_Modulation:

    def __init__(self,root):
        self.img = ImageTk.PhotoImage(Image.open(r".\twitter.png"))
        self.twitter_img = Label(image=self.img)
        self.twitter_img.place(anchor=CENTER, relx=0.5, rely=0.15)

        self.text = Label(root, text = 'Tweee..Tweee..Tweeeettt..!!!', font = ('Courier', 15, 'bold'), fg='DeepSkyBlue2').place(anchor=CENTER, relx=0.5, rely=0.3)

        self.entry_field = StringVar()
        self.entryfield = Entry(root, textvariable=self.entry_field, bg = 'lightcyan').place(anchor=CENTER, rely=0.60, relx=0.50,height=250, width=300)

        self.tweet_button = Button(root, text = 'Tweet',width=8, command=self.tweet_moderation(self.entry_field.get()), fg='white', bg='DeepSkyBlue2', font=('Calibri',12,'bold'))
        self.tweet_button.place(anchor=CENTER, relx=0.4, rely=0.9)

        self.exit_button = Button(root, text = 'Exit...', command= root.destroy, width=8, fg='white', bg='DeepSkyBlue2', font=('Calibri',12,'bold')).place(anchor=CENTER, relx=0.6, rely=0.9)

    def tweet_moderation(self,tweet):
        global turn
        if tweet == '' and turn:
            msg.showinfo('Empty tweet..', 'Type something to tweet!!')
        else:
            turn = True
            self.mod_tweet = sight_engine.text_mod(tweet)
            self.post_on_twitter(tweet, self.mod_tweet)

    def post_on_twitter(self, tweet, mod_tweet):
        if tweet == mod_tweet:
            twitter_upload.tweeting(tweet)
            msg.showinfo('Success!', 'Tweet has been posted successfully!!')
            self.__init__(root) 
        else:
            msg.showinfo('Oopsie!', 'Not a good thing to post on Twitter!!')
            self.__init__(root)

calling = Tweet_Modulation(root)

root.mainloop()