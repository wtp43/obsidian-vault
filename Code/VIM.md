---
dg-publish: true
---
# Navigation
Directions
- hl
- j down
- k up
- `gg` to move to top

# Exiting VIM
Discard all changes
- ``:q!``
- ``:wq`

# Text Editing
- `x` deletes character under cursor
- `i` to insert text
- `A` to append. Cursor automatically moves to end of line.
- `shift + enter` to insert new line without leaving normal mode

# Deletion Commands
- `dw` delete word
- `d$` delete to end of line
- `dd` deletes the current line
	- `2dd` deletes two lines

# Motions
- `w` until start of next word, excluding its first character
	- `2w` moves the cursor two word forward
- `e` to the end of the current word, including the last character
- `E` to end of current word including punctuation
- `b` to start of previous word
- `B` to start of previous word including punctuation
- `%` move to matching character (`),],}`)
- `^` jump to first non-blank character
- `$` to the end of the line, including the last character
- `0` to move to the start of the line

# Find
- `fx` jump to before next occurrence of x
- `Fx` jump to previous occurrence of x
- `;` repeat previous f,t movement
- `,` repeat previous f,t movement backwards

# Undo/Redo
- `u` undos the last command
- `U` restores the line to its original state
- `CTRL-R` redos the last command

# Put
- `p` puts previously deleted text after the cursor
- `rx` to replace the character at the cursor with x

# Change 
The change operator is used with the same motions as delete
- `ce` to change until the end of a word
- `cc` does the same for the whole line
- `c3w` deletes the next 3 words

# Cursor Location and File Status
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

