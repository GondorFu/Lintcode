class Solution {  
public:      
    /** 
     * @param strs: A list of strings 
     * @return: A list of strings 
     */  
    vector<string> anagrams(vector<string> &strs) {  
        // write your code here  
        map<string, int> m;
        for(auto s:strs){
            sort(s.begin(), s.end());
            m[s]++;
        }
        
        vector<string> res;
        for(auto s:strs){
            auto temp = s;
            sort(temp.begin(), temp.end());
            if(m[temp] > 1)
                res.push_back(s);
                
        }
        
        return res;
    }  
};  
