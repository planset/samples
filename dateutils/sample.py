from datetime import datetime
from dateutil.rrule import rrule, DAILY, MO, WE

rrule_obj = rrule(DAILY,
                  byweekday=(MO, WE),
                  dtstart=datetime(2012,1,1),
                  until=datetime(2012, 2, 1))

for dt in rrule_obj:
    print dt

