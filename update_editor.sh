#!/bin/bash
# This script is used to update the monaco editor version

MONACO_VERSION=0.52
MONACO_VERSION_PATCH=2
ROCHER_PATCH_VERSION=$MONACO_VERSION_PATCH

echo "__version__ = '$MONACO_VERSION.$ROCHER_PATCH_VERSION'" > rocher/version.py
wget https://registry.npmjs.org/monaco-editor/-/monaco-editor-$MONACO_VERSION.$MONACO_VERSION_PATCH.tgz


tar -xvf monaco-editor-$MONACO_VERSION.$MONACO_VERSION_PATCH.tgz
rm -rf monaco-editor-$MONACO_VERSION.$MONACO_VERSION_PATCH.tgz

rm -Rf rocher/vs

mv package/min/vs rocher/vs
cp package/LICENSE rocher/vs/LICENSE
cp package/ThirdPartyNotices.txt rocher/vs/ThirdPartyNotices.txt

rm -Rf package

if [ $(git tag -l "v$MONACO_VERSION.$ROCHER_PATCH_VERSION") ]; then
    echo "Tag $MONACO_VERSION.$ROCHER_PATCH_VERSION already exists"
else
    git add .
    git commit -m "Monaco editor version $MONACO_VERSION"
    git tag -a "v$MONACO_VERSION.$ROCHER_PATCH_VERSION" -m "Monaco editor version $MONACO_VERSION"
fi
