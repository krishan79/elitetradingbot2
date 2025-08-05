import datetime

__all__ = ['is_safe_to_trade']

def is_safe_to_trade():
    # Simulated check — replace with actual news calendar check later
    now = datetime.datetime.utcnow()
    if now.minute in [0, 30]:  # Simulate news every full & half hour
        return False
    return True 