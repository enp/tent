#!/bin/bash -xe

for dockerfile in $(ls dockerfiles)
do
    docker image build . -f dockerfiles/$dockerfile -t tent:$dockerfile
done
