import subprocess
#videoname="D:\\cloud\\Huffman-Coding\\videos\\video1.mp4"
#filename="D:\\cloud\Huffman-Coding\\videos\\video1.mp4.compressed"
def vidtotext(videoname):
        subprocess.run(["g++", "-std=c++14","Compressor.cpp","-o","archive"])
        subprocess.run(["./archive",videoname])
#vidtotext(videoname)
     
#encryption(videoname)
def texttovid(filename):
        subprocess.run(["g++", "-std=c++14","Compressor.cpp","-o","archive"])
        subprocess.run(["./extract",filename])
#decryption(filename)
#exttovid(filename)