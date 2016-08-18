#!/bin/bash

cat header.html > index.html

for i in $( ls -d */ ); do
    echo "              <li><a href=\""$i"\">@"${i%%/}"</a></li>" >> index.html
done

cat footer.html >> index.html
