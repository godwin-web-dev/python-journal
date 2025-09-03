## Command History

```bash
$ history
```

Sample output:
```
  1  git config user.name
  2  pwd
  3  ls
  4  ls -l
  5  mkdir demo
  ...
 91  history
```

### Show Last 10 Commands

```bash
$ history | tail
```
Returns the last 10 records from the available history.

### Show First 10 Commands

```bash
$ history | head
```
Returns the first 10 records from the available history.

### Custom Number of Lines

```bash
$ history | tail -n 1
```
Returns only the last item in the history.  
You can use `-n <number>` with `head` or `tail` to specify how many lines to show.

---

## Creating and Editing Files

### Create a New File

```bash
$ touch demo.txt
```

### Edit the File

```bash
$ vi demo.txt
```
Example content:
```
1. dog
2. cat
3. lion
4. tiger
5. elephant
6. giraffe
7. zebra
8. monkey
9. horse
10. cow
```

### Save and Quit in `vi`

- Save: `:w`
- Quit: `:q`
- Save and quit: `:wq`
- Force quit: `:q!`

---