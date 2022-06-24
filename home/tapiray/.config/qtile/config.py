from typing import List
from libqtile import qtile
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

super_key = "mod4" # launching applications
alt_key = "mod1" # managing windows
control_key = "control" # managing workspaces

keys = [
    Key([alt_key], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([alt_key], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([alt_key], "j", lazy.layout.down(), desc="Move focus down"),
    Key([alt_key], "k", lazy.layout.up(), desc="Move focus up"),

    Key([alt_key, "shift"], "h", lazy.layout.shuffle_left(),  desc="Move window to the left"),
    Key([alt_key, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([alt_key, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([alt_key, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    Key([alt_key, control_key], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([alt_key, control_key], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([alt_key, control_key], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([alt_key, control_key], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([alt_key, control_key], "r", lazy.layout.normalize(), desc="Reset all window sizes"),

    Key([alt_key, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),

    Key([alt_key], "Return", lazy.next_layout(), desc="Toggle between layouts"),
    Key([alt_key], "Tab", lazy.window.toggle_fullscreen(), desc="Put the focused window to/from fullscreen mode."),
    Key([alt_key], "q", lazy.window.kill(), desc="Kill focused window"),

    Key([alt_key], "r", lazy.reload_config(), desc="Reload the config"),
]

groups = [Group("1", label="1"), Group("2", label="2"), Group("3", label="3"), Group("4", label="4"), Group("5", label="5"), Group("6", label="6"), Group("7", label="7"), Group("8", label="8"), Group("9", label="9"), Group("10", label="10")]

keys.extend([
    Key([control_key], "1", lazy.group[groups[0].name].toscreen(), desc="Switch to group 1"),
    Key([control_key], "2", lazy.group[groups[1].name].toscreen(), desc="Switch to group 2"),
    Key([control_key], "3", lazy.group[groups[2].name].toscreen(), desc="Switch to group 3"),
    Key([control_key], "4", lazy.group[groups[3].name].toscreen(), desc="Switch to group 4"),
    Key([control_key], "5", lazy.group[groups[4].name].toscreen(), desc="Switch to group 5"),
    Key([control_key], "6", lazy.group[groups[5].name].toscreen(), desc="Switch to group 6"),
    Key([control_key], "7", lazy.group[groups[6].name].toscreen(), desc="Switch to group 7"),
    Key([control_key], "8", lazy.group[groups[7].name].toscreen(), desc="Switch to group 8"),
    Key([control_key], "9", lazy.group[groups[8].name].toscreen(), desc="Switch to group 9"),
    Key([control_key], "0", lazy.group[groups[9].name].toscreen(), desc="Switch to group 10"),

    Key([alt_key, control_key], "1", lazy.window.togroup(groups[0].name, switch_group=True), desc="Switch to & move focused window to group 1"),
    Key([alt_key, control_key], "2", lazy.window.togroup(groups[1].name, switch_group=True), desc="Switch to & move focused window to group 2"),
    Key([alt_key, control_key], "3", lazy.window.togroup(groups[2].name, switch_group=True), desc="Switch to & move focused window to group 3"),
    Key([alt_key, control_key], "4", lazy.window.togroup(groups[3].name, switch_group=True), desc="Switch to & move focused window to group 4"),
    Key([alt_key, control_key], "5", lazy.window.togroup(groups[4].name, switch_group=True), desc="Switch to & move focused window to group 5"),
    Key([alt_key, control_key], "6", lazy.window.togroup(groups[5].name, switch_group=True), desc="Switch to & move focused window to group 6"),
    Key([alt_key, control_key], "7", lazy.window.togroup(groups[6].name, switch_group=True), desc="Switch to & move focused window to group 7"),
    Key([alt_key, control_key], "8", lazy.window.togroup(groups[7].name, switch_group=True), desc="Switch to & move focused window to group 8"),
    Key([alt_key, control_key], "9", lazy.window.togroup(groups[8].name, switch_group=True), desc="Switch to & move focused window to group 9"),
    Key([alt_key, control_key], "0", lazy.window.togroup(groups[9].name, switch_group=True), desc="Switch to & move focused window to group 10"),
])

floating_layout = layout.Floating(border_focus="000000", border_normal="ffffff", border_width=2)
layouts = [
    layout.Columns(border_focus="000000", border_normal="#ffffff", border_width=4, margin=4),
    layout.Floating(border_focus="000000", border_normal="ffffff", border_width=2)
]

screens = [Screen()]

mouse = [
    Drag([alt_key], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([alt_key], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
]

dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = False
cursor_warp = False
bring_front_click = True #"floating_only"
auto_fullscreen = False
focus_on_window_activation = "never"
reconfigure_screens = True
auto_minimize = False
