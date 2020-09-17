import re

def get_path_part(filename):
    try:
        last_slash_index = int(filename.rindex('/'))
        return filename[0: last_slash_index + 1]
    except:
        return ''


def get_filename_part(filename):
    try:
        last_slash_index = int(filename.rindex('/'))
        return filename[last_slash_index + 1:]
    except:
        return filename


def get_file_type(filename):
    try:
        last_dot_index = int(filename.rindex('.'))
        return filename[last_dot_index + 1:]
    except:
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