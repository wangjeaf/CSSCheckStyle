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

    let ret = system("ckstyle fix -p ".expand('%:t'))

	:g/.*/d
	let @0 = ret
	:put!0
endfunction

function! g:FixstyleSingleLine(a)
	if !s:is_css()
		echo "Not a CSS file."
		return
	endif

    let ret = system("ckstyle fix -p --singleLine ".expand('%:t'))

	:g/.*/d
	let @0 = ret
	:put!0
endfunction

function! g:FixstyleSafe(a)
	if !s:is_css()
		echo "Not a CSS file."
		return
	endif

    let ret = system("ckstyle fix -p --safeMode ".expand('%:t'))

	:g/.*/d
	let @0 = ret
	:put!0
endfunction

function! g:Ckstyle(a)
	if !s:is_css()
		echo "Not a CSS file."
		return
	endif

    let ret = system("ckstyle check ".expand('%:t'))
    if filereadable("".expand('%:t').".ckstyle.txt")
        echo "[ckstyle] has error, @see ".expand('%:t').".ckstyle.txt"
    else
        echo "[ckstyle] No mistake found in this CSS, NB!"
    endif

endfunction

function! g:CssCompress(a)
	if !s:is_css()
		echo "Not a CSS file."
		return
	endif

    let ret = system("ckstyle compress -p ".expand('%:t'))

	:g/.*/d
	let @0 = ret
	:put!0
endfunction

command! -nargs=? -range=% Fixstyle :call g:Fixstyle(<count>, <f-args>)
command! -nargs=? -range=% FixstyleSafe :call g:FixstyleSafe(<count>, <f-args>)
command! -nargs=? -range=% FixstyleSingleLine :call g:FixstyleSingleLine(<count>, <f-args>)
command! -nargs=? -range=% CssCompress :call g:CssCompress(<count>, <f-args>)
command! -nargs=? -range=% Ckstyle :call g:Ckstyle(<count>, <f-args>)

