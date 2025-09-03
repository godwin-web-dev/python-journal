# Combine Two Files (or More) in Linux

You can combine the contents of multiple files into a single file using the `cat` command.

---

## Create Sample Files

```bash
vi file_01.txt
vi file_02.txt
vi file_03.txt
vi file_04.txt
```

## Combine Files

```bash
cat file_01 file_02 file_03 file_04
```

This will display the contents of all four files in the terminal.

## Redirect Output to a New File

To combine the files and save the output to a new file, use the `>` operator:

```bash
cat file_01 file_02 file_03 file_04 > combined_file_1
```

You can then view the contents of the new file with:

```bash
cat combined_file_1
```


