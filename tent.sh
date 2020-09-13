#!/bin/bash -xe

gradle -b /opt/tent/tent.gradle $@ 2>&1 | tee build.log
