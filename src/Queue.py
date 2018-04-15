import math

class Queue(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        self.items = []
    
    # Insert at position 0.
    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    
    def get(self, name):
        return_item=None
        object_list=[item for item in self.items if item.name==name]
        if len(object_list) > 0:
            return_item=object_list[0]
        #remove item from list
        self.items=[item for item in self.items if item.name!=name]
        return return_item

    def size(self):
        return len(self.items)

    #
    def peek(self, name):
        return_item = None
        object_list = [item for item in self.items if item.name == name]
        if len(object_list) > 0:
            return_item = object_list[0]
        return return_item
    
    def isEmpty(self):
        return len(self.items)==0
    
    
class DayHourMinute(object):
    def __init__(self, day_string, hour_string, minute_string):
        self.day=day_string
        self.hour=hour_string
        self.minute=minute_string


class ScheduleHour(object):
    def __init__(self, day, hour, index):
        self.day = day
        self.hour = hour
        self.index = index

#function degrees to radians
def deg2rad(deg):
    return (deg * math.pi / 180)