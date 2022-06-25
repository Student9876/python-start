# This is to play a sound using playsound module
# To stop the sound click on the terminal
# After the cursor appears then CTRL+C

import multiprocessing
from playsound import playsound
p=multiprocessing.process(target=playsound, args=("D:\\Audio\\eps4_main_menu.wav",))
p.start()
input("press Enter to stop playback")
p.terminate()