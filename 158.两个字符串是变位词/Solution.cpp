class Solution {
public:
    /**
     * @param s: The first string
     * @param b: The second string
     * @return true or false
     */
    bool anagram(string s, string t) {
        // write your code here
        int lens = s.size(), lent = t.size();
		if(lens != lent)
			return false;
		vector<int> count(128,0);
		for (string::iterator it=s.begin(); it!=s.end(); it++)
			count[*it]++;
		for(string::iterator it=t.begin(); it!=t.end(); it++)
			if(--count[*it] < 0)
				return false;
		return true;
    }
};