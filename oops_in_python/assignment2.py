import abc
import datetime

class WriteFile(object):
  __mataclass__ = abc.ABCMeta 
  @abc.abstractmethod
  def write(self):
    return
  
  def __init__(self, file_name):
    self.file_name = file_name
  
  def write_line(self, text):
    with open(self.file_name, 'a') as file:
      file.write(text + "\n")

class LogFile(WriteFile):
  
  def write(self, log_msg):
    date_time = datetime.datetime.now()
    date_time_str = date_time.strftime("%Y-%m-%d %H:%M")
    # super(LogFile, self).write_line(f"{date_time_str}  {log_msg}")
    self.write_line(f"{date_time_str}  {log_msg}")

  
class DelimFile(WriteFile):
  def __init__(self, file_name, sep=","):
    super(DelimFile, self).__init__(file_name)
    self.seperator = sep
    
  
  def write(self, valList):
    string = self.seperator.join(valList) 
    # print(f"{string}")
    # super(DelimFile, self).write_line(string)
    self.write_line(string)
  


log = LogFile('log.txt')
c = DelimFile('log.csv', ",")

log.write("this is a log message")
log.write("this is another log message")
c.write(['a', 'b', 'c', 'd'])
c.write(['1', '2', '3', '4'])