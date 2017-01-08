from datetime import date, timedelta, datetime
import logging
import pytz
logging.basicConfig(filename='mbc.log',level=logging.DEBUG)


DAY_OF_WEEK = (
    (0, 'Monday'),
    (1, 'Tuesday'),
    (2, 'Wednesday'),
    (3, 'Thursday'),
    (4, 'Friday'),
    (5, 'Saturday'),
    (6, 'Sunday')
)


def all_of_days(week_day, week_time):
    ahora = datetime.now(pytz.utc)
    d = ahora
    d += timedelta(days=week_day - ahora.weekday())
    while d.year <= ahora.year:
        logging.debug(d.replace(hour=week_time.hour, minute=week_time.minute))
        yield d.replace(hour=week_time.hour, minute=week_time.minute)
        d += timedelta(days=7)

