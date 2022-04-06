setxkbmap tr
xset -b
xset r rate 300 50
xinput set-prop 13 311 1
xrdb -load ~/.Xresources
feh --bg-fill --no-fehbg /usr/share/wallpapers/sunset_deer.jpg
qtile start
