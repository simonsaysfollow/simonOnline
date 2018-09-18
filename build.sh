#!/bin/bash

#main content
cat templates/top.html content/index.html  templates/bottom.html > docs/index.html

#relevant content
cat templates/top.html content/relevantIndex.html  templates/bottom.html > docs/relevantIndex.html

#blog
cat templates/top.html content/blogIndex.html  templates/bottom.html > docs/blogIndex.html
