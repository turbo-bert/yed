#!/bin/bash


source ~/src/github/yed/python/bin/activate

python ../src/yed/__main__.py -i --unset volumes,bla test.yml

#python ../src/yed/__main__.py -i --addnull volumes,bla8 test.yml
