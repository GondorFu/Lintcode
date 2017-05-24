class Solution {
public:
    /**
     * @param s : A string
     * @return : The length of the longest substring 
     *           that contains at most k distinct characters.
     */
    int lengthOfLongestSubstringKDistinct(string s, int k) {  
        // write your code here  
        int ret = 0;  
        int start = 0;  
        int end = 0;  
        map<char,int> m;  
        for(int i=0;i<s.length();i++)  
        {  
            m[s[i]]++;  
            end = i;  
            while(m.size()>k)  
            {  
                m[s[start]]--;  
                if(m[s[start]]==0)  
                    m.erase(m.find(s[start]));  
                start++;  
            }  
            ret = max(ret,end-start+1);  
        }  
        return ret;  
    }  
};  