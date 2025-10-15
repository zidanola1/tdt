# Trading Pattern Detection Indicators

A collection of TradingView Pine Script indicators for pattern detection.

## 📦 Indicators Included

1. **Candlestick Patterns** (`candlestick_patterns.pine`) - Classic candlestick pattern detection
2. **Harmonic Patterns** (`harmonic_patterns_simple.pine`) - Simple harmonic pattern detection (Gartley, Bat, Butterfly, Crab)

---

## 🕯️ Candlestick Patterns Indicator

A TradingView Pine Script indicator for detecting and alerting on multiple candlestick patterns.

## Features

This indicator detects the following candlestick patterns:

### Bullish Patterns
- **Three Inside Up** - Three-candle bullish reversal pattern
- **Three Outside Up** - Three-candle bullish engulfing pattern
- **Morning Star** - Three-candle bullish reversal pattern with a gap
- **Bullish Engulfing** - Two-candle pattern where a bullish candle engulfs the previous bearish candle
- **Hammer** - Single-candle bullish reversal pattern with a long lower shadow
- **Inverted Hammer** - Single-candle bullish reversal pattern with a long upper shadow

### Bearish Patterns
- **Three Inside Down** - Three-candle bearish reversal pattern
- **Three Outside Down** - Three-candle bearish engulfing pattern
- **Evening Star** - Three-candle bearish reversal pattern with a gap
- **Bearish Engulfing** - Two-candle pattern where a bearish candle engulfs the previous bullish candle

### Fractal Patterns
- **Engulfing Fractals** (High and Low)
- **Non-Engulfing Fractals** (High and Low)

### Other Patterns
- **Doji / Near Doji** - Indecision candles where open and close are very close

## Usage

1. Open TradingView
2. Open the Pine Editor
3. Copy the contents of `candlestick_patterns.pine`
4. Add the script to your chart
5. Configure the pattern toggles in the indicator settings
6. Set up custom alerts for the patterns you want to track

## Customization

Each pattern type can be enabled or disabled using the input toggles:
- Enable Three Inside Up and Down Signals
- Enable Three Outside Up and Down Signals
- Enable Morning and Evening Star Signals
- Enable Bullish and Bearish Engulfing Signals
- Enable Hammer and Inverted Hammer Signals
- Enable Doji and Near Doji Signals
- Enable Fractal Signals

## Alerts

Custom alerts are included for all pattern types. You can set up notifications to be alerted when specific patterns form on your charts.

## Author

Original candlestick pattern code by Donovan Wall

---

## 📐 Harmonic Patterns Indicator

A simple, clean harmonic pattern detector that matches the style of the candlestick indicator above.

### Supported Patterns

- **Gartley (222)** - Classic harmonic pattern, AD = 0.786 of XA
- **Bat** - Deep retracement pattern, AD = 0.886 of XA
- **Butterfly** - Extension pattern, AD = 1.27-1.618 of XA (D beyond X)
- **Crab** - Extreme extension, AD = 1.618 of XA (D far beyond X)

### Features

- ✅ Clean visual - draws pattern lines only when complete
- ✅ No spam - patterns shown at completion, not before
- ✅ Simple alerts - one alert when any pattern detected
- ✅ Adjustable tolerance - default 10% (works for most markets)
- ✅ Color coded - green for bullish, red for bearish

### Settings

| Setting | Default | Description |
|---------|---------|-------------|
| ZigZag Depth | 12 | Higher = fewer, stronger pivots |
| Ratio Tolerance | 10% | Flexibility in pattern matching |
| Show Pattern Lines | ON | Draw X-A-B-C-D lines |
| Show Pattern Labels | ON | Label with pattern name |

### Usage

1. Copy `harmonic_patterns_simple.pine` into TradingView Pine Editor
2. Add to chart
3. Adjust ZigZag Depth based on your timeframe (higher for lower timeframes)
4. Set up alert for "Harmonic Pattern Detected"
5. Enter at D-point with confirmation

### Target Setting
- **Conservative**: Point C
- **Moderate**: Point A  
- **Aggressive**: 161.8% extension from D

Stop loss: Just beyond X point

---

## 🚀 Getting Started

1. Choose your indicator:
   - **Candlestick Patterns**: For single/multi-bar patterns
   - **Harmonic Patterns**: For 5-point reversal structures

2. Copy the `.pine` file into TradingView Pine Editor
3. Add to your chart
4. Configure settings for your timeframe
5. Set up alerts

---

## ⚠️ Disclaimer

These indicators are tools for technical analysis. Always use proper risk management and backtest before live trading.
