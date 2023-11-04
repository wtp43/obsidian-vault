---
dg-publish: true
---
- End of line: ctrl + e
- Clear screen: ctrl + l
- Backward delete char: ctrl + h
- Forward char: ctrl + f
- Expand or complete: ctrl + i
- Backward word: ctrl+ b


## Comparisons

### String Comparisons
Spaces are significant between operators and brackets

```zsh
if [ $VAR1 == $VAR2 ]; then
```
### Numeric Comparisons
Use the operator `-eq` instead of ==
### Unquoted variables

When a variable contains spaces or special characters, it is essential to quote the variable to prevent word splitting. For example:

```zsh
VAR1="Hello World"
if [ $VAR1 == "Hello World" ]; then
```


https://apple.stackexchange.com/questions/361870/what-are-the-practical-differences-between-bash-and-zsh
### Some nice zsh features

Here are a few nice zsh features that bash doesn't have (at least not without some serious elbow grease). Once again, this is just a selection of the ones I consider the most useful.

**[Glob qualifiers](http://zsh.sourceforge.net/Doc/Release/Expansion.html#Glob-Qualifiers)** allow matching files based on metadata such as their time stamp, their size, etc. They also allow tweaking the output. The syntax is rather cryptic, but it's extremely convenient. Here are a few examples:

- `foo*(.)`: only regular files matching `foo*` and symbolic links to regular files, not directories and other special files.
- `foo*(*.)`: only executable regular files matching `foo*`.
- `foo*(-.)`: only regular files matching `foo*`, not symbolic links and other special files.
- `foo*(-@)`: only dangling symbolic links matching `foo*`.
- `foo*(om)`: the files matching `foo*`, sorted by last modification date, most recent first. Note that if you pass this to `ls`, it'll do its own sorting. This is especially useful in…
- `foo*(om[1,10])`: the 10 most recent files matching `foo*`, most recent first.
- `foo*(Lm+1)`: files matching `foo*` whose size is at least 1MB.
- `foo*(N)`: same as `foo*`, but if this doesn't match any file, produce an empty list regardless of the setting of the `null_glob` option (see above).
- `*(D)`: match all files including dot files (except `.` and `..`).
- `foo/bar/*(:t)` (using a [history modifier](http://zsh.sourceforge.net/Doc/Release/Expansion.html#Modifiers)): the files in `foo/bar`, but with only the base name of the file. E.g. if there is a `foo/bar/qux.txt`, it's expanded as `qux.txt`.
- `foo/bar/*(.:r)`: take regular files under `foo/bar` and remove the extension. E.g. `foo/bar/qux.txt` is expanded as `foo/bar/qux`.
- `foo*.odt(e\''REPLY=$REPLY:r.pdf'\')`: take the list of files matching `foo*.odt`, and replace `.odt` by `.pdf` (regardless of whether the PDF file exists).

Here are a few useful zsh-specific **[wildcard patterns](http://zsh.sourceforge.net/Doc/Release/Expansion.html#Glob-Operators)**.

- `foo*.txt~foobar*`: all `.txt` files whose name starts with `foo` but not `foobar`.
- `image<->.jpg(n)`: all `.jpg` files whose base name is `image` followed by a number, e.g. `image3.jpg` and `image22.jpg` but not `image-backup.jpg`. The glob qualifier `(n)` causes the files to be listed in numerical order, i.e. `image9.jpg` comes before `image10.jpg` (you can make this the default even without `-n` with [`setopt numeric_glob_sort`](http://zsh.sourceforge.net/Doc/Release/Options.html#index-NUMERIC_005fGLOB_005fSORT)).

To **mass-rename files**, zsh provides a very convenient tool: the [`zmv` function](http://zsh.sourceforge.net/Doc/Release/User-Contributions.html#index-zmv). Suggested for your `.zshrc`:

```bash
autoload zmv
alias zcp='zmv -C' zln='zmv -L'
```

Example:

```dart
zmv '(*).jpeg' '$1.jpg'
zmv '(*)-backup.(*)' 'backups/$1.$2'
```



## zsh Functions
- `xargs`: The `xargs` command in UNIX is a command line utility for building an execution pipeline from standard input. Whilst tools like [`grep`](https://shapeshed.com/unix-grep/) can accept standard input as a parameter, many other tools cannot. Using `xargs` allows tools like `echo` and [`rm`](https://shapeshed.com/unix-rm/) and [`mkdir`](https://shapeshed.com/unix-mkdir/) to accept standard input as arguments.    


## Other

### ls vs echo $(ls)
https://unix.stackexchange.com/questions/283586/difference-between-ls-and-echo-ls
When you run this command:
`ls`
the terminal displays the output of ls.
When you run this command:
`echo $(ls)`
the shell captures the output of $(ls) and performs word splitting on it. With the default IFS, this means that all sequences of white space, including newline characters, are replaced by a single blank. That is why the output of echo $(ls) appears on one line.

**Command Substitution**
`$(...)` is command substitution ´