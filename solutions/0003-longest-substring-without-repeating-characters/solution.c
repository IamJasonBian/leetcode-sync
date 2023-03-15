#include <stdio.h>
#include <string.h>

int lengthOfLongestSubstring(char *s) {


int n = strlen(s);
    int start = 0, end = 0;
    int maxLen = 0;
     int set[128] = {0};  // initialize set with 0

    while (end < n) {
        if (set[s[end]] == 0) {

            set[s[end]] = 1;
              end++;
            maxLen =    (end - start > maxLen) ? (end - start) : maxLen;
        } else {

            set[s[start]] = 0;
            start++;
        }
    }

    return maxLen;
}



