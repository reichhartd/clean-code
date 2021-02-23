import re


# Get the File path E.g. log/cups/
def get_file(file_path):
    if len(file_path) > 0 and file_path[len(file_path) - 1] == '/':
        return file_path

    try:
        p_location = int(file_path.rindex('/'))
    except:
        p_location = -1
    dirName = ''
    # Karl what is this?
    if p_location >= 0:
        dirName = file_path[0: p_location + 1]
    else:
        dirName = '' #sFilename

    return dirName

# This function gets the file
def get_filename_part(filename):
    try:
        int(filename.rindex('/'))
    except:
        return filename

    pos = filename.rindex('/')
    base_name = filename[pos + 1:]
    return base_name


#.png
def get_extension_part(filename):
    try:
        occurrences = [m.start() for m in re.finditer('\.', filename)]
        return filename[occurrences[-1] + 1:]
    except:
        return ''
