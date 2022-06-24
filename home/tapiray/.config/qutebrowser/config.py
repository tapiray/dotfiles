config.load_autoconfig(False)
c.content.autoplay = False
c.content.cookies.accept = 'all'
c.content.cookies.store = False
c.content.desktop_capture = False
c.content.geolocation = False
c.content.blocking.enabled = True
c.content.blocking.method = 'auto'
c.content.images = True
c.content.javascript.alert = False
c.content.javascript.enabled = True
c.content.javascript.prompt = False
c.content.notifications.enabled = False
c.completion.shrink = True
c.tabs.last_close = "close"
c.downloads.position = 'top'
c.hints.mode = 'letter'
c.keyhint.delay = 0
c.content.pdfjs = True
c.scrolling.bar = 'overlay'
c.scrolling.smooth = False
c.statusbar.show = 'in-mode'
c.statusbar.position = 'bottom'
c.statusbar.widgets = ['keypress', "progress", 'url']
c.tabs.position = 'top'
c.tabs.show_switching_delay = 0
c.tabs.show = "multiple"
c.url.default_page = 'https://start.duckduckgo.com'
c.url.searchengines = {'DEFAULT': 'https://duckduckgo.com/?q={}'}
c.url.start_pages = 'https://start.duckduckgo.com'
c.backend = "webengine"
c.colors.webpage.preferred_color_scheme = 'light'
c.colors.webpage.darkmode.enabled = False
c.colors.webpage.darkmode.policy.images = 'smart'
c.colors.webpage.darkmode.policy.page = 'always'
c.fonts.web.size.default = 20
c.fonts.web.size.default_fixed = 18
c.window.hide_decoration = True
c.completion.height = "30%"
c.completion.delay = 0
c.completion.min_chars = 1
c.completion.open_categories = ["searchengines", "bookmarks", "filesystem"]
c.completion.scrollbar.width = 0
c.completion.scrollbar.padding = 1
c.completion.shrink = True
c.completion.quick = True
c.completion.show = "always"
c.downloads.location.prompt = True
c.downloads.location.remember = False
c.content.private_browsing = True
c.tabs.close_mouse_button = "none"
c.tabs.close_mouse_button_on_bar = "ignore"
c.tabs.mode_on_change = "normal"
c.tabs.width = "10%"
c.tabs.tooltips = False
c.statusbar.padding = {"left": 0, "right": 0, "top": 0, "bottom": 0}
c.tabs.padding = {"left": 0, "right": 0, "top": 0, "bottom": 0}
c.aliases = {}
c.bindings.default = {
    "caret": {"<Escape>": "mode-leave", "<Space>": "selection-toggle", "G": "move-to-end-of-document", "H": "scroll left", "J": "scroll down", "K": "scroll up", "L": "scroll right", "V": "selection-toggle --line", "Y": "yank selection -s", "[": "move-to-start-of-prev-block", "]": "move-to-start-of-next-block", "b": "move-to-prev-word", "c": "mode-enter normal", "e": "move-to-end-of-word", "g": "move-to-start-of-document", "h": "move-to-prev-char", "j": "move-to-next-line", "k": "move-to-prev-line", "l": "move-to-next-char", "o": "selection-reverse", "v": "selection-toggle", "w": "move-to-next-word", "y": "yank selection", "{": "move-to-end-of-prev-block", "}": "move-to-end-of-next-block"},
    "command": {"<Alt-B>": "rl-backward-word", "<Alt-Backspace>": "rl-backward-kill-word", "<Alt-D>": "rl-kill-word", "<Alt-F>": "rl-forward-word", "<Ctrl-?>": "rl-delete-char", "<Ctrl-A>": "rl-beginning-of-line", "<Ctrl-B>": "rl-backward-char", "<Ctrl-C>": "completion-item-yank", "<Ctrl-D>": "completion-item-del", "<Ctrl-E>": "rl-end-of-line", "<Ctrl-F>": "rl-forward-char", "<Ctrl-H>": "rl-backward-delete-char", "<Ctrl-K>": "rl-kill-line", "<Ctrl-N>": "command-history-next", "<Ctrl-P>": "command-history-prev", "<Ctrl-Return>": "command-accept --rapid", "<Ctrl-Shift-C>": "completion-item-yank --sel", "<Ctrl-Shift-Tab>": "completion-item-focus prev-category", "<Ctrl-Shift-W>": "rl-filename-rubout", "<Ctrl-Tab>": "completion-item-focus next-category", "<Ctrl-U>": "rl-unix-line-discard", "<Ctrl-W>": "rl-rubout \" \"", "<Ctrl-Y>": "rl-yank", "<Down>": "completion-item-focus --history next", "<Escape>": "mode-leave", "<PgDown>": "completion-item-focus next-page", "<PgUp>": "completion-item-focus prev-page", "<Return>": "command-accept", "<Shift-Delete>": "completion-item-del", "<Shift-Tab>": "completion-item-focus prev", "<Tab>": "completion-item-focus next", "<Up>": "completion-item-focus --history prev"},
    "hint": {"<Ctrl-B>": "hint all tab-bg", "<Ctrl-F>": "hint links", "<Ctrl-R>": "hint --rapid links tab-bg", "<Escape>": "mode-leave", "<Return>": "hint-follow"},
    "insert": {"<Ctrl-E>": "edit-text", "<Escape>": "mode-leave", "<Shift-Escape>": "fake-key <Escape>", "<Shift-Ins>": "insert-text -- {primary}"},
    "normal": {"+": "zoom-in", "-": "zoom-out","/": "set-cmd-text /", ":": "set-cmd-text :", ";h": "hint all hover", ";d": "hint all download", ";r": "hint all delete", ";o": "hint all tab", ";y": "hint all yank", "<Alt-1>": "tab-focus 1", "<Alt-2>": "tab-focus 2", "<Alt-3>": "tab-focus 3", "<Alt-4>": "tab-focus 4", "<Alt-5>": "tab-focus 5", "<Alt-6>": "tab-focus 6", "<Alt-7>": "tab-focus 7", "<Alt-8>": "tab-focus 8", "<Alt-9>": "tab-focus 9", "<Alt-9>": "tab-focus -1", "<Alt-m>": "tab-mute", "<Alt-p>": "print", "<Alt-r>": "reload -f", "<Alt-PgDown>": "tab-next", "<Alt-PgUp>": "tab-prev", "<Alt-t>": "open -t -r", "<Alt-h>": "home", "<Escape>": "clear-keychain ;; search ;; fullscreen --leave", "=": "zoom", "@": "macro-run", "<Alt-d>": "tab-close", "G": "scroll-to-perc", "H": "back", "J": "tab-next", "K": "tab-prev", "L": "forward", "u": "undo -w", "V": "mode-enter caret ;; selection-toggle --line", "f": "hint", "b": "set-cmd-text -s :bookmark-load", "<Alt-c>": "tab-clone", "<Alt-g>": "tab-give", "g": "scroll-to-perc 0", "h": "scroll left", "i": "mode-enter insert", "j": "scroll down", "k": "scroll up", "l": "scroll right", "q": "macro-record", "v": "mode-enter caret", "y": "yank"},
    "prompt": {"<Alt-B>": "rl-backward-word", "<Alt-Backspace>": "rl-backward-kill-word", "<Alt-D>": "rl-kill-word", "<Alt-F>": "rl-forward-word", "<Alt-Shift-Y>": "prompt-yank --sel", "<Alt-Y>": "prompt-yank", "<Ctrl-?>": "rl-delete-char", "<Ctrl-A>": "rl-beginning-of-line", "<Ctrl-B>": "rl-backward-char", "<Ctrl-E>": "rl-end-of-line", "<Ctrl-F>": "rl-forward-char", "<Ctrl-H>": "rl-backward-delete-char", "<Ctrl-K>": "rl-kill-line", "<Ctrl-P>": "prompt-open-download --pdfjs", "<Ctrl-Shift-W>": "rl-filename-rubout", "<Ctrl-U>": "rl-unix-line-discard", "<Ctrl-W>": "rl-rubout \" \"", "<Ctrl-X>": "prompt-open-download", "<Ctrl-Y>": "rl-yank", "<Down>": "prompt-item-focus next", "<Escape>": "mode-leave", "<Return>": "prompt-accept", "<Shift-Tab>": "prompt-item-focus prev", "<Tab>": "prompt-item-focus next", "<Up>": "prompt-item-focus prev"},
    "register": {"<Escape>": "mode-leave"},
    "yesno": {"<Alt-Shift-Y>": "prompt-yank --sel", "<Alt-Y>": "prompt-yank", "<Return>": "prompt-accept", "<Escape>": "mode-leave", "N": "prompt-accept --save no", "Y": "prompt-accept --save yes", "n": "prompt-accept no", "y": "prompt-accept yes"}
}
