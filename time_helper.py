#!/usr/bin/python
from datetime import datetime

def get_time():
    return datetime.now().strftime('%H:%M on %B %d, %Y')

