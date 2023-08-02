class Clock:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    
    def get_time(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds
    
    def __setattr__(self, key, value):
        if key in ('hours', 'minutes', 'seconds'):
            if value >= 0 and type(value) == int:
                self.__dict__[key] = value
        
        else:
            super.__setattr__(self, key, value)


class DeltaClock:
    def __init__(self, clock1: Clock, clock2: Clock):
        self.clock1 = clock1
        self.clock2 = clock2
    
    def __str__(self):
        res_sec = self.clock1.get_time() - self.clock2.get_time()
        if res_sec <= 0:
            return '00: 00: 00'
        else:
            # hours
            hours, remainder = divmod(res_sec, 3600)
            # minutes, seconds
            minutes, seconds = divmod(remainder, 60)
            # total time
            return '{:02}: {:02}: {:02}'.format(int(hours), int(minutes), int(seconds))
        
    def __len__(self):
        return self.clock1.get_time() - self.clock2.get_time()


dt = DeltaClock(Clock(2, 45, 0), Clock(1, 15, 0))
print(dt) # 01: 30: 00
len_dt = len(dt) # 5400
print(len_dt)
