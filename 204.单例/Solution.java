class Solution {
    /**
     * @return: The same instance of this class every time
     */
    private static class Singleton{
        private static final Solution INSTANCE = new Solution();
    }
    private Solution () {}
    public static final Solution getInstance() {
        // write your code here
        return Singleton.INSTANCE;
    }
};