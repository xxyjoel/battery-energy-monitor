# 🚀 Quick Start Guide

Get up and running in 30 seconds!

## Fastest Method (No Installation)

```bash
# 1. Make executable
chmod +x battery_energy_monitor.py

# 2. Run it!
./battery_energy_monitor.py -m --compact
```

That's it! You'll see a real-time display of your battery and power usage.

## Three Usage Modes

### 1. Snapshot (one-time check)
```bash
./battery_energy_monitor.py
```
Shows current status once, then exits.

### 2. Full Monitor (detailed display)
```bash
./battery_energy_monitor.py -m
```
Real-time dashboard with all info. Perfect for keeping in a terminal window.

### 3. Compact Monitor (single line)
```bash
./battery_energy_monitor.py -m --compact
```
Minimal single-line display. Great for tmux status bars or side terminals.

## Installation (Optional)

Want to run it from anywhere?

```bash
# Run the installer
chmod +x install.sh
./install.sh

# Then use from anywhere
battery-monitor -m
```

## Launcher Menu (Easy Mode)

Don't remember the commands?

```bash
chmod +x launch.sh
./launch.sh
```

Interactive menu walks you through all options.

## First Time? Start Here

**New to terminal?** Try this:

```bash
# 1. Open Terminal app (⌘+Space, type "terminal")

# 2. Navigate to where you saved the files
cd ~/Downloads  # or wherever you saved them

# 3. Make it work
chmod +x battery_energy_monitor.py

# 4. Run the full monitor
./battery_energy_monitor.py -m

# 5. Stop it with: Ctrl+C
```

## Common Options

```bash
# Update every 2 seconds instead of 1
./battery_energy_monitor.py -m --interval 2

# Compact mode with custom interval
./battery_energy_monitor.py -m --compact --interval 0.5

# Get help
./battery_energy_monitor.py --help
```

## Need Sudo?

Power metrics require sudo. Just run once:
```bash
sudo -v
```

Then your monitor will work without asking for password for ~15 minutes.

## What You'll See

**Compact mode shows:**
```
🔋 85% │ CPU: 2.1W │ GPU: 0.8W │ Total: 3.2W │ 14:30:45
```

**Full mode shows:**
- Battery percentage bar
- Charging status
- Time remaining
- Battery health
- Cycle count
- CPU/GPU/ANE power
- Live timestamps

## Tips

1. **Keep it running**: Open a separate terminal window for monitoring
2. **Tmux/Screen**: Run in background with `tmux` or `screen`
3. **Battery testing**: Great for comparing different apps' battery impact
4. **Gaming**: See how much power your game actually uses
5. **Development**: Track power during builds/tests

## Troubleshooting

**"Permission denied"?**
```bash
chmod +x battery_energy_monitor.py
```

**Power metrics not showing?**
```bash
sudo ./battery_energy_monitor.py -m
```

**Too much flickering?**
```bash
./battery_energy_monitor.py -m --interval 2
```

## Next Steps

- Read [README.md](README.md) for full documentation
- Check [EXAMPLES.md](EXAMPLES.md) to see example outputs
- Run `./battery_energy_monitor.py --help` for all options

## One-Liner for Copy/Paste

```bash
chmod +x battery_energy_monitor.py && ./battery_energy_monitor.py -m --compact
```

That's it! You're monitoring your M4 Mac's battery and power in real-time. 🎉
