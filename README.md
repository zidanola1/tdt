# tdt

## Re-anchor CLI

This repository includes a simple CLI to "re-anchor" at a configured anchor time.

- re-anchor is toggled by `re_anchor: true`
- DFR is toggled by `dfr: true`
- Anchor time is defined as `anchor_time: "17:00"`

### Configuration

Edit `config.yaml`:

```yaml
re_anchor: true
dfr: true
anchor_time: "17:00"
```

### Install

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Usage

```bash
python -m app.reanchor --config config.yaml
```

Optional overrides for testing:

```bash
python -m app.reanchor --now 2025-10-15T16:30:00 --tz 0
python -m app.reanchor --now 2025-10-15T18:00:00 --tz 0
```

The program prints a YAML summary including the computed `next_anchor` datetime.
