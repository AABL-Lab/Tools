# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


from moviepy.editor import *
import time
video_len = 20
for i in range(0, video_len):
    clip = VideoFileClip("/Users/hangyu/Desktop/0.mp4" ).subclip(i*4, i*4+4)
    clip.write_videofile("/Users/hangyu/Desktop/Clips/"+"episode0"+"step"+str(i)+".mp4")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
