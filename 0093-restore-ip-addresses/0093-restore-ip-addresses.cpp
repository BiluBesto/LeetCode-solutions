class Solution {
public:
    vector<string> restoreIpAddresses(string s) {
        vector<string> res;
        string partres;
        string a,b,c,d;
        int x,y,z,w;
        for(int i = 0;i<3;i++)
        {
            for(int j = 0;j<3;j++)
            {
                for(int k = 0;k<3;k++)
                {
                    for(int l = 0 ; l < 3; l++){
                        if(i+j+k+l+4 != s.length())
                        {
                            continue;
                        }
                        a = s.substr(0,i+1);
                        b = s.substr(i+1,j+1);
                        c = s.substr(i+j+2,k+1);
                        d = s.substr(i+j+k+3,l+1);
                        x = stoi(a);
                        y = stoi(b);
                        z = stoi(c);
                        w = stoi(d);
                        if(((!a.starts_with('0') && a.length()>1)||a.length()==1) && (x>=0 && x<=255))
                        {
                            if(((!b.starts_with('0') && b.length()>1)||b.length()==1)&&(y>=0 && y<=255))
                            {
                                if(((!c.starts_with('0') && c.length()>1)||c.length()==1)&&(z>=0 && z<=255))
                                {
                                    if(((!d.starts_with('0') && d.length()>1)||d.length()==1)&&(w>=0 && w<=255))
                                    {
                                        partres = a+"."+b+"."+c+"."+d;
                                        res.push_back(partres);
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
        return res;
    }
};

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna