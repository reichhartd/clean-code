def __split_path(file_path):
    try:
        last_slash_index = file_path.rindex('/') + 1
        file_path_part = file_path[:last_slash_index]
        filename = file_path[last_slash_index:]
        return file_path_part, filename
    except:
        return '', file_path

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
        try:
            last_slash_index = int(filename.rindex('/'))
        except:
            last_slash_index = 0

        if last_slash_index > last_dot_index:
            return ''

        return filename[last_dot_index + 1:]
    except:
        return ''


assert(__split_path("log/cups/access_log")[0] == "log/cups/")
assert(__split_path("log/cups/access_log")[1] == "access_log")

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
assert(get_file_type("src/base.tmp/") == "")