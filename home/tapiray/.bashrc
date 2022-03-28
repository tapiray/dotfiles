[[ $- != *i* ]] && return

export PS1="\e[1;34m\W \e[0m$ "

alias ls="ls -A --color=auto --classify=auto --group-directories-first"
alias grep="grep --color=auto"
alias battery="cat /sys/class/power_supply/BAT*/capacity /sys/class/power_supply/BAT*/status"

