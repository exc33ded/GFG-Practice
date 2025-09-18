class Solution {
  public:
    vector<int> nextGreater(vector<int> &arr) {
        // code here
        stack<int>temp;
        int big=max_element(arr.begin(),arr.end())-arr.begin();
        int n=arr.size();
        vector<int> res(n);
        res[big]=-1;
        temp.push(arr[big]);
        for(int i=big-1;i>=0;i--)
        {
            while(!temp.empty() && temp.top()<=arr[i]) temp.pop();
            if(temp.empty())
            res[i]=-1;
            else
            res[i]=temp.top();
            temp.push(arr[i]); 
        }
        // if(big==n-1) return res;
        for(int i=n-1;i>big;i--)
        {
            while(!temp.empty() && temp.top()<=arr[i]) temp.pop();
            if(temp.empty())
            res[i]=-1;
            else
            res[i]=temp.top();
            temp.push(arr[i]);
        }
        return res;
    }
};