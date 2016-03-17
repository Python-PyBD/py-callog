# py-callog

Pass a file that has call logs in hh:mm:ss format.

```
$ cat call.log
00:52:34
00:50:21
00:00:26
00:05:39
...
```

Run `call.py` to calculate total sum in human readable hh:mm:ss format.

```
$ cat call.log | python callsum.py 
99h 9m 4s
```
