# Candlestick Patterns Indicator

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

Original code by Donovan Wall
