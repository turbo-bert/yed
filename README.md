# Installation

    echo "#!$(which python3.11)" >~/bin/yed
    curl -L 'https://raw.githubusercontent.com/turbo-bert/yed/main/src/yed/__main__.py' >>~/bin/yed
    #cat src/yed/__main__.py >>~/bin/yed
    chmod a+x ~/bin/yed
