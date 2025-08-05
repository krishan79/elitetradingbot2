# Trading Bot - Prop Firm Ready

A Python-based trading bot with multiple strategies including EMA crossover, risk management, and session filtering.

## 🚀 Features

- **Multiple Strategies**: London Scalp, Trend Follow, Breakout, Mean Reversion, EMA Crossover
- **Risk Management**: Daily drawdown limits, position sizing, max lot limits
- **Session Filtering**: Only trades during specified hours (12:30-22:30 IST)
- **News Filtering**: Avoids trading during news impact times
- **Trade Logging**: All trades logged to CSV with timestamps
- **Error Handling**: Robust error handling and graceful shutdown

## 📋 Requirements

- Python 3.7+
- Required packages: `pyyaml`, `pytz`

## 🛠️ Installation

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Verify installation:**
   ```bash
   python test_bot.py
   ```

3. **Run the bot:**
   ```bash
   python main.py
   ```

## 📁 File Structure

```
prop_firm_bot/
├── main.py              # Main bot runner
├── strategy_engine.py   # Trading strategies (including EMA crossover)
├── risk_manager.py      # Risk management and position sizing
├── trade_executor.py    # Trade execution (simulated)
├── session_filter.py    # Trading session time filter
├── news_filter.py       # News impact time filter
├── logger.py           # Trade logging to CSV
├── config.yaml         # Risk configuration
├── test_bot.py         # Test script to verify components
├── requirements.txt    # Python dependencies
└── data/              # Trade logs directory (auto-created)
    └── trade_logs.csv # Trade history
```

## ⚙️ Configuration

Edit `config.yaml` to adjust risk parameters:

```yaml
risk:
  daily_drawdown: 4000    # Maximum daily loss
  total_drawdown: 8000    # Maximum total loss
  risk_per_trade: 0.5     # Risk per trade (%)
  max_lot: 10            # Maximum lot size
```

## 🎯 Strategies

### EMA Crossover Strategy
- **BUY Signal**: When EMA 20 crosses above EMA 50
- **SELL Signal**: When EMA 20 crosses below EMA 50
- **Stop Loss**: 30 pips
- **Take Profit**: 50 pips

### Other Strategies
- **London Scalp**: Short-term scalping strategy
- **Trend Follow**: Trend following strategy
- **Breakout**: Breakout trading strategy
- **Mean Reversion**: Mean reversion strategy

## 🔧 Customization

### Adding New Strategies
1. Add your strategy function to `strategy_engine.py`
2. Include it in the `strategies` list in `get_trade_signal()`
3. Return a signal dictionary with required fields

### Connecting to Real Broker
1. Replace `trade_executor.py` with your broker's API
2. Update `risk_manager.py` to use real account data
3. Modify `session_filter.py` for your timezone

## 🚨 Important Notes

- **Demo Mode**: Currently runs in simulation mode
- **Session Time**: Trades only between 12:30-22:30 IST
- **News Filter**: Avoids trading at :00 and :30 minutes
- **Risk Management**: Always active to protect capital

## 🐛 Troubleshooting

### Common Issues

1. **Import Error**: Install dependencies with `pip install -r requirements.txt`
2. **Config Error**: Ensure `config.yaml` exists and is properly formatted
3. **Permission Error**: Check file permissions for data directory

### Testing
Run the test script to verify all components:
```bash
python test_bot.py
```

## 📊 Trade Logs

All trades are logged to `data/trade_logs.csv` with:
- Timestamp
- Strategy used
- Currency pair
- Direction (buy/sell)
- Stop loss (pips)
- Take profit (pips)
- Lot size
- Result

## 🔒 Safety Features

- **Graceful Shutdown**: Press Ctrl+C to stop safely
- **Error Recovery**: Automatically retries after errors
- **Risk Limits**: Multiple layers of risk protection
- **Session Control**: Only trades during specified hours

## 📞 Support

If you encounter issues:
1. Run `python test_bot.py` to identify problems
2. Check the console output for error messages
3. Verify all files are in the correct directory
4. Ensure Python and dependencies are properly installed

---

**⚠️ Disclaimer**: This is a demo bot for educational purposes. Use at your own risk in live trading. 