#!/bin/bash
# This script is used to update the monaco editor version

VERSION=0.44.0

echo "__version__ = '$VERSION'" > rocher/version.py
wget https://registry.npmjs.org/monaco-editor/-/monaco-editor-$VERSION.tgz


tar -xvf monaco-editor-$VERSION.tgz
rm -rf monaco-editor-$VERSION.tgz

rm -Rf rocher/monaco

mv package/min/vs rocher/vs
cp package/LICENSE rocher/vs/LICENSE
cp package/ThirdPartyNotices.txt rocher/vs/ThirdPartyNotices.txt

rm -Rf package