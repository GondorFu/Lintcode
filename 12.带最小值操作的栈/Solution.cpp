class MinStack {
public:
    MinStack() {
        // do initialization if necessary
        
    }

    void push(int number) {
        // write your code here
        data.push(number);
        if(mins.empty() || number <= mins.top())
            mins.push(number);
        else{
            mins.push(mins.top());
        }
    }

    int pop() {
        // write your code here
        mins.pop();
        int res = data.top();
        data.pop();
        return res;
    }

    int min() {
        // write your code here
        int res = mins.top();
    }

private:
    stack<int> data;
    stack<int> mins;
};
