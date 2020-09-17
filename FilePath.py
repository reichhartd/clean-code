class File:
    __file_path_part: str
    __file_name: str

    def __init__(self, file_path):
        try:
            last_slash_index = file_path.rindex('/') + 1
            self.__file_path_part = file_path[:last_slash_index]
            self.__file_name = file_path[last_slash_index:]
        except:
            self.__file_path_part = ''
            self.__file_name = file_path

    def get_path_part(self) -> str:
        return self.__file_path_part

    def get_filename_part(self) -> str:
        return self.__file_name

    def get_file_type(self) -> str:
        try:
            last_dot_index = self.__file_name.rindex('.')
            return self.__file_name[last_dot_index + 1:]
        except:
            return ''


assert(File("log/cups/access_log").get_path_part() == "log/cups/")
assert(File("log/cups/").get_path_part() == "log/cups/")
assert(File("cups/access_log").get_path_part() == "cups/")
assert(File("access_log").get_path_part() == "")
assert(File("log/cups/access_log").get_filename_part() == "access_log")
assert(File("log/cups/").get_filename_part() == "")
assert(File("cups/access_log").get_filename_part() == "access_log")
assert(File("access_log").get_filename_part() == "access_log")
assert(File("log/cups/access_log").get_file_type() == "")
assert(File("base/FileHelper.cpp").get_file_type() == "cpp")
assert(File("base/FileHelper.cpp.bak").get_file_type() == "bak")
assert(File("src/base.tmp/").get_file_type() == "")