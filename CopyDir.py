The MIT License (MIT)

Copyright (c) 2015 Exequor Studios Inc. (exequor)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

import os
import shutil
import hashlib

def sha1OfFile(filepath):
    import hashlib
    with open(filepath, 'rb') as f:
        return hashlib.sha1(f.read()).hexdigest()

def copydir(sourcePath, destinationPath,ignore):
    #onlydirs = [f for f in os.listdir(mypath) if not os.path.isfile(os.path.join(sourcePath,f))]
    #print(onlydirs)
    #for onedir in onlydirs:
        
        #copydir(mypath+"/"+onedir)

    onlyfiles = [f for f in os.listdir(sourcePath)]
    
    for onefile in onlyfiles:
        if (ignore.count(onefile) == 0):
            srcfile = sourcePath+"/"+onefile
            dstfile = destinationPath+"/"+onefile

            if os.path.isdir(srcfile):
                if not os.path.isdir(dstfile):
                    os.makedirs(dstfile)
                    print("Making Dir:",dstfile)
                copydir(srcfile, dstfile,ignore)
            elif os.path.isfile(srcfile):                  
                if os.path.isfile(dstfile):
                    if os.path.getmtime(srcfile) == os.path.getmtime(dstfile):
                        print ("DATE EQUAL: "+srcfile)
                    elif sha1OfFile(srcfile) == sha1OfFile(dstfile):
                        print ("DATE DIFFERENT, SIG EQUAL: "+srcfile)
                        os.utime(dstfile, (-1,os.path.getmtime(srcfile)))
                    else:
                        print ("DATE DIFFERENT, SIG DIFFERENT, COPY: "+srcfile)
                        shutil.copyfile(srcfile, dstfile)
                else:
                    shutil.copyfile(srcfile, dstfile)
                    print ("Copying : "+srcfile)
