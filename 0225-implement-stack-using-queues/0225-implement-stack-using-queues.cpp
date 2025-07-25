class MyStack {
private:
    vector<int> arr;
    int idx;

public:
    MyStack() {
        idx = -1;
    }

    void push(int x) {
        idx++;
        if (idx < arr.size()) {
            arr[idx] = x;
        } else {
            arr.push_back(x);
        }
    }

    int pop() {
        if (idx >= 0) {
            int val = arr[idx];
            idx--;
            return val;
        }
        return -1; // hoặc throw exception nếu stack rỗng
    }

    int top() {
        if (idx >= 0) {
            return arr[idx];
        }
        return -1; // hoặc throw exception nếu stack rỗng
    }

    bool empty() {
        return idx < 0;
    }
};
