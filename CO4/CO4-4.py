import datetime
class Time:
    def _init_(self):
        time_entry = input('Enter a time in hh:mm:ss format:')
        self._hours, self.minutes, self._seconds = map(int, time_entry.split(':'))
        print(datetime.time(self._hours, self.minutes, self._seconds))
    def _add_(self, other):
        self.seconds = self._hours*60*60 + self.minutes*60 + self._seconds
        other.seconds = other._hours*60*60 + other.minutes*60 + other._seconds
        return convert(self.seconds+other.seconds)
def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds//3600
    seconds %= 3600
    minutes = seconds//60
    seconds %= 60
    return "%d:%02d:%02d" % (hour, minutes, seconds)
t1 = Time()
t2 = Time()
print(t1 + t2)
