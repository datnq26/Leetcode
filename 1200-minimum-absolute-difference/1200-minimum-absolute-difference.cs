public class Solution {
public IList<IList<int>> MinimumAbsDifference(int[] arr)
{
    Array.Sort(arr);

    int min = int.MaxValue;
    IList<IList<int>> res = new List<IList<int>>();

    for (int i = 0; i < arr.Length - 1; i++)
    {
        int diff = arr[i + 1] - arr[i];

        if (diff < min)
        {
            min = diff;
            res.Clear();
            res.Add(new List<int> { arr[i], arr[i + 1] });
        }
        else if (diff == min)
        {
            res.Add(new List<int> { arr[i], arr[i + 1] });
        }
    }

    return res;
}

}