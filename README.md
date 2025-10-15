# Trading Pattern Detection Suite

A comprehensive collection of TradingView Pine Script indicators for detecting candlestick patterns and advanced harmonic patterns with flexible ratios and ICT confluence.

## 📦 Indicators Included

1. **Candlestick Patterns Indicator** (`candlestick_patterns.pine`) - Classic candlestick pattern detection
2. **Advanced Harmonic Patterns** (`harmonic_patterns_advanced.pine`) - Professional harmonic pattern detection with flexible ratios

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

## 🎯 Advanced Harmonic Patterns Indicator

A professional-grade harmonic pattern detection system featuring:

### Core Features
- **Flexible Ratio System**: Intelligent scoring (0-100%) for pattern quality
- **Dynamic Tolerance**: ATR-based adaptation to market volatility
- **ICT Confluence**: Fair Value Gaps (FVG) and Order Block (OB) detection
- **Trend Context Filter**: Only shows counter-trend reversal setups
- **6 Harmonic Patterns**: Gartley, Bat, Butterfly, Crab, Shark, Cypher

### Supported Patterns

| Pattern | Best For | Reversal Strength | Key Ratio |
|---------|----------|-------------------|-----------|
| **Gartley** | Trending markets | Moderate | AD = 0.786 XA |
| **Bat** | Deep pullbacks | Strong | AD = 0.886 XA |
| **Butterfly** | Extensions | Very Strong | AD = 1.27-1.618 XA |
| **Crab** | Extreme extensions | Extreme | AD = 1.618 XA |
| **Shark** | Trend continuations | Strong | AD = 0.886-1.13 XA |
| **Cypher** | Precision entries | High | AD = 0.786 XA |

### Why Flexible Ratios?

Traditional "perfect" Fibonacci ratios (0.618, 0.786, 1.27, etc.) miss 60-70% of valid reversals because:
- Real markets have volatility, slippage, and wicks
- Price respects **zones**, not exact levels
- Smart money operations distort perfect geometry

This indicator solves this by:
1. **Scoring each leg** on how close it matches the ideal ratio
2. **Weighting the AD ratio** as most critical (35% of total score)
3. **Dynamic tolerance** that adapts to market conditions
4. **Quality threshold** ensures only high-probability patterns show

### Configuration Guide

**For Crypto/High Volatility:**
```
Base Detection Margin: 8-12%
Dynamic Tolerance: ON
Min Quality Score: 75%
Trend Filter: ON
```

**For Forex:**
```
Base Detection Margin: 5-8%
Dynamic Tolerance: ON
Min Quality Score: 80%
Trend Filter: ON
```

**For Stocks (Daily):**
```
Base Detection Margin: 4-6%
Dynamic Tolerance: OFF
Min Quality Score: 75%
Trend Filter: ON
```

### Usage

1. **Copy** `harmonic_patterns_advanced.pine` into TradingView Pine Editor
2. **Add to chart** and configure settings for your market
3. **Wait for patterns** to complete at D-point (non-repainting)
4. **Check quality score** (aim for 75%+ minimum)
5. **Verify ICT confluence** (FVG or OB near D-point)
6. **Enter with confirmation** (price action or retest)

### Target Guidelines

From D-point completion:
- **Target 1**: 38.2% retracement of AD (quick profit)
- **Target 2**: 61.8% retracement of AD (conservative)  
- **Target 3**: Point A (full pattern reversal)
- **Target 4**: 161.8% extension of AD (home run)

Stop loss: 1-2 ATR beyond X-point

### Performance Expectations

| Setup Quality | Win Rate | Risk:Reward | Notes |
|---------------|----------|-------------|-------|
| Premium (85%+ score + ICT) | 70-80% | 1:3+ | Trending markets with confluence |
| Good (75-85% + trend filter) | 60-70% | 1:2 | Most conditions |
| Average (75% score only) | 50-60% | 1:1.5 | Mixed results |

### Documentation

For complete details on:
- Pattern specifications and ratios
- Scoring system explanation
- ICT confluence strategies
- Multi-timeframe analysis
- Common mistakes to avoid
- Advanced trading techniques

See **[HARMONIC_PATTERNS_GUIDE.md](./HARMONIC_PATTERNS_GUIDE.md)** for the full professional guide.

---

## 🚀 Getting Started

1. Choose your indicator based on your trading style:
   - **Candlestick Patterns**: For quick visual signals and classic patterns
   - **Harmonic Patterns**: For structured, high-probability reversal setups

2. Copy the `.pine` file into TradingView Pine Editor

3. Add to your chart and configure settings

4. Set up alerts for your preferred patterns

5. Backtest on historical data before live trading

---

## 📚 Resources

- **Harmonic Trading** by Scott Carney
- **Trade What You See** by Larry Pesavento  
- **ICT Concepts** by Inner Circle Trader
- TradingView Pine Script documentation

---

## ⚠️ Disclaimer

These indicators are tools for technical analysis. They do not guarantee profits. Always:
- Use proper risk management (1-2% per trade)
- Backtest before live trading
- Combine with other analysis methods
- Never risk more than you can afford to lose

---

## 📝 License

Open source for educational and personal use. Attribution appreciated if you modify or share.
