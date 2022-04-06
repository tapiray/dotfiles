map <up> <nop>
map <down> <nop>
map <left> <nop>
map <right> <nop>
imap <up> <nop>
imap <down> <nop>
imap <left> <nop>
imap <right> <nop>

colorscheme default
syntax on
filetype on
filetype indent on
filetype plugin on
filetype plugin indent on
set mouse=a
set number relativenumber
set tabstop=4
set expandtab
set nohlsearch
set nowrap
set incsearch
set signcolumn=no
set belloff=all
set shiftwidth=4
set nobackup
set ignorecase
set smartcase
set showcmd
set showmatch
set showmode
set history=1000
set scrolloff=10
set wildmenu
set wildmode=list:longest
set foldmethod=marker

autocmd Filetype python setlocal tabstop=4 shiftwidth=4 expandtab
autocmd BufReadPost *.rkt,*.rktl set filetype=racket
autocmd Filetype racket set lisp
autocmd Filetype racket setlocal tabstop=2 shiftwidth=2 expandtab

set statusline=
set statusline+=%F\ %M\ %Y\ %R
set statusline+=%=
set statusline+=ascii:\ %b\ hex:\ 0x%B\ row:\ %l\ col:\ %c\ percent:\ %p%%
set laststatus=2
