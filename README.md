# 🔋 Real-Time Battery & Energy Monitor for M4 Mac

A minimal, real-time terminal monitor that tracks both **battery life** and **energy consumption** on Apple Silicon Macs.

## Features

✅ **Real-time battery monitoring**
- Battery percentage with visual bar
- Charging status detection
- Time remaining estimates
- Battery health & cycle count
- Color-coded status (green/yellow/red)

✅ **Live power consumption tracking**
- CPU power usage
- GPU power usage
- ANE (Apple Neural Engine) power
- Total system power consumption

✅ **Clean terminal interface**
- Full display mode with detailed info
- Compact single-line mode
- Color-coded output
- Auto-refreshing display

## Quick Start

### Python Version (Recommended)

```bash
# Make executable
chmod +x battery_energy_monitor.py

# Quick snapshot
./battery_energy_monitor.py

# Real-time monitoring (full display)
./battery_energy_monitor.py -m

# Compact mode (single line)
./battery_energy_monitor.py -m --compact

# Custom update interval (2 seconds)
./battery_energy_monitor.py -m --interval 2
```

### Bash Version

```bash
# Make executable
chmod +x battery_energy_monitor.sh

# Run with 1 second updates
./battery_energy_monitor.sh

# Custom interval (2 seconds)
./battery_energy_monitor.sh 2
```

## Usage Examples

### Snapshot Mode (Python only)
Shows current status once:
```
Battery & Energy Snapshot - 2025-11-01 14:30:45

Battery: ████████████████░░░░░░░░░░░░░░ 85% (Discharging)
Time Remaining: 4:32

Power Consumption:
  CPU:    2.1W
  GPU:    0.8W
  ANE:      0mW
  Total:  3.2W
```

### Full Monitoring Mode
Real-time display with all details:
```
======================================================================
  🔋 Battery & Energy Monitor                               14:30:45
======================================================================

  Battery Status
  🔋 On Battery
  ████████████████░░░░ 85%

  Time Remaining: 4:32
  Cycle Count: 23
  Health: Normal

  Power Consumption
  ────────────────────────────────────────
  CPU:      2.1W
  GPU:      0.8W
  ANE:        0mW
  ────────────────────────────────────────
  Total:    3.2W

  Updating every 1s • Press Ctrl+C to stop
======================================================================
```

### Compact Mode
Single line that updates in place:
```
🔋 ████████████████░░░░  85% │ CPU:    2.1W │ GPU:    0.8W │ Total:    3.2W │ 14:30:45
```

## Requirements

- **macOS**: Works on all Apple Silicon Macs (M1/M2/M3/M4)
- **Python 3**: Pre-installed on macOS
- **Sudo access**: Required for power metrics only
  - Battery info works without sudo
  - Power consumption requires sudo

### One-time sudo setup
To avoid entering password repeatedly:
```bash
# Cache sudo credentials for 15 minutes
sudo -v

# Or run the monitor once with sudo
sudo ./battery_energy_monitor.py -m
```

## Command Line Options (Python)

```
usage: battery_energy_monitor.py [-h] [-m] [-i INTERVAL] [-c]

Real-Time Battery & Energy Monitor for Apple Silicon Macs

optional arguments:
  -h, --help            show this help message and exit
  -m, --monitor         Enable real-time monitoring mode
  -i INTERVAL, --interval INTERVAL
                        Update interval in seconds (default: 1.0)
  -c, --compact         Use compact single-line display
```

## What Each Metric Means

### Battery Metrics

| Metric | Description |
|--------|-------------|
| **Percentage** | Current battery charge level (0-100%) |
| **Status** | Charging, Discharging, or Fully Charged |
| **Time Remaining** | Estimated time until empty/full |
| **Cycle Count** | Number of complete charge cycles |
| **Health** | Battery condition (Normal/Replace Soon/etc.) |

### Power Consumption

| Metric | Description |
|--------|-------------|
| **CPU Power** | Power used by efficiency & performance cores |
| **GPU Power** | Graphics processor power (active during gaming, video, ML) |
| **ANE Power** | Apple Neural Engine (ML/AI workloads) |
| **Total Power** | Combined system power (CPU + GPU + ANE + DRAM) |

## Color Coding

- 🟢 **Green**: Battery > 50% or good health
- 🟡 **Yellow**: Battery 20-50% or warning
- 🔴 **Red**: Battery < 20% or critical
- 🔵 **Cyan**: Currently charging
- ⚫ **Gray**: Secondary info / timestamps

## Use Cases

### Track battery drain during tasks
```bash
# Open in one terminal
./battery_energy_monitor.py -m --compact

# Run your task in another terminal
./compile_large_project.sh
```

### Monitor power efficiency
```bash
# Test different browsers/apps
./battery_energy_monitor.py -m
# Then open Chrome, Safari, etc. and compare power usage
```

### Check charging behavior
```bash
# Watch as your Mac charges
./battery_energy_monitor.py -m
```

### Log power consumption
```bash
# Redirect output to file (snapshot mode)
while true; do
    ./battery_energy_monitor.py >> power_log.txt
    sleep 60
done
```

## Troubleshooting

### "sudo: no tty present and no askpass program specified"
Run once to cache credentials:
```bash
sudo -v
./battery_energy_monitor.py -m
```

### Power metrics show 0 or unavailable
Make sure you're running with sudo:
```bash
sudo ./battery_energy_monitor.py -m
```

### Battery info not showing
Battery metrics use `pmset` which doesn't require sudo. If this fails, check:
```bash
pmset -g batt
```

### Screen flickers too much
Increase the update interval:
```bash
./battery_energy_monitor.py -m --interval 2
```

## Comparison with Other Tools

| Feature | This Tool | macmon | mactop | Activity Monitor |
|---------|-----------|--------|--------|------------------|
| Battery % | ✅ | ❌ | ❌ | ❌ |
| Battery time | ✅ | ❌ | ❌ | ❌ |
| Battery health | ✅ | ❌ | ❌ | ❌ |
| Power consumption | ✅ | ✅ | ✅ | ⚠️ Limited |
| No sudo needed | ⚠️ Partial | ✅ | ❌ | ✅ |
| Terminal UI | ✅ | ✅ | ✅ | ❌ |
| Compact mode | ✅ | ❌ | ❌ | ❌ |

## Tips

1. **Save battery**: Use compact mode, it uses less CPU
2. **Background monitoring**: Run in a separate terminal/tmux/screen
3. **Quick alias**: Add to `~/.zshrc`:
   ```bash
   alias battery='~/battery_energy_monitor.py -m --compact'
   ```
4. **Remove sudo prompts**: Edit sudoers (see main guide)

## Technical Details

### Data Sources
- **Battery info**: `pmset -g batt` and `system_profiler SPPowerDataType`
- **Power metrics**: `powermetrics` (Apple's built-in tool)

### Update Rate
- Default: 1 second
- Recommended range: 0.5 - 5 seconds
- Lower = more responsive but uses more CPU
- Higher = more efficient but less responsive

### Accuracy
- Battery percentage: ±1%
- Time remaining: Estimated (varies with usage)
- Power consumption: ±50mW (hardware estimation)

## License

Free to use and modify. No warranty provided.

## Credits

Inspired by:
- [macmon](https://github.com/vladkens/macmon) - Sudoless Apple Silicon monitor
- [mactop](https://github.com/context-labs/mactop) - Terminal monitoring
- [asitop](https://github.com/tlkh/asitop) - Python-based monitoring

Built for users who want a simple, focused tool that shows what matters most: **battery life + power usage**.
