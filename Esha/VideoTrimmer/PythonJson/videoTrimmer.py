import json
from moviepy.editor import *

# To get extension of input file
def getExtension(name):
    return(name.split(".")[-1])

# To get file parameters for each instance to be trimmed
def getParameters(data,i):
    startTime = data['outputParameters'][i]['startTime']
    endTime = data['outputParameters'][i]['endTime']
    ssTime = data['outputParameters'][i]['span']
    name = data['outputParameters'][i]['outputFileName'].strip()
    return(startTime,endTime,ssTime,name)

# To clip the main "clip" with specified parametrs 
def getFiles(clip,name,startTime,endTime):
    clip2 = clip.subclip(startTime,endTime)
    clip2.write_videofile(name)
 
# main()
def main():   
    #reading json data
    with open("confVideoTrimmer.json") as f:
        completeData = json.load(f)
    
    for data in completeData:   
        iName = data['inputFile']

        # Get extension of inputfile
        extension = "."+getExtension(iName)

        # Assign input file as "clip"
        clip = VideoFileClip(iName)
       

        #iterate throuh all the instance of json objeacts
        for i in range(len(data['outputParameters'])):
            
            # Get parametrs for each object in json one at a time
            parameters = getParameters(data,i)
            
            startTime = parameters[0] 
            endTime = parameters[1]
            ssTime = parameters[2]
            name = parameters[3]
            
            try:
                if startTime > clip.duration or endTime > clip.duration or ssTime > clip.duration:
                    msg = "Not valid Range"
                    raise ValueError(msg,name)
                else:
                    # For when No Span is given 
                    if ssTime == 0:
                        oName = name+extension
                        # Passing parameters to obtain output
                        getFiles(clip,oName,startTime,endTime)
                    
                    # For when span is given along with endtime
                    elif endTime != 0:
                        # Check for left duration to avoid failure
                        # in case where it is less than span time
                        leftDuration = endTime - startTime
                        if leftDuration < ssTime:
                            dummyTime = startTime + leftDuration
                        else:
                            dummyTime = startTime+ssTime 
                        count = 1
                        while dummyTime <= endTime and startTime != dummyTime:
                            f = iName.split(".")[-2]
                            oName = f+"_"+str(count)+extension
                            # Passing parameters to obtain output
                            getFiles(clip,oName,startTime,dummyTime)
                            startTime = dummyTime
                            leftDuration = endTime - startTime
                            if leftDuration < ssTime:
                                dummyTime = startTime + leftDuration
                            else:
                                dummyTime = startTime+ssTime 
                            count += 1
                            
                    # For when span is given but no endtime is specified
                    elif endTime == 0:
                        endTime = clip.duration
                        # Check for left duration to avoid failure
                        # in case where it is less than span time
                        leftDuration = endTime - startTime
                        if leftDuration < ssTime:
                            dummyTime = startTime + leftDuration
                        else:
                            dummyTime = startTime+ssTime 
                        count = 1
                        while dummyTime <= endTime and startTime != dummyTime: 
                            f = iName.split(".")[-2]
                            oName = f+"_"+str(count)+extension
                            
                            # Passing parameters to obtain output
                            getFiles(clip,oName,startTime,dummyTime)
                            startTime = dummyTime
                            # Condition where the clip duraion left to generated has
                            # time less than span time
                            leftDuration = endTime - startTime
                            if leftDuration < ssTime:
                                dummyTime = startTime + leftDuration
                            else:
                                dummyTime = startTime+ssTime
                            count += 1

            except ValueError as ve:
                print(msg)
                print(name,"Cannot be created")
# Call to main
if __name__ == '__main__':
    main()