import yaml
import os

__all__ = ['is_trade_allowed', 'calculate_lot_size']

# Get absolute path to config.yaml relative to this file
current_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(current_dir, "config.yaml")

with open(config_path, "r") as f:
    config = yaml.safe_load(f)

DAILY_DD_LIMIT = config['risk']['daily_drawdown']
TOTAL_DD_LIMIT = config['risk']['total_drawdown']
MAX_RISK_PERCENT = config['risk']['risk_per_trade']

# Simulated tracking values (to be replaced with live data)
today_loss = 0
floating_loss = 0
peak_equity = 100000
current_equity = 100000

pip_values = {
    "EURUSD": 10,
    "XAUUSD": 1.0,
    "NAS100": 1.0
}

def is_trade_allowed(balance, trade_signal):
    global today_loss, floating_loss, current_equity, peak_equity
    
    if today_loss + floating_loss >= DAILY_DD_LIMIT:
        return False
    if peak_equity - current_equity >= TOTAL_DD_LIMIT:
        return False
    return True

def calculate_lot_size(balance, risk_percent, sl_pips, pair):
    pip_value = pip_values.get(pair, 10)
    risk_amount = balance * (risk_percent / 100)
    lot_size = risk_amount / (sl_pips * pip_value)
    return round(min(lot_size, config['risk']['max_lot']), 2)

