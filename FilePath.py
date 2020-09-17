class File:
    file_path_part: str
    file_name: str

    def __init__(self, file_path):
        try:
            last_slash_index = file_path.rindex('/') + 1
            self.file_path_part = file_path[:last_slash_index]
            self.file_name = file_path[last_slash_index:]
        except:
            self.file_path_part = ''
            self.file_name = file_path

    def get_path_part(self):
        return self.file_path_part

    def get_filename_part(self):
        return self.file_name

    def get_file_type(self, file_path):
        name = self.split_path(file_path)[1]
        try:
            last_dot_index = name.rindex('.')
            return name[last_dot_index + 1:]
        except:
            return ''


assert(File("log/cups/access_log").file_path_part == "log/cups/")
assert(File("log/cups/access_log").file_name == "access_log")
assert(File("log/cups/access_log").get_path_part() == "log/cups/")
assert(File("log/cups/").get_path_part() == "log/cups/")
assert(File("cups/access_log").get_path_part() == "cups/")
assert(File("access_log").get_path_part() == "")
assert(File("log/cups/access_log").get_filename_part() == "access_log")
assert(File("log/cups/").get_filename_part() == "")
assert(File("cups/access_log").get_filename_part() == "access_log")
assert(File("access_log").get_filename_part() == "access_log")
assert(File().get_file_type("log/cups/access_log") == "")
assert(File().get_file_type("base/FileHelper.cpp") == "cpp")
assert(File().get_file_type("base/FileHelper.cpp.bak") == "bak")
assert(File().get_file_type("src/base.tmp/") == "")