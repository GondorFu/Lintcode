class Solution {
public:
    /**
     * Returns a index to the first occurrence of target in source,
     * or -1  if target is not part of source.
     * @param source string to be scanned.
     * @param target string containing the sequence of characters to match.
     */
    int strStr(const char *source, const char *target) {
        // write your code here
        if(source == NULL || target == NULL)
            return -1;
        vector<int> next = getNext(target);
        int ns = strlen(source), nt = strlen(target);
        int i = 0, j = 0;
        while(i<ns && j<nt){
            if(j == -1 || source[i] == target[j])
                i++, j++;
            else
                j = next[j];
        }
        if(j == nt)
            return i-nt;
        return -1;
    }
    
    vector<int> getNext(const char* target){
        vector<int> next(strlen(target) + 1);
        next[0] = -1;
        int i = 0, j = -1;
        while(i < strlen(target)){
            if(j == -1 || target[i] == target[j])
                next[++i] = ++j;
            else
                j = next[j];
        }
        return next;
    }
};
