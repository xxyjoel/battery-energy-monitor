#!/bin/bash

# Real-Time Battery & Energy Monitor for Apple Silicon Macs
# Compact bash version

# Colors
RESET='\033[0m'
BOLD='\033[1m'
GREEN='\033[92m'
YELLOW='\033[93m'
RED='\033[91m'
CYAN='\033[96m'
GRAY='\033[90m'

# Configuration
INTERVAL=${1:-1}  # Default 1 second

# Function to get battery percentage
get_battery_percentage() {
    pmset -g batt | grep -Eo "\d+%" | cut -d'%' -f1
}

# Function to check if charging
is_charging() {
    pmset -g batt | grep -q "AC Power\|charging"
}

# Function to get time remaining
get_time_remaining() {
    pmset -g batt | grep -Eo "\d+:\d+" | head -1
}

# Function to format power
format_power() {
    local mw=$1
    if [ $mw -ge 1000 ]; then
        awk "BEGIN {printf \"%.2fW\", $mw/1000}"
    else
        printf "%4dmW" $mw
    fi
}

# Function to create battery bar
create_battery_bar() {
    local percentage=$1
    local width=20
    local filled=$(( percentage * width / 100 ))
    local empty=$(( width - filled ))
    
    printf "█%.0s" $(seq 1 $filled)
    printf "░%.0s" $(seq 1 $empty)
}

# Function to get battery color
get_battery_color() {
    local percentage=$1
    local charging=$2
    
    if [ "$charging" = "true" ]; then
        echo -e "${CYAN}"
    elif [ $percentage -gt 50 ]; then
        echo -e "${GREEN}"
    elif [ $percentage -gt 20 ]; then
        echo -e "${YELLOW}"
    else
        echo -e "${RED}"
    fi
}

# Clear screen
clear

echo -e "${BOLD}🔋 Battery & Energy Monitor${RESET}"
echo -e "${GRAY}Press Ctrl+C to stop${RESET}"
echo ""

# Main monitoring loop
while true; do
    # Get battery info
    BATTERY_PCT=$(get_battery_percentage)
    
    if is_charging; then
        CHARGING="true"
        STATUS_ICON="⚡"
    else
        CHARGING="false"
        STATUS_ICON="🔋"
    fi
    
    TIME_REMAINING=$(get_time_remaining)
    
    # Get power metrics
    POWER_OUTPUT=$(sudo powermetrics -n 1 --samplers cpu_power 2>/dev/null)
    
    CPU=$(echo "$POWER_OUTPUT" | grep "CPU Power:" | awk '{print $3}')
    GPU=$(echo "$POWER_OUTPUT" | grep "GPU Power:" | awk '{print $3}')
    ANE=$(echo "$POWER_OUTPUT" | grep "ANE Power:" | awk '{print $3}')
    TOTAL=$(echo "$POWER_OUTPUT" | grep "Combined Power" | awk '{print $5}')
    
    # Format power values
    CPU_FMT=$(format_power ${CPU:-0})
    GPU_FMT=$(format_power ${GPU:-0})
    ANE_FMT=$(format_power ${ANE:-0})
    TOTAL_FMT=$(format_power ${TOTAL:-0})
    
    # Get battery color
    BAT_COLOR=$(get_battery_color $BATTERY_PCT $CHARGING)
    
    # Create battery bar
    BAT_BAR=$(create_battery_bar $BATTERY_PCT)
    
    # Get timestamp
    TIMESTAMP=$(date '+%H:%M:%S')
    
    # Print status (overwrite previous line)
    printf "\r\033[K"
    printf "${STATUS_ICON} ${BAT_COLOR}${BAT_BAR} %3d%%${RESET} │ " $BATTERY_PCT
    printf "CPU: %8s │ GPU: %8s │ ANE: %8s │ Total: ${BOLD}%8s${RESET} │ ${GRAY}%s${RESET}" \
        "$CPU_FMT" "$GPU_FMT" "$ANE_FMT" "$TOTAL_FMT" "$TIMESTAMP"
    
    sleep $INTERVAL
done
