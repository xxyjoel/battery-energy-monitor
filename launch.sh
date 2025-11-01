#!/bin/bash

# Battery Monitor Launcher
# Simple wrapper to make it easy to start monitoring

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MONITOR="${SCRIPT_DIR}/battery_energy_monitor.py"

# Colors
GREEN='\033[92m'
CYAN='\033[96m'
GRAY='\033[90m'
RESET='\033[0m'

echo -e "${CYAN}🔋 Battery & Energy Monitor Launcher${RESET}\n"

# Check if Python script exists
if [ ! -f "$MONITOR" ]; then
    echo "Error: battery_energy_monitor.py not found"
    exit 1
fi

# Make sure it's executable
chmod +x "$MONITOR"

echo "Select mode:"
echo "  1) Snapshot (one-time check)"
echo "  2) Full monitoring (detailed display)"
echo "  3) Compact monitoring (single line)"
echo "  4) Custom interval"
echo ""
read -p "Choice [1-4]: " choice

case $choice in
    1)
        echo -e "\n${GREEN}Running snapshot...${RESET}\n"
        "$MONITOR"
        ;;
    2)
        echo -e "\n${GREEN}Starting full monitoring...${RESET}"
        echo -e "${GRAY}Press Ctrl+C to stop${RESET}\n"
        sleep 1
        "$MONITOR" -m
        ;;
    3)
        echo -e "\n${GREEN}Starting compact monitoring...${RESET}"
        echo -e "${GRAY}Press Ctrl+C to stop${RESET}\n"
        sleep 1
        "$MONITOR" -m --compact
        ;;
    4)
        read -p "Update interval (seconds): " interval
        echo -e "\n${GREEN}Starting monitoring with ${interval}s interval...${RESET}"
        echo -e "${GRAY}Press Ctrl+C to stop${RESET}\n"
        sleep 1
        "$MONITOR" -m --interval "$interval"
        ;;
    *)
        echo "Invalid choice"
        exit 1
        ;;
esac
