#!/bin/bash -xe

deliver=$1
repo=$2
branch=$3

mkdir -p builds
git clone -b $branch --single-branch https://github.com/$repo builds/$deliver
cd builds/$deliver
docker run --rm -it -v $(pwd):/product tent:centos7 tent.sh rpm
