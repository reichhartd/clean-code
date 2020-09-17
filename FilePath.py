import re

def get_path_part(filename):
    try:
        last_slash_index = int(filename.rindex('/'))
        return filename[0: last_slash_index + 1]
    except:
        return ''


def get_filename_part(filename):
    try:
        int(filename.rindex('/'))
    except:
        return filename

    pos = filename.rindex('/')
    base_name = filename[pos + 1:]
    return base_name



def get_file_type(filename):
    try:
        occurrences = [m.start() for m in re.finditer('\.', filename)]
        return filename[occurrences[-1] + 1:]
    except:
        pass

    return ''


assert(get_path_part("log/cups/access_log") == "log/cups/")
assert(get_path_part("log/cups/") == "log/cups/")
assert(get_path_part("cups/access_log") == "cups/")
assert(get_path_part("access_log") == "")
assert(get_filename_part("log/cups/access_log") == "access_log")
assert(get_filename_part("log/cups/") == "")
assert(get_filename_part("cups/access_log") == "access_log")
assert(get_filename_part("access_log") == "access_log")
assert(get_file_type("log/cups/access_log") == "")
assert(get_file_type("base/FileHelper.cpp") == "cpp")
assert(get_file_type("base/FileHelper.cpp.bak") == "bak")