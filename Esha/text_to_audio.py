
from gtts import gTTS
import os

input_file = open('ucharan.txt', 'r')
count_lines = 0
for line in input_file:
    print (line)
    break if line == '\t' or line == '\n' else continue 
        count_lines += 1
        fname="ucharan_"+str(count_lines)+".mp3"
        myobj.save(fname)
        print("nothing to commit")
for j in range 
