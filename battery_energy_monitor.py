#!/usr/bin/env python3
"""
Real-Time Battery & Energy Monitor for Apple Silicon Macs
Displays battery status, charge level, and power consumption
"""

import subprocess
import re
import time
import sys
from datetime import datetime

# ANSI color codes
class Colors:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    CYAN = '\033[96m'
    GRAY = '\033[90m'

def get_battery_info():
    """Get detailed battery information"""
    try:
        result = subprocess.run(
            ['pmset', '-g', 'batt'],
            capture_output=True,
            text=True,
            timeout=2
        )
        
        output = result.stdout
        
        # Parse battery percentage
        percentage_match = re.search(r'(\d+)%', output)
        percentage = int(percentage_match.group(1)) if percentage_match else 0
        
        # Parse charging status
        is_charging = 'AC Power' in output or 'charging' in output.lower()
        is_charged = 'charged' in output.lower()
        
        # Parse time remaining
        time_remaining = None
        time_match = re.search(r'(\d+:\d+)', output)
        if time_match:
            time_remaining = time_match.group(1)
        
        # Get cycle count and health
        health_result = subprocess.run(
            ['system_profiler', 'SPPowerDataType'],
            capture_output=True,
            text=True,
            timeout=3
        )
        
        health_output = health_result.stdout
        cycle_match = re.search(r'Cycle Count:\s+(\d+)', health_output)
        condition_match = re.search(r'Condition:\s+(.+)', health_output)
        
        cycle_count = int(cycle_match.group(1)) if cycle_match else None
        condition = condition_match.group(1).strip() if condition_match else None
        
        return {
            'percentage': percentage,
            'is_charging': is_charging,
            'is_charged': is_charged,
            'time_remaining': time_remaining,
            'cycle_count': cycle_count,
            'condition': condition
        }
    except Exception as e:
        print(f"Error reading battery info: {e}", file=sys.stderr)
        return None

def get_power_metrics():
    """Get power consumption metrics"""
    try:
        result = subprocess.run(
            ['sudo', 'powermetrics', '-n', '1', '--samplers', 'cpu_power'],
            capture_output=True,
            text=True,
            timeout=3
        )
        
        output = result.stdout
        
        # Extract power values
        cpu_power = re.search(r'CPU Power:\s+(\d+)\s+mW', output)
        gpu_power = re.search(r'GPU Power:\s+(\d+)\s+mW', output)
        ane_power = re.search(r'ANE Power:\s+(\d+)\s+mW', output)
        combined = re.search(r'Combined Power.*?:\s+(\d+)\s+mW', output)
        
        return {
            'cpu': int(cpu_power.group(1)) if cpu_power else 0,
            'gpu': int(gpu_power.group(1)) if gpu_power else 0,
            'ane': int(ane_power.group(1)) if ane_power else 0,
            'total': int(combined.group(1)) if combined else 0
        }
    except Exception as e:
        return None

def format_power(mw):
    """Convert milliwatts to watts for display"""
    if mw >= 1000:
        return f"{mw/1000:.2f}W"
    else:
        return f"{mw:>4}mW"

def get_battery_color(percentage, is_charging):
    """Get color based on battery level"""
    if is_charging:
        return Colors.CYAN
    elif percentage > 50:
        return Colors.GREEN
    elif percentage > 20:
        return Colors.YELLOW
    else:
        return Colors.RED

def create_battery_bar(percentage, width=20):
    """Create a visual battery bar"""
    filled = int((percentage / 100) * width)
    empty = width - filled
    return '█' * filled + '░' * empty

def clear_screen():
    """Clear the terminal screen"""
    print('\033[2J\033[H', end='')

