
from gtts import gTTS
import os

input_file = open('ucharan.txt', 'r')
count_lines = 0
for line in input_file:
    print (line)
    if line == '\t' or line == '\n':
        break
    
    else:  
        myobj= gTTS(text=line, lang='hi', slow=False)
    #file_input = input("Enter a file name  : ")
        count_lines += 1
        fname="ucharan_"+str(count_lines)+".mp3"
        myobj.save(fname)
   # myobj.save("audio_file.mp3")
        os.system("mpg321 fname")    
        
print ('number of lines:', count_lines)
input_file.close()




