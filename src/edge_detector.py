import sys
import string
import math

def main():
    series = []                                                                                 #Initialize
    temp = []

    for line in sys.stdin:                                                                      #Accept input even if its multi-lines
        temp = line.split(" ")
        series = series + temp

    if len(series) > 100:                                                                       #Only upto 100 integer values allowed
        sys.exit("Only upto 100 integer values allowed")                                        #Say "No" to exit(0); sys.exit() is far better

    if series[len(series)-1] == "\n":                                                            #Check if there are any unneccessary newline character
        series.remove(series[len(series)-1])

    try:
        int_series = list(map(int, series))                                                     #I used map, yay!!
    except ValueError:
        print("Error: Invalid Input")                                                           #Catch if there are invalid inputs like chartacters or other characters (intergers only)
        raise

    for i in int_series:
        if abs(i) > 100:                                                                        #Only integers between -100 and 100 are allowed
            sys.exit("Only integers between -100 and 100 are allowed")

    out_list = [0] * len(int_series)                                                            #Initialize and allocate only what is neccesary

    for i in range(1, len(int_series)):
        if (max(int_series[i-1] - int_series[i], int_series[i] - int_series[i-1])) > 10:        #Distance between numbers
            out_list[i] = 1
    
    #str_out = str(out_list).replace(",", "")                                                   Original plan was to replace, Im gonna leave this here
    str_out = ' '.join(filter(str.isalnum, str(out_list)))                                      #Found out this works better
    print(str_out)
    


main()