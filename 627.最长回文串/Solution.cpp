class Solution {
public:
    /**
     * @param s a string which consists of lowercase or uppercase letters
     * @return the length of the longest palindromes that can be built
     */
    int longestPalindrome(string& s) {
        // Write your code here
        map<char, int> mp;
        map<char, int>::iterator iter;
        for(int i=0; i<s.length(); i++){
            if(mp.find(s[i]) == mp.end())
                mp[s[i]] = 1;
            else
                mp[s[i]] += 1;
        }
        int flag = 0;
        int rlt = 0;
        for(iter = mp.begin(); iter != mp.end(); iter++){
            if(iter->second % 2 == 0)
                rlt += iter->second;
            else if(flag == 0){
                rlt += iter->second;
                flag = 1;
            }
            else
                rlt += iter->second - 1;
        }
        return rlt;
    }
};