import re


# Get the File path E.g. log/cups/
# sFile is the file path
def get_file(sFile):
    if len(sFile) > 0 and sFile[len(sFile) - 1] == '/':
        return sFile

    try:
        p_location = int(sFile.rindex('/'))
    except:
        p_location = -1
    dirName = ''
    # Karl what is this?
    if p_location >= 0:
        dirName = sFile[0: p_location + 1]
    else:
        dirName = '' #sFilename

    return dirName

# This function gets the file
def get_filename_part(sFilename):
    try:
        int(sFilename.rindex('/'))
    except:
        return sFilename

    pos = sFilename.rindex('/')
    base_name = sFilename[pos + 1:]
    return base_name


#.png
def get_extension_part(sFilename):
    try:
        occurrences = [m.start() for m in re.finditer('\.', sFilename)]
        return sFilename[occurrences[-1] + 1:]
    except:
        pass

    return ''
