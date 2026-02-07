using System;

public class Solution
{
    public int MinimumDeletions(string s)
    {
        int rightA = 0;
        foreach (char c in s)
            if (c == 'a') rightA++;

        int leftB = 0;
        int ans = rightA; // split at i=0: delete all 'a' on the right

        foreach (char c in s)
        {
            if (c == 'a') rightA--;   // this 'a' moves to the left side
            else leftB++;             // this 'b' is now on the left side

            ans = Math.Min(ans, leftB + rightA);
        }

        return ans;
    }
}
