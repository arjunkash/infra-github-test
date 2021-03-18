# Signal edge detector

This repository is the basis of a test on how you work with tools such as git & github
as well as a hopefully interesting programming challenge.


## Task

1. Clone this repository to a private github repository
2. Solve the programming task in the language of your choice
3. Modify the `Dockerfile` such, that it runs your program when run with `docker run ...`

You can run `./docker-build.sh` to build the image locally and `./run-tests.sh` to test your program.

## Signal edge detector

* Read a line with up to 100 integer values from standard input
* For each value
    * Compare it to previous value
    * Write "1" if the value differs by more then 10 to the previous
    * If not, write "0"
    * The first output is always "0"
* The output values should be separated by a space
* Input values are integers between -100 and 100

If you played the programming game TIS-100, this one will be familiar.

### Example

The spaces are aligned for readability 
```
Input:
 0 32 30 27 24 28 37 33 24 13  9 13  9 13 12 14
Output:
 0  1  0  0  0  0  0  0  0  1  0  0  0  0  0  0
```
