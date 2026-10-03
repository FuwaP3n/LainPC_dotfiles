# Affected apps
Theme is made for tmux vim users so tmux and vim are changed a little bit. Terminal emulator is kitty. And session manager is ly.
# Required apps
i3-wm,
i3status,
picom,
rofi,
feh

fastfetch

magick - for screenshots
# Wallpapers
All of the wallpapers that I used is from this site https://fauux.neocities.org/ that was made by fauux.
His youtube channel https://www.youtube.com/@fauux and his about me page https://fauux.neocities.org/AboutMe
# Font
For terminal im using Iosevka and for status bar it is Terminus. You must install them manually.
# Setup
Just drop contents of .config dir into yours and everything else(except ly dir) into home directory, also check files .config/i3/paper.py(you need to change USERNAME to yours), .config/i3/init.sh (There is some lines of code for keyboard and multiple monitor setup).
Check .config/i3status/config to change VPN info to WIFI info, for example, and check .config/picom/config to change opacity

You should also make changes in .config/i3/config file, because it has some crazy keybindings.


# Quick notes
win+r to change wallpaper(It is also changed whenever i3 restarted)

win+shift+s for a screenshot(It is automatically saved in Pictures/Screenshot.png)

Window switching is using same keys as in vim(hjkl)

win+d for rofi

win+b for browser(default is flatpak zen)

win+alt+w for tab mode

win+alt+s for stack mode

win+alt+e for normal mode

win+w for resize mode

## tmux changes
ctrl+space to enter command mode or how does it called
Also vim theme is only working inside tmux idk why and I don't really care
