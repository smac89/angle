#!/usr/bin/env bash
echo INSTALLING DEPENDENCIES... This might take a minute or 10

#git submodule foreach init
git submodule foreach git pull origin master

export ANGLE_HOME=$PWD
echo export ANGLE_HOME=$PWD
echo "export ANGLE_HOME=$PWD" >> ~/.bashrc

sudo ln -s $ENGLISH_SCRIPT_HOME/bin/angle /usr/bin/angle

echo "Adding TextMate support, like syntax highlighting"
git clone git@github.com:pannous/EnglishScript.tmbundle.git ~/Library/Application\ Support/TextMate/Bundles/EnglishScript.tmbundle/ 2>/dev/null