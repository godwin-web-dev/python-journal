# CUT Command in Linux

The `cut` command is used to extract specific sections from each line of a file.  
You can perform cut operations on characters or on fields separated by delimiters such as spaces or commas.

---

## Cut Operation on Characters

Create a file and add content:
```bash
$ touch godwin.txt
$ vi godwin.txt
```
Sample content:
```
Godwin
```

Extract specific characters:
```bash
$ cut -c 1 godwin.txt
G

$ cut -c 1-3 godwin.txt
God

$ cut -c 1- godwin.txt
Godwin

$ cut -c 3- godwin.txt
dwin
```

---

## Cut Operation Using Delimiters

### With Space as Delimiter

List files with details and extract specific fields:
```bash
$ ls -l
total 12
-rw-r--r-- 1 AzureAD+GodwinV 4096   46 Aug 12 21:55 data.txt
-rw-r--r-- 1 AzureAD+GodwinV 4096    8 Aug 12 23:31 data2.txt
-rw-r--r-- 1 AzureAD+GodwinV 4096   90 Aug 12 22:39 demo.txt
-rw-r--r-- 1 AzureAD+GodwinV 4096   44 Aug 13 00:18 dummy.txt
-rw-r--r-- 1 AzureAD+GodwinV 4096    7 Aug 13 00:29 godwin.txt
-rw-r--r-- 1 AzureAD+GodwinV 4096  661 Aug 12 22:38 index.txt
-rw-r--r-- 1 AzureAD+GodwinV 4096 1060 Aug 12 22:32 index2.txt
-rw-r--r-- 1 AzureAD+GodwinV 4096  446 Aug 12 23:39 lorem
-rw-r--r-- 1 AzureAD+GodwinV 4096  326 Aug 12 23:46 quote.txt

$ ls -l | cut -d ' ' -f 1
total
-rw-r--r--
-rw-r--r--
-rw-r--r--
-rw-r--r--
-rw-r--r--
-rw-r--r--
-rw-r--r--
-rw-r--r--
-rw-r--r--

$ ls -l | cut -d ' ' -f 1-3
total 12
-rw-r--r-- 1 AzureAD+GodwinV
-rw-r--r-- 1 AzureAD+GodwinV
-rw-r--r-- 1 AzureAD+GodwinV
-rw-r--r-- 1 AzureAD+GodwinV
-rw-r--r-- 1 AzureAD+GodwinV
-rw-r--r-- 1 AzureAD+GodwinV
-rw-r--r-- 1 AzureAD+GodwinV
-rw-r--r-- 1 AzureAD+GodwinV
-rw-r--r-- 1 AzureAD+GodwinV
```

### With Comma-Separated Values

Create a file with comma-separated values and extract specific fields:
```bash
$ touch fruits.txt
$ vi fruits.txt
```
Sample content:
```
apple,mango,orange,pineapple are the fruits
```

Extract specific fruits:
```bash
$ cut -d ',' -f 1 fruits.txt
apple

$ cut -d ',' -f 1-3 fruits.txt
apple,mango,orange
```

Extract words based on space delimiter:
```bash
$ cut -d ' ' -f 1 fruits.txt
apple,mango,orange,pineapple

$ cut -d ' ' -f 2 fruits.txt
are

$ cut -d ' ' -f 3 fruits.txt
the 

$ cut -d ' ' -f 4 fruits.txt
fruits
```

# CUT Command Using the Complement Option

The `--complement` option with the `cut` command allows you to exclude the fields you specify, instead of including them.

For example, if you want to exclude the first field from a CSV file:

```bash
$ cat example.csv
name,age,city
Alice,30,New York
Bob,25,Los Angeles
Charlie,35,Chicago

$ cut -d ',' -f 1 --complement example.csv
age,city
30,New York
25,Los Angeles
35,Chicago
```

To exclude the first two fields:

```bash
$ cut -d ',' -f1-2 --complement example.csv
city
New York
Los Angeles
Chicago
```

## CUT Command with the Output Delimiter

You can also change the output delimiter using the `--output-delimiter` option. For example, to change the delimiter to `__+__`:

```bash
$ cut -d "," -f1- --output-delimiter="__+__" example.csv
name__+__age__+__city
Alice__+__30__+__New York
Bob__+__25__+__Los Angeles
Charlie__+__35__+__Chicago
```


