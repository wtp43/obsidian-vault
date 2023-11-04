---
dg-publish: true
---
---

>[!summary]+ Contents
>```toc
style: number
min_depth:1
max_depth:6 
>```

# Command line Utilities

## jq
JSON parser

### Usage

`.` 	unchanged input 	
`.foo, .foo.bar, .foo?` 	value at key
`.[], .[]?, .[2], .[10:15]` 	array operation 	
`[], {}` 	array/object construction
`select(foo)` 	input unchanged if foo returns true 	
`map(foo)` 	invoke filter foo for each input 	
`if-then-else-end` 	conditionals 	
`\(foo)` 	string interpolation
`|` pipe
`length` 	length of a value 	
`keys`  	keys in an array

### Example
```zsh

# Grab the first commit
curl 'https://api.github.com/repos/jqlang/jq/commits?per_page=5' | jq '.[0]'

[
  {
    "sha": "cff5336ec71b6fee396a95bb0e4bea365e0cd1e8",
    "node_id": "C_kwDOAE3WVdoAKGNmZjUzMzZlYzcxYjZmZWUzOTZhOTViYjBlNGJlYTM2NWUwY2QxZTg",
    "commit": {
      "author": {
        "name": "Mattias Wadman",
        "email": "mattias.wadman@gmail.com",
        "date": "2021-06-09T14:02:22Z"
      },
      "committer": {
        "name": "Nico Williams",
        "email": "nico@cryptonector.com",
        "date": "2022-05-26T21:04:32Z"
      },
      "message": "docs: Document repeat(exp)",
      "tree": {
        "sha": "d67d5542df1f16d1a48e1fb75749f60482cd874b",
        "url": "https://api.github.com/repos/jqlang/jq/git/trees/d67d5542df1f16d1a48e1fb75749f60482cd874b"
      },
      "url": "https://api.github.com/repos/jqlang/jq/git/commits/cff5336ec71b6fee396a95bb0e4bea365e0cd1e8",
      "comment_count": 0,
      "verification": {
        "verified": false
      }
    },
    "comments_url": "https://api.github.com/repos/jqlang/jq/commits/cff5336ec71b6fee396a95bb0e4bea365e0cd1e8/comments",
    "author": {

# Get specific fields and return it as an object

jq '.[0] | {message: .commit.message, name: .commit.committer.name}'

{
  "message": "docs: Document repeat(exp)",
  "name": "Nico Williams"
}

# Return all collected objects into 1 array. Wrap command with []
jq '[.[] | {message: .commit.message, name: .commit.committer.name}]'

# Get Parent
jq '[.[] | {message: .commit.message, parents: [.parents[].html_url]}]'
```
## curl
Transfer data to/from server

> [!example]+ Ex: curl google.com
> Displays the content of the url 

- `-O`: downloads file with name as url
- `-C`: resume download that was stopped for some reason
- numeric sequence in url: curl http://site.com/file[1-20].jpeg
- substitutions: curl http://site.{x,y,z}.com

## xargs
For building an execution pipeline from standard input. Useful for tools like `echo`, `rm`, mkdir

- `-I`: run multiple commands

> [!example]+ Multiple Commands
> `cat foo.txt`
> one
> two
> three
> 
> `cat foo.txt | xargs -I % sh -c 'echo %; mkdir %'`
> one
> two
> three
> 
> `ls`
> one two three



### Common Usage
- In conjunction with `find`:
- 
> [!example]+ find /tmp -mtime +14 | xargs rm
> 1. Find all files in /tmp that is older than 2 weeks
> 2. Result piped to `xargs` which runs `rm` on each file

## svn (Subversion)

Centralized version control system
### Common Usage
- Clone only a subdirectory: Append `/trunk/subdirectory_name` to repository along 
	- Verify content with `svn ls https://github.com/foobar/Test.git/trunk/foo`
	- Export: `svn export`

## chmod (Change mode)
Change file permissions
### Common Usage
- Add execute permission
	- `chmod +x foo`

# Related
