# Example Output

## Snapshot Mode

```
Battery & Energy Snapshot - 2025-11-01 14:30:45

Battery: ████████████████████████░░░░░░ 85% (Discharging)
Time Remaining: 4:32

Power Consumption:
  CPU:    2.1W
  GPU:    0.8W
  ANE:      0mW
  Total:  3.2W
```

## Full Monitoring Mode

```
======================================================================
  🔋 Battery & Energy Monitor                               14:30:45
======================================================================

  Battery Status
  🔋 On Battery
  ████████████████████████░░░░░░░░░░░░ 85%

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

## Compact Mode (Single Line - Updates in Place)

```
🔋 ████████████████████████░░░░  85% │ CPU:    2.1W │ GPU:    0.8W │ Total:    3.2W │ 14:30:45
```

## While Charging

```
⚡ ████████████████████████████░░  92% │ CPU:    1.8W │ GPU:    0.5W │ Total:    2.5W │ 14:35:22
```

## Low Battery Warning (Red)

```
🔋 ████░░░░░░░░░░░░░░░░░░░░░░░░  15% │ CPU:    3.2W │ GPU:    1.2W │ Total:    5.1W │ 16:45:10
```

## During Heavy GPU Use (Gaming/Video)

```
🔋 ██████████████░░░░░░░░░░░░░░  62% │ CPU:    8.5W │ GPU:   12.3W │ Total:   22.1W │ 15:22:33
```

## Color Coding Examples

- **Green** (>50% battery): Normal operation
- **Yellow** (20-50% battery): Warning zone
- **Red** (<20% battery): Critical - plug in soon!
- **Cyan** (charging): Currently plugged in and charging
- **Gray**: Timestamps and secondary info

## Real-World Scenarios

### Idle Mac
```
🔋 ████████████████████████████  95% │ CPU:    0.8W │ GPU:    0.1W │ Total:    1.2W │ 09:15:00
```

### Web Browsing (Safari)
```
🔋 ██████████████████████████░░  88% │ CPU:    2.1W │ GPU:    0.3W │ Total:    2.8W │ 10:30:15
```

### Video Streaming (YouTube 4K)
```
🔋 ████████████████████░░░░░░░░  75% │ CPU:    3.5W │ GPU:    2.1W │ Total:    6.2W │ 11:45:22
```

### Compiling Code
```
🔋 ████████████████████░░░░░░░░  72% │ CPU:   15.2W │ GPU:    0.4W │ Total:   17.8W │ 13:20:45
```

### Gaming
```
🔋 ██████████████░░░░░░░░░░░░░░  55% │ CPU:   18.5W │ GPU:   32.1W │ Total:   52.3W │ 14:55:10
```

### ML/AI Model Training
```
🔋 ██████████░░░░░░░░░░░░░░░░░░  45% │ CPU:   12.8W │ GPU:   28.4W │ Total:   45.2W │ 16:10:33
```

## Battery Health Indicators

### Excellent Health
```
  Cycle Count: 15
  Health: Normal
```

### Good (Higher Usage)
```
  Cycle Count: 342
  Health: Normal
```

### Warning
```
  Cycle Count: 987
  Health: Replace Soon
```

## Time Remaining Examples

### Long Battery Life (Light Use)
```
Time Remaining: 8:45
```

### Medium Battery Life (Normal Use)
```
Time Remaining: 4:32
```

### Short Battery Life (Heavy Use)
```
Time Remaining: 1:15
```

### Charging
```
Time Remaining: 2:30 until full
```

### Calculating (Just Unplugged)
```
Time Remaining: (Calculating...)
```
