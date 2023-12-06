---
dg-publish: true
---
# Vim 
## Navigation
Directions
- hl
- j down
- k up
- `gg` to move to top
- G to move to bottom
- `{`, `}` to jump paragraphs

### Horizontal
- fx/Fx
- tx/Tx

### Vertical
- 5jj

### Jump
- `<leader> gd`: Jump to definition in the file (or function?)


## Text Editing
- `ci` change inside
	- `ci"` 
- `daw`
- `diw`

const res = await fetch(, `)
- `^` jump to first non-blank character
- `$` to the end of the line, including the last character
- `0` to move to the start of the line

## find
- `fx` jump to before next occurrence of x
- `fx` jump to previous occurrence of x
- `;` repeat previous f,t movement
- `,` repeat previous f,t movement backwards

## indentation
- `>` indent 
- `<` indent 
# undo/redo
- `u` undos the last command
- `u` restores the line to its original state
- `ctrl-r` redos the last command

# put
- `p` puts previously deleted text after the cursor
- `rx` to replace the character at the cursor with x

# change 
the change operator is used with the same motions as delete
- `ce` to change until the end of a word
- `cc` does the same for the whole line
- `c3w` deletes the next 3 words

# cursor location and file status
- `CTRL-g` to show current line and and file status
- `G` to move to bottom of file
- `gg` to move to start of file
- `492G` to move to line 492

# Search
- `/` followed by a phrase 
- `n` to move forward, `N` to move backwards
- `?` to search backwards
- `CTRL-o` to go back to where you came from
- `CTRL-i` to go forward

# Substitute
- `:s/old/new/g` to substitute 'new' for old', g flag to replace globally in the line
- `%s/old/new/g` to substitute for the whole file
	-`/gc` to prompt whether to substitute or not
- `:#,#s/old/new/g` to substitute between line numbers

# Execute External Command
- `:!` followed by an external command

# Write
- `:w FILENAME`

# Visual Mode
- In visual mode, the cursor can be moved around to make the selection bigger or smaller.
- An operator can be applied to the text after

