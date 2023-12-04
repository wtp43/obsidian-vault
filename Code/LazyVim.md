---
dg-publish: true
---
# LazyVim
## Todo mappings
- 'jk' to esc
- ctrl - d with zz

## Basics

### File tree
- leader + e
- `<C-L>`, `<C-H>` switch between neo-tree and bufferline buffers
- `<C-l>`, `<C-h>` switch between neo-tree and bufferline

## Buffers
### Close buffer
- `<leader> + bd` to close current buffer
### Switch between buffers
- `<leader> + bb` or  ```<leader> ` ``` to switch to previous buffer

## Comment
`gco` - Insert comment to the next line and enters INSERT mode
`gcO` - Insert comment to the previous line and enters INSERT mode

`gcc` - Toggles the current line using linewise comment
`gbc` - Toggles the current line using blockwise comment

`gbaf` - Toggle comment around a function (w/ LSP/treesitter support)
`gbac` - Toggle comment around a class (w/ LSP/treesitter support)
## Terminal
- toggleterm config:
https://medium.com/@shaikzahid0713/terminal-support-in-neovim-c616923e0431

## Telescope

- `<leader><space>`Find Files (root dir)
- `<leader>,` Switch Buffer
- `<leader>/`|Grep (root dir)
- `<leader>:`Command History
|`<leader>fb`|Buffers|**n**|
|`<leader>fc`|Find Config File|**n**|
|`<leader>ff`|Find Files (root dir)|**n**|
|`<leader>fF`|Find Files (cwd)|**n**|
|`<leader>fr`|Recent|**n**|
|`<leader>fR`|Recent (cwd)|**n**|
|`<leader>gc`|commits|**n**|
|`<leader>gs`|status|**n**|
|`<leader>s"`|Registers|**n**|
|`<leader>sa`|Auto Commands|**n**|
|`<leader>sb`|Buffer|**n**|
|`<leader>sc`|Command History|**n**|
|`<leader>sC`|Commands|**n**|
|`<leader>sd`|Document diagnostics|**n**|
|`<leader>sD`|Workspace diagnostics|**n**|
|`<leader>sg`|Grep (root dir)|**n**|
|`<leader>sG`|Grep (cwd)|**n**|
|`<leader>sh`|Help Pages|**n**|
|`<leader>sH`|Search Highlight Groups|**n**|
|`<leader>sk`|Key Maps|**n**|
|`<leader>sm`|Jump to Mark|**n**|
|`<leader>sM`|Man Pages|**n**|
|`<leader>so`|Options|**n**|
|`<leader>sR`|Resume|**n**|
|`<leader>ss`|Goto Symbol|**n**|
|`<leader>sS`|Goto Symbol (Workspace)|**n**|
|`<leader>sw`|Word (root dir)|**n**|
|`<leader>sW`|Word (cwd)|**n**|
|`<leader>sw`|Selection (root dir)|**v**|
|`<leader>sW`|Selection (cwd)|**v**|
|`<leader>uC`|Colorscheme with preview|**n**|

##

### Split Window
- open split window
- switch between split window

### Fuzzy search (telescope)

### Notifications
- `<leader>un` :	Dismiss all Notifications	

leader + 
- e: Explorer NeoTree(root dir)
- E: Explorer Neo 
- /: Grep (root dir)
- |: Split window right
- f: find
- shift + v: v-line
	- gc: uncomment
- 
### cmdline
- shift + :
	- w
	- qa: quit all

## Buffers and not tabs
A buffer is the in-memory text of a file.
A window is a viewport on a buffer.
A tab page is a collection of windows.

- `:bd` or `leader + bd` closes buffer
- ctrl-i/o to navigate jumplist
### Harpoon

### Telescope
## Other Plugins
### lsp

### Telescope


### Leap.nvim



# Mason
- leader + cm
- Manage linters, language support
# Related
