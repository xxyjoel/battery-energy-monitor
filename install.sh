#!/bin/bash

# Installation script for Battery & Energy Monitor

set -e

INSTALL_DIR="${HOME}/.local/bin"
SCRIPT_NAME="battery-monitor"

# Colors
GREEN='\033[92m'
YELLOW='\033[93m'
CYAN='\033[96m'
RESET='\033[0m'

echo -e "${CYAN}╔════════════════════════════════════════════╗${RESET}"
echo -e "${CYAN}║  Battery & Energy Monitor - Installation  ║${RESET}"
echo -e "${CYAN}╚════════════════════════════════════════════╝${RESET}\n"

# Create install directory if it doesn't exist
if [ ! -d "$INSTALL_DIR" ]; then
    echo -e "${YELLOW}Creating installation directory: ${INSTALL_DIR}${RESET}"
    mkdir -p "$INSTALL_DIR"
fi

# Copy the Python script
echo -e "${GREEN}Installing monitor script...${RESET}"
cp battery_energy_monitor.py "${INSTALL_DIR}/${SCRIPT_NAME}"
chmod +x "${INSTALL_DIR}/${SCRIPT_NAME}"

echo -e "${GREEN}✓ Installed to ${INSTALL_DIR}/${SCRIPT_NAME}${RESET}\n"

# Check if directory is in PATH
if [[ ":$PATH:" != *":${INSTALL_DIR}:"* ]]; then
    echo -e "${YELLOW}⚠️  ${INSTALL_DIR} is not in your PATH${RESET}"
    echo -e "${YELLOW}Add this line to your ~/.zshrc or ~/.bashrc:${RESET}\n"
    echo -e "    export PATH=\"\${HOME}/.local/bin:\${PATH}\"\n"
    echo -e "Then run: ${CYAN}source ~/.zshrc${RESET} (or ~/.bashrc)\n"
else
    echo -e "${GREEN}✓ Installation directory is in PATH${RESET}\n"
fi

# Create helpful aliases
echo -e "${CYAN}Suggested aliases for your shell config:${RESET}\n"
echo "    alias battery='${SCRIPT_NAME}'"
echo "    alias battery-monitor='${SCRIPT_NAME} -m'"
echo "    alias battery-compact='${SCRIPT_NAME} -m --compact'"
echo ""

# Setup sudo passwordless (optional)
echo -e "${YELLOW}Optional: Setup passwordless sudo for powermetrics${RESET}"
echo -e "This allows monitoring without entering password repeatedly.\n"
read -p "Configure now? (y/N): " response

if [[ "$response" =~ ^[Yy]$ ]]; then
    echo ""
    echo -e "${GREEN}Adding sudoers entry...${RESET}"
    SUDOERS_LINE="${USER} ALL=(ALL) NOPASSWD: /usr/bin/powermetrics"
    
    # Check if entry already exists
    if sudo grep -q "powermetrics" /etc/sudoers.d/powermetrics 2>/dev/null; then
        echo -e "${YELLOW}Sudoers entry already exists${RESET}"
    else
        echo "$SUDOERS_LINE" | sudo tee /etc/sudoers.d/powermetrics > /dev/null
        sudo chmod 0440 /etc/sudoers.d/powermetrics
        echo -e "${GREEN}✓ Passwordless sudo configured for powermetrics${RESET}"
    fi
fi

echo ""
echo -e "${GREEN}╔════════════════════════════════════════╗${RESET}"
echo -e "${GREEN}║        Installation Complete! 🎉       ║${RESET}"
echo -e "${GREEN}╚════════════════════════════════════════╝${RESET}\n"

echo "Quick start:"
echo "  ${CYAN}${SCRIPT_NAME}${RESET}              - Quick snapshot"
echo "  ${CYAN}${SCRIPT_NAME} -m${RESET}           - Full monitoring"
echo "  ${CYAN}${SCRIPT_NAME} -m --compact${RESET} - Compact mode"
echo ""
echo "For help: ${CYAN}${SCRIPT_NAME} --help${RESET}"
echo ""
