#!/bin/bash

# Get a list of sudo users
sudo_users=$(cut -d: -f1,3 /etc/passwd | awk -F: '$2 >= 1000 {print $1}')

# Check if there are sudo users
if [ -z "$sudo_users" ]; then
    whiptail --title "No Sudo Users" --msgbox "There are no users with sudo privileges." 10 60
    exit 1
fi

# Create a list for the menu
menu_options=()
count=1
IFS=$'\n' # Set Internal Field Separator to newline to handle user names with spaces
for user_line in $sudo_users; do
    user=$(echo "$user_line" | cut -d: -f1)
    menu_options+=("$count" "$user")
    ((count++))
done

# Add a "Quit" option
menu_options+=("$count" "Quit")

# Display the menu
CHOICE=$(whiptail --title "Select Sudo User" --menu "Choose a sudo user for chroot environment who can access the hole system and other users in to chroot jail. " 15 60 $((count+1)) "${menu_options[@]}" 3>&1 1>&2 2>&3)

case $CHOICE in
    $count) 
        echo "Exiting"; exit 0;;
    *) 
        selected_user=$(echo "$sudo_users" | sed -n "${CHOICE}p" | cut -d: -f1)
        echo "You chose sudo user: $selected_user"

        # Append lines to /etc/ssh/sshd_config
        echo "" | sudo tee -a /etc/ssh/sshd_config
        echo "# Custom configuration for $selected_user" | sudo tee -a /etc/ssh/sshd_config
        echo "Protocol 2" | sudo tee -a /etc/ssh/sshd_config
        echo "Match User *,!$selected_user" | sudo tee -a /etc/ssh/sshd_config
        echo "   ChrootDirectory %h" | sudo tee -a /etc/ssh/sshd_config
        echo "" | sudo tee -a /etc/ssh/sshd_config

        # Restart SSH service
        sudo service ssh restart

        echo "Configuration updated for $selected_user";;
esac
