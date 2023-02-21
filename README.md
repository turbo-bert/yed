# What is this...

A very small hack to automate editing YAML files. By the time I didn't find an easy way to change stuff in YAML files from the linux shell. So in most of my environments there's python. Here we go.

# Installation

    echo "#\!$(which python3.11)" | tr -d '\\' >~/bin/yed
    curl -L 'https://raw.githubusercontent.com/turbo-bert/yed/main/src/yed/__main__.py' >>~/bin/yed
    #cat src/yed/__main__.py >>~/bin/yed
    chmod a+x ~/bin/yed
