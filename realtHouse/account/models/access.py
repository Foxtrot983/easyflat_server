from django.utils import timezone as tz

def make_access(days=0, hours=0, minutes=0):
    return tz.now() + tz.timedelta(days=days, hours=hours, minutes=minutes)