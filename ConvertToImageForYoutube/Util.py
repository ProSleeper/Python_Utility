# 경과시간 체크용 클래스.
import datetime

class ElapsedTime:
 def __init__(self):
    self.start_time = datetime.datetime.now()

 def endTime(self):
    self.end_time = datetime.datetime.now()
    self.elapsed_time = self.end_time - self.start_time

    self.elapsed_seconds = int(self.elapsed_time.total_seconds())
    self.elapsed_milliseconds = int((self.elapsed_time.total_seconds() - self.elapsed_seconds) * 1000)

    print("Duration: {}sec {}ms".format(self.elapsed_seconds, self.elapsed_milliseconds))
