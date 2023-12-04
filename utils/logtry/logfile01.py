import logging

from logging import StreamHandler
from logging import FileHandler

####默认是低于warning的不输出


####但是可以修改默认日志级别
#logging.basicConfig( level = logging.DEBUG )
####同样，也可以指定输出的文件位置
# logging.basicConfig( filename= 'panbodemo.log', level = logging.INFO)
# logging.debug("==== here is debug information ====")
# logging.info("==== here is info information ====")
# logging.warning("==== here is warning information ====")
# logging.error("==== here is error information ====")
# logging.critical("==== here is critical information ====")


###指定日志格式
###日志格式可以根据个人需求自定义

# logging.basicConfig( format = " PID:%(process)d Thread:%(thread)d TIME:%(asctime)s LEVEL:%(levelname)s NAME:%(name)s MESSAGE:%(message)s")

# logging.error("==== here is error information ====")


# logger = logging.getLogger(__name__)


#处理器 handler
#负责记录日志记录在哪里
#可能会将INFO级别的日志记录到文件
#将ERROR级别的日志记录到标准输出，
#将某些关键日志（例如有订单或者严重错误）发送到某个邮件地址通知老板
#这时候你的记录器添加多个不同的处理器来处理不同的消息日志，以此根据消息的重要性发送的特定的位置。

"""
1、StreamHandler 标准流处理器，将消息发送到标准输出流、错误流
2、FileHandler 文件处理器，将消息发送到文件
3、RotatingFileHandler 文件处理器，文件达到指定大小后，启用新文件存储日志
4、TimedRotatingFileHandler 文件处理器，日志以特定的时间间隔轮换日志文件
"""

# logger = logging.getLogger(__name__)

# #设置DEBUG级别
# logger.setLevel(logging.DEBUG)

# #标准流处理器，设置的级别为WARNING
# stream_handler = StreamHandler()
# stream_handler.setLevel(logging.WARNING)
# logger.addHandler(stream_handler)

# #文件处理器，设置的级别为INFO
# file_handler = FileHandler(filename = "panbotest.log")
# file_handler.setLevel(logging.INFO)
# logger.addHandler(file_handler)

# logger.debug("==== here is debug information ====")
# logger.info("==== here is info information ====")
# logger.warning("==== here is warning information ====")
# logger.error("==== here is error information ====")


#logging.basicConfig  给日志系统做一个最基础的配置。
#它必须在开始记录日志前调用

"""
1、创建一个root记录器
2、设置root的日志级别为warning
3、为root记录器添加StreamHandler处理器
4、为处理器设置一个简单格式器
"""

##日志配置
## 可以配置在代码中，/或者单独成configfile。
import logging 
import logging.config

#加载配置
logging.config.fileConfig(r'C:\\Users\\panbo\\Desktop\\pl_ai_project-master\\utils\\logtry\\logging.conf')

#创建logger
logger = logging.getLogger()

#应用代码
logger.debug("debug message")
logger.info("info message")
logger.warning("warning message")
logger.error("error message")












