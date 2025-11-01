# 📦 Battery & Energy Monitor - File Index

Complete real-time battery and energy monitoring for your M4 Mac.

## 🎯 Start Here

**New user?** → [QUICKSTART.md](QUICKSTART.md)  
Get running in 30 seconds with simple copy/paste commands.

## 📂 Files Overview

### 🚀 Main Applications

| File | Description | When to Use |
|------|-------------|-------------|
| **battery_energy_monitor.py** | Main Python app (recommended) | Most flexible, full features |
| **battery_energy_monitor.sh** | Bash version | If you prefer bash scripts |
| **launch.sh** | Interactive launcher menu | Easy mode - no commands to remember |
| **install.sh** | System installer | To use from anywhere on your system |

### 📖 Documentation

| File | Description | Read If... |
|------|-------------|------------|
| **QUICKSTART.md** | 30-second setup guide | You want to start immediately |
| **README.md** | Complete documentation | You want full details and options |
| **EXAMPLES.md** | Visual output examples | You want to see what it looks like |
| **INDEX.md** | This file! | You're figuring out what's what |

## 🎮 Usage Quick Reference

```bash
# Snapshot (one-time check)
./battery_energy_monitor.py

# Real-time full display
./battery_energy_monitor.py -m

# Real-time compact (single line)
./battery_energy_monitor.py -m --compact

# Interactive menu
./launch.sh

# Install system-wide
./install.sh
```

## 💡 Which File Should I Use?

### Just want to try it?
→ Use **battery_energy_monitor.py** with `-m --compact`

### Want detailed monitoring?
→ Use **battery_energy_monitor.py** with `-m`

### Don't like Python?
→ Use **battery_energy_monitor.sh** instead

### Want easy mode?
→ Run **launch.sh** for interactive menu

### Want it system-wide?
→ Run **install.sh** to install permanently

## 📊 What Does It Show?

### Battery Info
- Current charge percentage (0-100%)
- Visual battery bar indicator
- Charging/discharging status
- Time remaining estimate
- Battery health status
- Cycle count

### Power Consumption
- CPU power usage
- GPU power usage
- ANE (Neural Engine) power
- Total system power draw

All updated in real-time!

## 🛠️ System Requirements

- **macOS**: Any Apple Silicon Mac (M1/M2/M3/M4)
- **Python**: 3.x (pre-installed on macOS)
- **Sudo**: Required for power metrics only
- **Terminal**: Any terminal app works

## 📝 File Details

### battery_energy_monitor.py (11 KB)
- Language: Python 3
- Features: Full + compact modes, color output, timestamps
- Sudo: Required for power metrics
- Dependencies: None (uses built-in libraries)

### battery_energy_monitor.sh (3 KB)
- Language: Bash
- Features: Compact mode, color output
- Sudo: Required for power metrics
- Dependencies: Standard Unix tools

### launch.sh (1.6 KB)
- Language: Bash
- Purpose: Interactive menu launcher
- Makes it easy to pick options without remembering commands

### install.sh (3.3 KB)
- Language: Bash
- Purpose: System-wide installation
- Installs to: ~/.local/bin/battery-monitor
- Optional: Can setup passwordless sudo

## 🎨 Output Modes

### Snapshot Mode
Single check, then exits:
```
Battery: ████████████████░░░░  85% (Discharging)
Power: CPU 2.1W | GPU 0.8W | Total 3.2W
```

### Full Monitor Mode
Complete dashboard:
```
======================================
🔋 Battery & Energy Monitor  14:30:45
======================================

Battery Status: 🔋 On Battery
████████████████░░░░  85%
Time Remaining: 4:32

Power Consumption
CPU:    2.1W
GPU:    0.8W
Total:  3.2W
======================================
```

### Compact Monitor Mode
Single updating line:
```
🔋 85% │ CPU: 2.1W │ GPU: 0.8W │ Total: 3.2W │ 14:30:45
```

## 🔧 Common Tasks

### Quick Battery Check
```bash
./battery_energy_monitor.py
```

### Monitor While Working
```bash
./battery_energy_monitor.py -m --compact
# Keep running in separate terminal
```

### Test App Battery Impact
```bash
# Terminal 1: Start monitoring
./battery_energy_monitor.py -m

# Terminal 2: Run your app
./my-app
```

### Install Permanently
```bash
./install.sh
# Then use: battery-monitor -m
```

## 📚 Learning Path

1. **Start**: Read [QUICKSTART.md](QUICKSTART.md)
2. **Try**: Run `./battery_energy_monitor.py -m --compact`
3. **Explore**: Check [EXAMPLES.md](EXAMPLES.md) for output examples
4. **Deep Dive**: Read full [README.md](README.md) for all features
5. **Install**: Run `./install.sh` if you like it

## ❓ Help & Troubleshooting

**Need help?**
```bash
./battery_energy_monitor.py --help
```

**Common issues?**  
Check the Troubleshooting section in [README.md](README.md)

**Want examples?**  
See [EXAMPLES.md](EXAMPLES.md) for various scenarios

## 🎁 What's Different?

Unlike other tools:
- ✅ Shows **both** battery life **and** power consumption
- ✅ Multiple display modes (snapshot/full/compact)
- ✅ Clean, colored terminal output
- ✅ Easy installation with no complex setup
- ✅ Works on all Apple Silicon Macs
- ✅ Comprehensive documentation
- ✅ No bloat - just the essentials

## 🚀 Next Steps

1. Read [QUICKSTART.md](QUICKSTART.md) (2 min read)
2. Run `./battery_energy_monitor.py -m --compact`
3. Enjoy real-time battery and power monitoring!

---

Made for users who want to know exactly how much battery they have and how much power they're using - in real time, with zero bloat.
