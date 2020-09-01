from datetime import timedelta
import datetime
class interfaceTest():
    def get_today(self):
        now_time = datetime.datetime.now()
        today = now_time.strftime('%Y-%m-%d %H:%M:%S')
        return today
    def get_onedaytime(self,day):
        now_time = datetime.datetime.now()
        day_time = now_time+timedelta(days=day)
        oneday = day_time.strftime('%Y-%m-%d %H:%M:%S')
        return oneday
if "__main__" == __name__:
    day = 7
    a = interfaceTest().get_onedaytime(day=day)
    b = interfaceTest().get_today()
    print('今天后的日期：'+b)
    print(str(day)+'天后的日期：'+a)