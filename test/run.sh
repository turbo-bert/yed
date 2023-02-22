#!/bin/bash


source ~/src/github/yed/python/bin/activate

rm -fr run
mkdir run

for saml in $(ls *.saml); do
    cp -v $saml run/${saml%%.saml}.yaml
done

pushd .
cd run
python ../../src/yed/__main__.py -i --insert-yaml-file volumes test2.yaml test.yaml

popd

#python ../src/yed/__main__.py -i --unset volumes,bla test.yml
