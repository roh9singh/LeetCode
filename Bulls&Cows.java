

import java.util.Scanner;

public class Solution {
    public String getHint(String secret, String guess) {
        
        int s,i=0,j,a=0,b=0;
        String r;
        char[] flag= new char[secret.length()];
        
        for(i=0;i<secret.length();i++)
        {
            if(secret.charAt(i)==guess.charAt(i))
            {
                a++;
            }
            else
            {
                for(j=0;j<secret.length();j++)
                {
                    //s=(int)secret.charAt(i);
                    //c=""+secret.charAt(i);
                    //s=Integer.parseInt(c);
                    s=j;
                    if(secret.charAt(i)==guess.charAt(j) && guess.charAt(j)!=secret.charAt(j) && flag[s]!=1)
                    {
                        b++;
                        flag[s]=1;
                        break;
                    }
                }
            }    
        }
        
        r=a+"A"+b+"B";
        
        return r;
        
    }
}
