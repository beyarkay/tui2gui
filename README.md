# Tui2Gui

### Convert your favorite TUI/CLI app into a web GUI

Often I've got a favorite CLI that I want to use, and want to use on my phone
while I'm out and about. However the open source community isn't great at
providing GUIs, so this will automate the heavy lifting for you and create
beautiful GUIs that interact with the shell in a secure way.

## Screenshots

(This is still a work in progress)

![imgs/proof_of_concept.png](imgs/proof_of_concept.png)

## Features

- Beautiful and simple
- Can easily define buttons which execute a pre-specified command
- General access to the shell is not available
  the frontend must first be defined on the backend
- The stderr and stdout are piped back through to the frontend
    - future work will format this if it seems helpful

## Get started

This is still a work in progress

## Scope

This project is not aiming to let you type shell commands in your browser, I'm
sure something already exists for that.

Instead it covers the case where you want a GUI, but you want the back end to
be covered by a TUI that you host (on a raspberry pi or something).

This in turn means that tui2gui does not aim to be good at displaying
everything a terminal can display as soon as the terminal displays it. The idea
is you want to run a single (TUI-based) command on your phone, and possibly
want to get confirmation that it ran okay, but nothing more.

## Contributing

This is still a work in progress



