from banglatts import BanglaTTS

tts = BanglaTTS(save_location="./audio")
path = tts("আমি বাংলায় কথা বলতে পারি", voice='female', filename='voice.wav')