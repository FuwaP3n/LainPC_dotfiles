#!/bin/bash

#Monitors setup
#xrandr --output DP-1 --primary
#xrandr --output HDMI-1 --right-of DP-1

#Keyboard setup
#setxkbmap -layout us,ee,ru
#setxkbmap -variant ,,
#setxkbmap -option grp:caps_toggle

#Turn auto monitor shutdown a.k.a screensaver
#xset -dpms s off

#Thingy to randomly change your wallpaper
python ~/.config/i3/paper.py

#Picom setup
picom --config ~/.config/picom/config

