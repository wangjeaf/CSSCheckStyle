"=============================================================================
" File: fixstyle.vim
" Author: zhifu.wang(wangjeaf@gmail.com)
" WebPage: https://github.com/wangjeaf/CSSCheckStyle
" License: MIT
if &cp || exists("loaded_fixcssstyle")
    finish
endif
let loaded_fixcssstyle = 1

function! s:is_css()
	return expand("%:e") == "css"
endfunction

function! g:Fixstyle(a)
	if !s:is_css()
		echo "Not a CSS file."
		return
	endif

    let ret = system("fixstyle -p ".expand('%:t'))

	:g/.*/d
	let @0 = ret
	:put!0
endfunction

function! g:FixstyleSafe(a)
	if !s:is_css()
		echo "Not a CSS file."
		return
	endif

    let ret = system("fixstyle -p --safeMode ".expand('%:t'))

	:g/.*/d
	let @0 = ret
	:put!0
endfunction

function! g:CssCompress(a)
	if !s:is_css()
		echo "Not a CSS file."
		return
	endif

    let ret = system("csscompress -p ".expand('%:t'))

	:g/.*/d
	let @0 = ret
	:put!0
endfunction

command! -nargs=? -range=% Fixstyle :call g:Fixstyle(<count>, <f-args>)
command! -nargs=? -range=% FixstyleSafe :call g:FixstyleSafe(<count>, <f-args>)
command! -nargs=? -range=% CssCompress :call g:CssCompress(<count>, <f-args>)
