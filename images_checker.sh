#! /bin/bash
for file in `find /images -type f -name "image_*"`				#way to directory with photos!!!!
	do
		python3 faces_recognition.py $file										#way to program !!!!!!!!
	done
