# apipt
`APIPT` is a package which installs Python packages by `apt` if possible, otherwise using `pip`.

[It's better to use `apt`](https://stackoverflow.com/questions/6874527).

## Example
Say there are a few packages we want to install:

Python packages that can be install by `apt`:
* numpy
* requests

Python packages that can't:
* fastai
* tensorflow

Normal packages:
* bind9
* curl

Let's run `apipt install numpy requests fastai tensorflow bind9 curl`:

```shell script
root@Ubuntu ~# apipt install numpy requests fastai tensorflow bind9 curl
Running: apt install python3-numpy python3-requests bind9 curl
Press any key if no [y/N] prompt.

...

After this operation, 27.0 MB of additional disk space will be used.
Do you want to continue? [Y/n] Y

...

Running: pip install fastai tensorflow
Press any key if no [y/N] prompt.


Collecting fastai
...
```

Like what is shown above, `apipt` automatically divide those package into two group. 

For one group, it calls `apt install python3-numpy python3-requests bind9 curl`, and for another, `pip install fastai tensorflow`.
