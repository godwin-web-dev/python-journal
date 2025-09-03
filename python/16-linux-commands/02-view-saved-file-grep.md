##  Linux Command Notes Command  = HistoryViewing Files

```bash
$ cat demo.txt
```
Output:
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

---

## Searching with `grep`

### Find a Specific Pattern

```bash
$ cat demo.txt | grep "cat"
```
Output:
```
2. cat
```

### Search for Multiple Patterns (Extended Regex)

```bash
$ cat demo.txt | grep -E 'dog|cat'
```
Output:
```
1. dog
2. cat
```

### Invert Match (Exclude Pattern)

```bash
$ cat demo.txt | grep -v "dog"
```
Output:
```
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
This returns all lines except those containing "dog".

You can also use extended regex with `-v` to exclude multiple patterns. For example, to exclude both "dog" and "cat":
```bash
$ cat demo.txt | grep -vE 'dog|cat'
```