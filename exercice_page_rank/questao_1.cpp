#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    // ---- Carrega artigos ----
    ifstream artFile("articles.tsv");
    string article;
    vector<string> articles;
    unordered_map<string, int> id; // map: nome -> índice
    int idx = 0;

    while (getline(artFile, article)) {
        articles.push_back(article);
        id[article] = idx++;
    }
    artFile.close();

    int N = articles.size();

    // ---- Grafo (lista de adjacência) ----
    vector<vector<int>> graph(N);

    ifstream linkFile("links.tsv");
    string from, to;
    while (linkFile >> from >> to) {
        if (id.count(from) && id.count(to)) {
            graph[id[from]].push_back(id[to]);
        }
    }
    linkFile.close();

    // ---- PageRank ----
    vector<double> pr(N, 1.0 / N);
    vector<double> new_pr(N, 0.0);

    double d = 0.85; // alfa
    double tol = 1.0e-6;
    double error = 1.0;
    int max_iter = 100; // segurança
    int iter = 0;
    
    while (error > tol * N && iter < max_iter) {
        fill(new_pr.begin(), new_pr.end(), (1.0 - d) / N);
    
        for (int u = 0; u < N; u++) {
            if (!graph[u].empty()) {
                double share = pr[u] / graph[u].size();
                for (int v : graph[u]) {
                    new_pr[v] += d * share;
                }
            } else {
                for (int v = 0; v < N; v++) {
                    new_pr[v] += d * pr[u] / N;
                }
            }
        }
    
        // calcula erro
        error = 0.0;
        for (int i = 0; i < N; i++) {
            error += fabs(new_pr[i] - pr[i]);
        }
    
        pr.swap(new_pr);
        iter++;
    }
    cerr << "Convergiu em " << iter << " iteracoes, erro=" << error << "\n";
    // ---- Ordena por maior PageRank ----
    vector<pair<double,string>> ranking;
    for (int i = 0; i < N; i++) {
        ranking.push_back({pr[i], articles[i]});
    }
    sort(ranking.rbegin(), ranking.rend());

    // ---- Imprime top 10 ----
    int topN = 10;
    for (int i = 0; i < topN && i < (int)ranking.size(); i++) {
        cout << ranking[i].second << "\t" << ranking[i].first << "\n";
    }

    return 0;
}

