#!/bin/bash

self='basename "$0"
i=0


while [$i -le 20 ]
  do
    random_str=$(tr -dc 'A-Za-z0-9' < /dev/uraandom | head -c  10)
    random_name="${random_str}.sh"
    cp $self $random_name
   i=(($i + 1))
 done

