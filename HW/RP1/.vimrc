set nocompatible
filetype off

set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

Plugin 'VundleVim/Vundle.vim'
Plugin 'delimitMate.vim'

call vundle#end()
filetype plugin indent on


set nu
set ts=4
set sw=4
set ls=2
set cindent
set autoindent
syntax on

let delimitMate_expand_cr=1

