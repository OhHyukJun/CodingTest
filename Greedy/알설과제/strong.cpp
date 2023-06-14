#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>

using namespace std;

vector<vector<int>> graph;
vector<int> color, discoverTime, low, scc;
stack<int> discoverStack;
int Time, sccNumber;

void DFS(int u) {
    color[u] = 1; //1�� gray
    discoverTime[u] = Time;
    Time++;
    low[u] = discoverTime[u];
    discoverStack.push(u);
 
    for (int j = 0; j < graph[u].size(); j++) {
        int v = graph[u][j];
        if (color[v] == 0) { //color�� white�̸�
            DFS(v);
            low[u] = min(low[u], low[v]);
        }
        else if (scc[v] == -1) {
            low[u] = min(low[u], discoverTime[v]);
        }
    }

    if (low[u] >= discoverTime[u]) {
        int y;
        while (y != u) {
            y = discoverStack.top(); //y�� �ʱⰪ�� ������ �ֻ��� �� 
            discoverStack.pop(); // y�� discoverStack���� pop�� ����
            scc[y] = sccNumber;
        }
        sccNumber++;
    }
}

int main() {
    int n, m;
    Time = 1;
    sccNumber = 1;

    cin >> n >> m;

    graph.resize(n + 1); 
    //�迭�� ũ�⸦ ���Ҵ��ϴ� �Լ� ũ�⸦ n+1�� �Ҵ�

    for (int i = 0; i <= n + 1; i++) {    
        color.push_back(0);
        discoverTime.push_back(Time);
        low.push_back(Time);
        scc.push_back(-1);
    } //�� ���͵� �ʱ�ȭ

    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        graph[u].push_back(v);
    }
    
    for (int u = 1; u <= n; u++) {
        if (color[u] == 0) { // color�� white
            DFS(u);
        }
    }


    cout << sccNumber-1 << endl;

    return 0;
}
