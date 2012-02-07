#!/bin/bash

szAnswer=$(zenity --entry --text "Enter de Commit message:" --entry-text "");

if [ $? -eq 0 ]; then
	git add --all
	git commit -am"$szAnswer"
	git push origin master	
	exit 0
fi	
	exit 1


