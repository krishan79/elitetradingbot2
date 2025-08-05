from datetime import datetime
import pytz

__all__ = ['is_in_session']

def is_in_session():
    ist = pytz.timezone('Asia/Kolkata')
    now = datetime.now(ist)
    hour = now.hour
    # Allow trading only between 12:30–22:30 IST (London to NY)
    return 12 <= hour <= 22 