import csv
from datetime import datetime
import os

__all__ = ['log_trade']

LOG_FILE = "data/trade_logs_elite.csv"

def log_trade(signal, lot, result):
    try:
        os.makedirs("data", exist_ok=True)
        file_exists = os.path.exists(LOG_FILE)

        with open(LOG_FILE, "a", newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow([
                    'timestamp', 'strategy', 'pair', 'direction',
                    'sl_pips', 'tp_pips', 'lot_size', 'result'
                ])
            writer.writerow([
                datetime.now().isoformat(),
                signal.get("strategy", "unknown"),
                signal.get("pair", "unknown"),
                signal.get("direction", "unknown"),
                signal.get("sl_pips", 0),
                signal.get("tp_pips", 0),
                lot,
                result
            ])
        print("📝 Trade logged successfully")
    except Exception as e:
        print(f"❌ Error logging trade: {e}")
