'''
First version of copy tool, which ignores copy errors
caused by file permissions or files in use
'''

import os
import shutil

def copyTree(sourceDir, destDir):

    print "sourceDir:", sourceDir
    print "destDir:", destDir
    print

    errors = list()
    
    if not os.path.exists(sourceDir):
        return (False, "Source Directory does not exists")

    if not os.path.exists(destDir):
        try:
            os.makedirs(destDir)
        except:
            return (False, "Could not create %s" % destDir)

    cwd = destDir
    for dirName, subDirList, fileList in os.walk(sourceDir):
        cwd = os.path.join(destDir, dirName[len(sourceDir):].strip(os.sep))

        for subDir in subDirList:
            try:
                os.makedirs(os.path.join(cwd, subDir))
            except:
                errors.append("Could not create %s" % str(os.path.join(cwd, subDir)))

        for _file in fileList:
            try:
                shutil.copy(os.path.join(dirName, _file), cwd)
            except:
                errors.append("Could not create %s" %  str(os.path.join(dirName, _file)))

    if len(errors) > 0:
        return (False, '\n'.join(errors))
    else:
        return (True, '')

rootDir = os.path.abspath(os.path.join(__file__ , ".."))

res = copyTree(os.path.join(rootDir, "sourceDir"), os.path.join(rootDir, "destDir"))
print res
