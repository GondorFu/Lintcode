class Solution {
public:
    /**
     * @return: The same instance of this class every time
     */
    static Solution* getInstance() {
        // write your code here
        static Solution INSTANCE;
        return &INSTANCE;
    }
    
protected:
    struct Object_Creator{
        Object_Creator(){Solution::getInstance();}
    };
    static Object_Creator _object_creator;
    
    Solution() {}
    ~Solution() {}
};