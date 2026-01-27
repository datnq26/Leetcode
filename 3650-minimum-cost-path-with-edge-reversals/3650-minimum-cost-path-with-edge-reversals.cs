public class Solution {
public int MinCost(int n, int[][] edges)
{
    List<(int to, int cost)>[] graph = new List<(int, int)>[n];
    for (int i = 0; i < n; i++)
        graph[i] = new List<(int, int)>();

    foreach (var e in edges)
    {
        int u = e[0], v = e[1], w = e[2];
        graph[u].Add((v, w));
        graph[v].Add((u, 2 * w));
    }

    int[] dist = new int[n];
    Array.Fill(dist, int.MaxValue);
    dist[0] = 0;

    var pq = new PriorityQueue<int, int>();
    pq.Enqueue(0, 0);

    while (pq.Count > 0)
    {
        int u = pq.Dequeue();
        int d = dist[u];

        if (u == n - 1) return d;

        foreach (var (v, cost) in graph[u])
        {
            if (d + cost < dist[v])
            {
                dist[v] = d + cost;
                pq.Enqueue(v, dist[v]);
            }
        }
    }

    return -1;
}

}