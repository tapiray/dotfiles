[[ $- != *i* ]] && return

export PS1="\e[0m$ "

alias ls="ls -A --color=auto --classify=auto --group-directories-first"
alias grep="grep --color=auto"
alias bat="cat /sys/class/power_supply/BAT*/capacity /sys/class/power_supply/BAT*/status"
alias clear="printf '\033c'"
alias vol="pactl get-sink-volume 0 && pactl get-sink-mute 0"
alias brn="intelbacklight -get"
alias irssi="irssi --home=$HOME/.config/irssi"
alias yt="ytfzf -t -f --type=all --thumbnail-quality=high --detach"
