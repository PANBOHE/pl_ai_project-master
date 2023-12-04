from typing import Any


class Config(object):
    class ConstError(TypeError):
        pass


    class ConstCaseError(ConstError):
        pass


    def __setattr__(self, __name: str, __value: Any) -> None:
        #存在性验证，是否已经设置过了
        if __name in self.__dict__.keys():
            raise self.ConstCaseError("Can't change a const variable: '%s'" % __name)
        #合法性验证，是否是大写
        if not __name.isupper():
            #语法规范验证
            raise self.ConstCaseError("Const variable must be combined with upper letters:'%s'" % __name)
        self.__dict__[__name] = __value


    def __str__(self) -> str:
        _str = '<====== Configs information ======>\n'
        for name, value in self.__dict__.items():
            _str += '  {}  \t{}\n'.format(name, value)
        return _str
        
#=============================================#
config = Config()
#=============================================#

"""
Base project information
"""
config.INPUT_FOLDER = "input/inputfile"
config.OUTPUT_FOLDER = "output/outputfile"
config.MAIN_WORK_LOG = "logs/main_work_log"
config.RUN_WORK_LOG = "logs/run_work_log"

"""
Use by ./clear_files_on_time.py

"""
config.CMD_LIST = ["rm -rf {}/*".format(config.INPUT_FOLDER),
                    "rm -rf {}".format(config.MAIN_WORK_LOG),
                    "rm -rf {}".format(config.RUN_WORK_LOG)
                ]
config.SLEEP_TIME = 24*60*60

"""
Use by ../main_work.py

"""
config.USE_LOGGING = True
config.API_URL = ""
config.MAX_RTMP_TIME = 10
config.LOCAL_IP = "192.168.1.1"
config.MAIN_API_PORT = 5000
config.DETECT_PORT = 5001
config.MAX_THREAD_NUM = 50

print("config information is {}".format(config))


if __name__ == "__main__":
    config = Config()
    print("config information is {}".format(config))
