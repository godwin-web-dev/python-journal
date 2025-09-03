# awk command is used to find, manipulate the output, return a specific column
 
>ls -l | awk ' {print $0}
AzureAD+GodwinV@OnStak MINGW64 ~
$ ls -l | awk '{print $0}' 
note: print $0 returns all the columns by default
total 21159
drwxr-xr-x 1 AzureAD+GodwinV 4096        0 Feb 24 15:38 AppData/
lrwxrwxrwx 1 AzureAD+GodwinV 4096       32 Feb 24 15:37 Application Data -> /c/Users/GodwinV/AppData/Roaming/
drwxr-xr-x 1 AzureAD+GodwinV 4096        0 Feb 24 15:44 Contacts/
lrwxrwxrwx 1 AzureAD+GodwinV 4096       60 Feb 24 15:37 Cookies -> /c/Users/GodwinV/AppData/Local/Microsoft/Windows/INetCookies/
drwxr-xr-x 1 AzureAD+GodwinV 4096        0 Aug 13 11:20 Desktop/
drwxr-xr-x 1 AzureAD+GodwinV 4096        0 Aug  5 10:08 Documents/
drwxr-xr-x 1 AzureAD+GodwinV 4096        0 Aug 11 10:55 Downloads/
drwxr-xr-x 1 AzureAD+GodwinV 4096        0 Feb 24 15:44 Favorites/
drwxr-xr-x 1 AzureAD+GodwinV 4096        0 Feb 24 15:44 Links/
lrwxrwxrwx 1 AzureAD+GodwinV 4096       30 Feb 24 15:37 Local Settings -> /c/Users/GodwinV/AppData/Local/
drwxr-xr-x 1 AzureAD+GodwinV 4096        0 Feb 24 15:44 Music/
lrwxrwxrwx 1 AzureAD+GodwinV 4096       26 Feb 24 15:37 My Documents -> /c/Users/GodwinV/Documents/
-rw-r--r-- 1 AzureAD+GodwinV 4096 13631488 Aug  1 01:20 NTUSER.DAT
-rw-r--r-- 1 AzureAD+GodwinV 4096    65536 Feb 24 15:37 NTUSER.DAT{e2c9ef2b-f296-11ef-bbab-c08579be7b0d}.TM.blf
-rw-r--r-- 1 AzureAD+GodwinV 4096   524288 Feb 24 15:37 NTUSER.DAT{e2c9ef2b-f296-11ef-bbab-c08579be7b0d}.TMContainer00000000000000000001.regtrans-ms
-rw-r--r-- 1 AzureAD+GodwinV 4096   524288 Feb 24 15:37 NTUSER.DAT{e2c9ef2b-f296-11ef-bbab-c08579be7b0d}.TMContainer00000000000000000002.regtrans-ms
lrwxrwxrwx 1 AzureAD+GodwinV 4096       68 Feb 24 15:37 NetHood -> /c/Users/GodwinV/AppData/Roaming/Microsoft/Windows/Network Shortcuts/
drwxr-xr-x 1 AzureAD+GodwinV 4096        0 Oct  8  2024 OneDrive/
drwxr-xr-x 1 AzureAD+GodwinV 4096        0 Feb 24 15:44 Pictures/
drwxr-xr-x 1 AzureAD+GodwinV 4096        0 Nov 26  2024 Postman/
lrwxrwxrwx 1 AzureAD+GodwinV 4096       68 Feb 24 15:37 PrintHood -> /c/Users/GodwinV/AppData/Roaming/Microsoft/Windows/Printer Shortcuts/
lrwxrwxrwx 1 AzureAD+GodwinV 4096       57 Feb 24 15:37 Recent -> /c/Users/GodwinV/AppData/Roaming/Microsoft/Windows/Recent/
drwxr-xr-x 1 AzureAD+GodwinV 4096        0 Feb 24 15:44 Saved Games/
drwxr-xr-x 1 AzureAD+GodwinV 4096        0 Feb 24 15:44 Searches/
lrwxrwxrwx 1 AzureAD+GodwinV 4096       57 Feb 24 15:37 SendTo -> /c/Users/GodwinV/AppData/Roaming/Microsoft/Windows/SendTo/
lrwxrwxrwx 1 AzureAD+GodwinV 4096       61 Feb 24 15:37 Start Menu -> /c/Users/GodwinV/AppData/Roaming/Microsoft/Windows/Start Menu/
lrwxrwxrwx 1 AzureAD+GodwinV 4096       60 Feb 24 15:37 Templates -> /c/Users/GodwinV/AppData/Roaming/Microsoft/Windows/Templates/
drwxr-xr-x 1 AzureAD+GodwinV 4096        0 Aug  4 10:21 Videos/
drwxr-xr-x 1 AzureAD+GodwinV 4096        0 Oct 26  2024 bin/
drwxr-xr-x 1 AzureAD+GodwinV 4096        0 Aug 12 16:24 demo/
drwxr-xr-x 1 AzureAD+GodwinV 4096        0 Jul 31 23:29 godwin-portfolio/
-rw-r--r-- 1 AzureAD+GodwinV 4096        0 Aug 12 16:02 helloworld.txt
-rw-r--r-- 1 AzureAD+GodwinV 4096      255 Aug  2 17:17 index.html
-rw-r--r-- 1 AzureAD+GodwinV 4096        0 Aug 13 13:25 ls
-rw-r--r-- 1 AzureAD+GodwinV 4096       52 Aug 13 13:20 new_txt_file_using_echo.txt
-rw-r--r-- 1 AzureAD+GodwinV 4096  3420160 Feb 24 15:37 ntuser.dat.LOG1
-rw-r--r-- 1 AzureAD+GodwinV 4096  3358720 Feb 24 15:37 ntuser.dat.LOG2
-rw-r--r-- 1 AzureAD+GodwinV 4096       20 Feb 24 15:44 ntuser.ini
drwxr-xr-x 1 AzureAD+GodwinV 4096        0 Aug 13 11:45 practising-grep-commands/