def monitor_realtime(interval=1.0, compact=False):
    """Real-time monitoring of battery and energy"""
    
    # Check if sudo access is available
    try:
        subprocess.run(
            ['sudo', '-n', 'true'],
            capture_output=True,
            timeout=1
        )
    except:
        print(f"{Colors.YELLOW}⚠️  This tool requires sudo access for power metrics.{Colors.RESET}")
        print(f"{Colors.GRAY}Run: sudo -v{Colors.RESET}\n")
    
    try:
        iteration = 0
        while True:
            # Only clear screen periodically to reduce flicker
            if iteration % 10 == 0 or iteration == 0:
                clear_screen()
            
            battery = get_battery_info()
            power = get_power_metrics()
            
            timestamp = datetime.now().strftime('%H:%M:%S')
            
            if not compact:
                # Full display mode
                print(f"{Colors.BOLD}{'=' * 70}{Colors.RESET}")
                print(f"{Colors.BOLD}  🔋 Battery & Energy Monitor{Colors.RESET}                    {Colors.GRAY}{timestamp}{Colors.RESET}")
                print(f"{Colors.BOLD}{'=' * 70}{Colors.RESET}\n")
                
                if battery:
                    color = get_battery_color(battery['percentage'], battery['is_charging'])
                    bar = create_battery_bar(battery['percentage'])
                    
                    # Battery status icon
                    if battery['is_charged']:
                        status_icon = "⚡ Fully Charged"
                    elif battery['is_charging']:
                        status_icon = "🔌 Charging"
                    else:
                        status_icon = "🔋 On Battery"
                    
                    print(f"  {Colors.BOLD}Battery Status{Colors.RESET}")
                    print(f"  {status_icon}")
                    print(f"  {color}{bar} {battery['percentage']}%{Colors.RESET}\n")
                    
                    # Additional battery info
                    if battery['time_remaining']:
                        print(f"  Time Remaining: {battery['time_remaining']}")
                    
                    if battery['cycle_count'] is not None:
                        print(f"  Cycle Count: {battery['cycle_count']}")
                    
                    if battery['condition']:
                        health_color = Colors.GREEN if battery['condition'] == 'Normal' else Colors.YELLOW
                        print(f"  Health: {health_color}{battery['condition']}{Colors.RESET}")
                    
                    print()
                
                if power:
                    print(f"  {Colors.BOLD}Power Consumption{Colors.RESET}")
                    print(f"  {'─' * 40}")
                    print(f"  CPU:   {format_power(power['cpu']):>8}")
                    print(f"  GPU:   {format_power(power['gpu']):>8}")
                    print(f"  ANE:   {format_power(power['ane']):>8}")
                    print(f"  {'─' * 40}")
                    print(f"  {Colors.BOLD}Total: {format_power(power['total']):>8}{Colors.RESET}\n")
                else:
                    print(f"  {Colors.YELLOW}⚠️  Power metrics unavailable (sudo required){Colors.RESET}\n")
                
                print(f"{Colors.GRAY}  Updating every {interval}s • Press Ctrl+C to stop{Colors.RESET}")
                print(f"{Colors.BOLD}{'=' * 70}{Colors.RESET}")
            
            else:
                # Compact mode - single line
                if battery and power:
                    color = get_battery_color(battery['percentage'], battery['is_charging'])
                    status = "⚡" if battery['is_charging'] else "🔋"
                    
                    sys.stdout.write('\r\033[K')  # Clear line
                    sys.stdout.write(
                        f"{status} {color}{battery['percentage']:>3}%{Colors.RESET} │ "
                        f"CPU: {format_power(power['cpu']):>7} │ "
                        f"GPU: {format_power(power['gpu']):>7} │ "
                        f"Total: {format_power(power['total']):>7} │ "
                        f"{Colors.GRAY}{timestamp}{Colors.RESET}"
                    )
                    sys.stdout.flush()
            
            time.sleep(interval)
            iteration += 1
            
    except KeyboardInterrupt:
        print(f"\n\n{Colors.GREEN}✓ Monitoring stopped{Colors.RESET}")
        sys.exit(0)

def show_snapshot():
    """Show a single snapshot of current status"""
    battery = get_battery_info()
    power = get_power_metrics()
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    print(f"\n{Colors.BOLD}Battery & Energy Snapshot{Colors.RESET} - {timestamp}\n")
    
    if battery:
        color = get_battery_color(battery['percentage'], battery['is_charging'])
        bar = create_battery_bar(battery['percentage'], 30)
        status = "Charging" if battery['is_charging'] else "Discharging"
        
        print(f"Battery: {color}{bar} {battery['percentage']}%{Colors.RESET} ({status})")
        if battery['time_remaining']:
            print(f"Time Remaining: {battery['time_remaining']}")
        print()
    
    if power:
        print("Power Consumption:")
        print(f"  CPU: {format_power(power['cpu']):>8}")
        print(f"  GPU: {format_power(power['gpu']):>8}")
        print(f"  ANE: {format_power(power['ane']):>8}")
        print(f"  Total: {Colors.BOLD}{format_power(power['total']):>8}{Colors.RESET}")
    
    print()

def main():
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Real-Time Battery & Energy Monitor for Apple Silicon Macs',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                        # Single snapshot
  %(prog)s -m                     # Real-time monitoring (full display)
  %(prog)s -m --compact           # Real-time monitoring (compact)
  %(prog)s -m --interval 2        # Update every 2 seconds
        """
    )
    
    parser.add_argument(
        '-m', '--monitor',
        action='store_true',
        help='Enable real-time monitoring mode'
    )
    
    parser.add_argument(
        '-i', '--interval',
        type=float,
        default=1.0,
        help='Update interval in seconds (default: 1.0)'
    )
    
    parser.add_argument(
        '-c', '--compact',
        action='store_true',
        help='Use compact single-line display'
    )
    
    args = parser.parse_args()
    
    if args.monitor:
        monitor_realtime(args.interval, args.compact)
    else:
        show_snapshot()

if __name__ == '__main__':
    main()
