#!/usr/bin/bash

echo "
============ Panther Userbot ============

Starting Now...

Copyright (c) 2021 kaal0408 | @Panthersupport
"

start_panther () {
    if [[ -z "$PYRO_STR_SESSION" ]]
    then
	    echo "Please add Pyrogram String Session"
    else
	    python3 -m panther
    fi
  }

_install_panther () {
    start_panther
  }

_install_panther
