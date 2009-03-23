#!/bin/bash
sort < fastmail.txt > f.txt
sort < gmail.txt > g.txt
vimdiff f.txt g.txt
