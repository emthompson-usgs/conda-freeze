This is a small utility meant to create a custom channel of the current
conda virtual environment that can then be used to "freeze" all of the
packages in that environment. This was motivated by a history of using
conda to manage dependencies and having them "go bad" even when we pin
to exact version numbers.

Install
=======

1) Clone this repository.

2) Change into the the conda virtual environment that you want to freeze.
```
conda activate <name>
```

3) Install this repository. 
```
pip install -e <path to the clone of this repository>
```

4)  Install conda-build.
```
conda install conda-build
```

Run
===

Run the script and provide an output directory for the results
```
freeze <output directory>
```

This will output a channel in the specified output direcotry that can be
used to install with a command like:
```
conda create -y --override-channels -n test \
      -c file://<absolute path to channel directory> \
      <list of packages>
```
It also automatically makes a tar file of the channel which can be used for
transferring the channel to another machine.
