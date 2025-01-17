class Solution {
public:
    bool isAlienSorted(vector<string>& words, string order) 
    {
        unordered_map<char,char> m;
        for(int i=0;i<26;i++)
        {
            m[order[i]]=i+'a';
        }
        for(auto &w:words)
        {
            for(auto &ch:w)
            {
                ch=m[ch];
            }
        }
        return is_sorted(words.begin(),words.end());// check sorting 
        
    }
};
//if you like the solution plz upvote;