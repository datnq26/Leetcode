using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int[][] SortMatrix(int[][] grid) {
        int n = grid.Length;
        var dict = new Dictionary<int, List<int>>();

        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                int key = j - i;
                if (!dict.ContainsKey(key))
                    dict[key] = new List<int>();
                dict[key].Add(grid[i][j]);
            }
        }

        foreach (var key in dict.Keys)
        {
            if (key <= 0)
                dict[key].Sort((a, b) => b.CompareTo(a));
            else
                dict[key].Sort();
        }

        var index = dict.Keys.ToDictionary(k => k, k => 0);

        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                int key = j - i;
                grid[i][j] = dict[key][index[key]];
                index[key]++;
            }
        }

        return grid;
    }
}
