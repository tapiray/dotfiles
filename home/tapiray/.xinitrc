setxkbmap tr &
xset -b &
xset r rate 300 50 &
xinput set-prop 13 303 1 &
xinput set-prop 13 313 0 &
picom --experimental-backends --config ~/.config/picom/picom.conf &
xwallpaper --stretch /usr/share/wallpapers/the_tower_of_babel.jpg &
sxhkd -c ~/.config/sxhkd/sxhkdrc &
bspwm -c ~/.config/bspwm/bspwmrc