==========================================================================================
> ls -l | awk '{print $1}
AzureAD+GodwinV@OnStak MINGW64 ~
$ ls -l | awk '{print $1}'
total
drwxr-xr-x
lrwxrwxrwx
drwxr-xr-x
lrwxrwxrwx
drwxr-xr-x
drwxr-xr-x
drwxr-xr-x
drwxr-xr-x
drwxr-xr-x
lrwxrwxrwx
drwxr-xr-x
lrwxrwxrwx
-rw-r--r--
-rw-r--r--
-rw-r--r--
-rw-r--r--
lrwxrwxrwx
drwxr-xr-x
drwxr-xr-x
drwxr-xr-x
lrwxrwxrwx
lrwxrwxrwx
drwxr-xr-x
drwxr-xr-x
lrwxrwxrwx
lrwxrwxrwx
lrwxrwxrwx
drwxr-xr-x
drwxr-xr-x
drwxr-xr-x
drwxr-xr-x
-rw-r--r--
-rw-r--r--
-rw-r--r--
-rw-r--r--
-rw-r--r--
-rw-r--r--
-rw-r--r--
drwxr-xr-x

=================================================================================================================

## note do not use the range in the awk u can access the columns seperate seperately like this 
ls -l | awk '{print $1 $2 $3}
AzureAD+GodwinV@OnStak MINGW64 ~
$ ls -l | awk '{print $1 $2 }'
total21159
drwxr-xr-x1
lrwxrwxrwx1
drwxr-xr-x1
lrwxrwxrwx1
drwxr-xr-x1
drwxr-xr-x1
drwxr-xr-x1
drwxr-xr-x1
drwxr-xr-x1
lrwxrwxrwx1
drwxr-xr-x1
lrwxrwxrwx1
-rw-r--r--1
-rw-r--r--1
-rw-r--r--1
-rw-r--r--1
lrwxrwxrwx1
drwxr-xr-x1
drwxr-xr-x1
drwxr-xr-x1
lrwxrwxrwx1
lrwxrwxrwx1
drwxr-xr-x1
drwxr-xr-x1
lrwxrwxrwx1
lrwxrwxrwx1
lrwxrwxrwx1
drwxr-xr-x1
drwxr-xr-x1
drwxr-xr-x1
drwxr-xr-x1
-rw-r--r--1
-rw-r--r--1
-rw-r--r--1
-rw-r--r--1
-rw-r--r--1
-rw-r--r--1
-rw-r--r--1
drwxr-xr-x1

AzureAD+GodwinV@OnStak MINGW64 ~
$ ls -l | awk '{print $1$5$8}'
total
drwxr-xr-x015:38
lrwxrwxrwx3215:37
drwxr-xr-x015:44
lrwxrwxrwx6015:37
drwxr-xr-x011:20
drwxr-xr-x010:08
drwxr-xr-x010:55
drwxr-xr-x015:44
drwxr-xr-x015:44
lrwxrwxrwx3015:37
drwxr-xr-x015:44
lrwxrwxrwx2615:37
-rw-r--r--1363148801:20
-rw-r--r--6553615:37
-rw-r--r--52428815:37
-rw-r--r--52428815:37
lrwxrwxrwx6815:37
drwxr-xr-x02024
drwxr-xr-x015:44
drwxr-xr-x02024
lrwxrwxrwx6815:37
lrwxrwxrwx5715:37
drwxr-xr-x015:44
drwxr-xr-x015:44
lrwxrwxrwx5715:37
lrwxrwxrwx6115:37
lrwxrwxrwx6015:37
drwxr-xr-x010:21
drwxr-xr-x02024
drwxr-xr-x016:24
drwxr-xr-x023:29
-rw-r--r--016:02
-rw-r--r--25517:17
-rw-r--r--013:25
-rw-r--r--5213:20
-rw-r--r--342016015:37
-rw-r--r--335872015:37
-rw-r--r--2015:44
drwxr-xr-x011:45

AzureAD+GodwinV@OnStak MINGW64 ~
$

# to create a file using echo 

>echo "hello world "> new_txt_file.txt

to find a specific text in the file that u have created use the '/' symbol

> awk '/hello/{print}' new_txt_file.txt
output 
hello world

AzureAD+GodwinV@OnStak MINGW64 ~
$ vi number.txt

AzureAD+GodwinV@OnStak MINGW64 ~
$ cat number.txt

one
two
three
four
five
six
seven
eight
nine
ten

$ awk '/three/{print}' number.txt
three

#to find and manipulate values
>awk '{%1="Godwin"; print$0}' number.txt
AzureAD+GodwinV@OnStak MINGW64 ~
$ awk '{$1="Godwin" ; print $0}' number.txt
Godwin
Godwin
Godwin
Godwin
Godwin
Godwin
Godwin
Godwin
Godwin
Godwin
Godwin

