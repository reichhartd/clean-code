class FilePath:
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

    def get_filename_part(self, file_path):
        return self.split_path(file_path)[1]

    def get_extension(self, file_path):
        name = self.split_path(file_path)[1]
        try:
            last_dot_index = name.rindex('.')
            return name[last_dot_index + 1:]
        except:
            return ''


assert(FilePath("log/cups/access_log").file_path_part == "log/cups/")
assert(FilePath("log/cups/access_log").file_name == "access_log")
assert(FilePath("log/cups/access_log").get_path_part() == "log/cups/")
assert(FilePath("log/cups/").get_path_part() == "log/cups/")
assert(FilePath("cups/access_log").get_path_part() == "cups/")
assert(FilePath("access_log").get_path_part() == "")
assert(FilePath().get_filename_part("log/cups/access_log") == "access_log")
assert(FilePath().get_filename_part("log/cups/") == "")
assert(FilePath().get_filename_part("cups/access_log") == "access_log")
assert(FilePath().get_filename_part("access_log") == "access_log")
assert(FilePath().get_extension("log/cups/access_log") == "")
assert(FilePath().get_extension("base/FileHelper.cpp") == "cpp")
assert(FilePath().get_extension("base/FileHelper.cpp.bak") == "bak")
assert(FilePath().get_extension("src/base.tmp/") == "")