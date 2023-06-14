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
    color[u] = 1; //1은 gray
    discoverTime[u] = Time;
    Time++;
    low[u] = discoverTime[u];
    discoverStack.push(u);
 
    for (int j = 0; j < graph[u].size(); j++) {
        int v = graph[u][j];
        if (color[v] == 0) { //color가 white이면
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
            y = discoverStack.top(); //y의 초기값은 스택의 최상위 값 
            discoverStack.pop(); // y는 discoverStack에서 pop한 정점
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
    //배열의 크기를 재할당하는 함수 크기를 n+1로 할당

    for (int i = 0; i <= n + 1; i++) {    
        color.push_back(0);
        discoverTime.push_back(Time);
        low.push_back(Time);
        scc.push_back(-1);
    } //각 벡터들 초기화

    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        graph[u].push_back(v);
    }
    
    for (int u = 1; u <= n; u++) {
        if (color[u] == 0) { // color는 white
            DFS(u);
        }
    }


    cout << sccNumber-1 << endl;

    return 0;
}
