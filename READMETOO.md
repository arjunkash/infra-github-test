Docker size: Official base image python:3 ~  900 MB

Used Alpine version: 107 MB

Dependency in Mac while running tests: 'shuf'
To install shuf: brew install coreutils


main file: src/
mytests: Check Invalid inputs and edgecases for the program

Run:

- cat mytests/valid_multilineinput.txt | docker run -i edge-detector

- echo "1 3 66 23 45 1 34" | docker run -i edge-detector


