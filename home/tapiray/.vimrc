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

set nocompatible
set number relativenumber
set tabstop=4
set softtabstop=4
set expandtab
if has("mouse")
  set mouse=a
endif
set nohlsearch
set nowrap
set notimeout
set incsearch
set signcolumn=no
set nostartofline
set belloff=all
set novisualbell
set noerrorbells
set shiftwidth=4
set nobackup
set nowb
set noswapfile
set ignorecase
set confirm
set smartcase
set showcmd
set showmatch
set showmode
set autoread
set history=0
set scrolloff=10
set wildmenu
set foldmethod=marker
set viminfo="NONE"

let g:netrw_dirhistmax=0

autocmd Filetype python setlocal tabstop=4 softtabstop=4 shiftwidth=4 expandtab
autocmd BufReadPost *.rkt,*.rktl set filetype=racket
autocmd Filetype racket set lisp
autocmd Filetype racket setlocal tabstop=2 shiftwidth=2 expandtab

set statusline=
set statusline+=%F\ %M\ %Y\ %R
set statusline+=%=
set statusline+=row:\ %l\ col:\ %c\ percent:\ %p%%
set laststatus=2
