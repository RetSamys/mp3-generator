import random

def frameHeader():
    "generate standard frame header"
    #header has 4 bytes, and its 32 bits is split into smaller subsegments, hence the odd numbers:

    #1st byte
    frameSync1=255 #Frame sync (all bits must be set)

    #2nd byte
    frameSync2=128+64+32 #Frame sync (all bits must be set)
    MPEGvers=16+0 #MPEG Audio version ID: 00 (0+0) - MPEG Version 2.5 (later extension of MPEG 2), 01 (0+8) - reserved, 10 (16+0) - MPEG Version 2 (ISO/IEC 13818-3), 11 (16+8) - MPEG Version 1 (ISO/IEC 11172-3) 
    layerDescription=0+2 #Layer description: 00 (0+0) - reserved, 01 (0+2) - Layer III, 10 (4+0) - Layer II, 11 () - Layer I
    protecc=1 #Protection bit: 0 - Protected by CRC (16bit CRC follows header), 1 - Not protected

    #3rd byte
    bitrateIndex=0+0+0+16 #Bitrate index: for MPEG-2, 0001 (0+0+0+16) means 8kbit/s
    samplingRate=8+0 #Sampling rate frequency index: for MPEG-2, 10 (8+0) means 16000 Hz
    padding=0 #Padding bit
    private=0 #Private bit. This one is only informative. (aka it's not good for anything? =D )
    
    #4th byte
    channelMode=128+64 #Channel Mode: 00 (0+0) - Stereo, 01 (0+64) - Joint stereo (Stereo), 10 (128+0) - Dual channel (2 mono channels), 11 (128+64) - Single channel (Mono)
    modeExtension=0+0 #Mode extension (Only used in Joint stereo)
    copyrighted=0 #Copyright:  0 - Audio is not copyrighted, 1 (8) - Audio is copyrighted
    original=4 #Original: 0 - Copy of original media, 1 (4) - Original media;  The original bit indicates, if it is set, that the frame is located on its original media.
    emphasis=0+0 #Emphasis: 00 (0+0) - none, 01 (0+1) - 50/15 ms, 10 (2+0) - reserved, 11 (2+1) - CCIT J.17

    #return the 4 bytes
    return [frameSync1,frameSync2+MPEGvers+layerDescription+protecc,bitrateIndex+samplingRate+padding+private,channelMode+modeExtension+copyrighted+original+emphasis]

def frameData():
    "generate random audio for frame"
    #the frame length is determined by bit rate, sample rate, and samples per frame
    #the formula is:
    #samples / bits-per-byte(8) * bit rate / (sample rate + padding (1 or 0) )
    #Note that MPEG-1 has 1152 and MPEG-2 has 576 samples per frame in Layer III
    #For example, an MPEG-2 with a bitrate of 8kbps and a samplerate of 16000 hz gives you 576/8*8000/16000=36
    #don't forget to substract the header bytes (4)
    result=[]
    for i in range(32):
        result+=[random.randint(0,255)]
        #result+=[0]
    return result

def generateRandomMP3():
    #a frame has a real time length of samples/sampling rate. Note that MPEG-1 has 1152 and MPEG-2 has 576 samples per frame in Layer III
    #for MPEG-2 and sampling rate of 16000 hz you'll get 36 ms per frame
    #a 40-L binary QR can store up to 2953 bytes
    #the MP3 file size is 36 bytes (for 8kbps), multiplied by the number of frames
    #a binary QR can store an MP3 of up to 82 frames, or 2953 ms (almost 3s)

    mp3Binary=[]
    for i in range(82):
        mp3Binary+=frameHeader()
        mp3Binary+=frameData()
    return mp3Binary

def run():
    loc=input("""This will generate a small MP3 file with random audio content. Please enter location of the file:
""")
    name=input("""Please enter file name (without extension):
""")
    if name=="":name="random"
    loc=loc.replace('\\',"/")
    if len(loc)>0:
        if loc[-1]!='/':loc+='/'
    path=loc+name+".mp3"
    f=open(path,"w+b")
    f.write(bytearray(generateRandomMP3()))
    f.close()
    print("Successfully created "+name+".mp3")
run()
