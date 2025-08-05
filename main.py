from strategy_engine import get_trade_signal, fetch_realtime_candles
from risk_manager import is_trade_allowed, calculate_lot_size
from trade_executor import place_trade
from session_filter import is_in_session
from news_filter import is_safe_to_trade
from trade_logger import log_trade
from datetime import datetime
import time
import sys

BALANCE = 100000
monitored_trades = []

def main():
    print("🚀 Elite Trading Bot Started")
    print("Press Ctrl+C to stop\n")
    
    try:
        while True:
            try:
                if not is_in_session():
                    print("⏰ Outside trading session")
                    time.sleep(300)
                    continue

                if not is_safe_to_trade():
                    print("📰 News time — skipping")
                    time.sleep(300)
                    continue

                trade_signal = get_trade_signal()

                if trade_signal:
                    pair = trade_signal['pair']
                    direction = trade_signal['direction']

                    print("\n📈 SIGNAL:", pair, direction.upper(), trade_signal['strategy'])
                    lot = calculate_lot_size(BALANCE, 0.5, trade_signal['sl_pips'], pair)
                    entry_price = trade_signal['price']
                    pip_size = 0.0001 if pair == "EURUSD" else 0.1
                    sl_price = entry_price - trade_signal['sl_pips'] * pip_size if direction == "buy" else entry_price + trade_signal['sl_pips'] * pip_size
                    tp_price = entry_price + trade_signal['tp_pips'] * pip_size if direction == "buy" else entry_price - trade_signal['tp_pips'] * pip_size
                    
                    trade_result = place_trade(trade_signal, lot)
                    log_trade(trade_signal, lot, "OPEN")

                    monitored_trades.append({
                        "pair": pair,
                        "direction": direction,
                        "sl": sl_price,
                        "tp": tp_price,
                        "entry": entry_price,
                        "strategy": trade_signal['strategy']
                    })
                else:
                    print(".", end="", flush=True)

                # Monitor SL/TP Hits
                for t in monitored_trades[:]:
                    df = fetch_realtime_candles(t["pair"])
                    if not df:
                        continue
                    high, low = df.iloc[-1][['high','low']]

                    if t["direction"] == "buy":
                        if low <= t["sl"]:
                            print(f"\n❌ SL hit for {t['pair']} at {t['sl']}")
                            log_trade(t, 0, "SL HIT")
                            monitored_trades.remove(t)
                        elif high >= t["tp"]:
                            print(f"\n✅ TP hit for {t['pair']} at {t['tp']}")
                            log_trade(t, 0, "TP HIT")
                            monitored_trades.remove(t)

                    else:
                        if high >= t["sl"]:
                            print(f"\n❌ SL hit for {t['pair']} at {t['sl']}")
                            log_trade(t, 0, "SL HIT")
                            monitored_trades.remove(t)
                        elif low <= t["tp"]:
                            print(f"\n✅ TP hit for {t['pair']} at {t['tp']}")
                            log_trade(t, 0, "TP HIT")
                            monitored_trades.remove(t)

                time.sleep(300)

            except Exception as e:
                print("⚠️ Error:", e)
                time.sleep(60)

    except KeyboardInterrupt:
        print("\n🛑 Bot stopped by you")
        sys.exit(0)

if __name__ == "__main__":
    main()
