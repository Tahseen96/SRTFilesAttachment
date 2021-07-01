# In this project we attach all .SRT file to its video file
import os
import os.path
import mimetypes
def video(videoFilesPath,srtFilesPath):
    subtitles(srtFilesPath)
    if(os.path.isdir(videoFilesPath)):
        count = 0
        filesList = os.listdir(videoFilesPath)
        strList = os.listdir(srtFilesPath)
        os.chdir(os.getcwd() + '\Videos')
        while(count<len(strList)):
            for (file) in filesList:
                if(mimetypes.guess_type(file)[0].find("video") != -1):  
                    if(os.path.basename(file).find(os.path.basename(strList[count]).split(".")[0]) != -1):
                        os.rename(os.path.join(srtFilesPath,os.path.basename(strList[count])),os.path.basename(file).split(".")[0] + ".srt")
                        pass
                    else:
                        pass
                else:
                    print("This is not a video file")
                    remove = os.path.join(videoFilesPath,file)
                    os.remove(remove)
            count+=1   
    else:
        print("Directory is not correct")
def subtitles(srtFilesPath):
    if(os.path.isdir(srtFilesPath)):
        filesList = os.listdir(srtFilesPath)
        for file in filesList:
            if(file.endswith(".srt") or file.endswith(".SRT")):
                pass
                # os.replace(os.path.join(srtFilesPath,file),os.path.join(videoFilesPath,file))
            else:
                remove = os.path.join(srtFilesPath,file)
                os.remove(remove)
    else:
        print("Srt Directory is not correct")

video(r"C:\Users\Tahseen\AttachsrtToFiles\Videos",r"C:\Users\Tahseen\AttachsrtToFiles\SRTFiles")
