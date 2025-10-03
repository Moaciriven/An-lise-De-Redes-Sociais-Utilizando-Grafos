import pandas as pd
import networkx as nx

# -----------------------------
# 1. Carregar os dados
# -----------------------------
# Links entre artigos
df_links = pd.read_csv("links.tsv", sep="\t", header=None, names=["from", "to"], comment="#")

# Categorias dos artigos
df_categories = pd.read_csv("categories.tsv", sep="\t", header=None, names=["article", "category"], comment="#")

# -----------------------------
# 2. Criar o grafo direcionado
# -----------------------------
G = nx.DiGraph()
for _, row in df_links.iterrows():
    G.add_edge(row["from"], row["to"])

print(f"Grafo com {G.number_of_nodes()} nós e {G.number_of_edges()} arestas\n")

# -----------------------------
# 3. Questão 4: In-degree
# -----------------------------
in_degree = dict(G.in_degree())
top10_in_degree = sorted(in_degree.items(), key=lambda x: x[1], reverse=True)[:10]

print("Top 10 artigos por grau de entrada (in-degree):")
for node, deg in top10_in_degree:
    print(node, deg)

# -----------------------------
# 4. Questão 5: PageRank e comparação
# -----------------------------
pagerank = nx.pagerank(G)
top10_pagerank = sorted(pagerank.items(), key=lambda x: x[1], reverse=True)[:10]

print("\nTop 10 artigos por PageRank:")
for node, pr in top10_pagerank:
    print(node, round(pr,5))

# Comparação
set_in = {n for n,_ in top10_in_degree}
set_pr = {n for n,_ in top10_pagerank}

print("\nArtigos em ambas as listas:", set_in & set_pr)
print("Só no in-degree:", set_in - set_pr)
print("Só no PageRank:", set_pr - set_in)

# -----------------------------
# 5. Questão 7: PageRank por categoria
# -----------------------------
df_categories["pagerank"] = df_categories["article"].map(pagerank).fillna(0)
pr_por_cat = df_categories.groupby("category")["pagerank"].mean().sort_values(ascending=False)

print("\nPageRank médio por categoria (top 10):")
print(pr_por_cat.head(10))

# -----------------------------
# 6. Questão 8: Top artigo de 3 categorias diferentes
# -----------------------------
categorias_escolhidas = pr_por_cat.head(3).index.tolist()
print("\nArtigos mais importantes em 3 categorias diferentes:")
for cat in categorias_escolhidas:
    top_article = df_categories[df_categories["category"] == cat].sort_values("pagerank", ascending=False).iloc[0]
    print(f"Categoria: {cat} -> Artigo: {top_article['article']} (PR={top_article['pagerank']:.5f})")

# -----------------------------
# 7. Questão 9: Categorias com menor PageRank
# -----------------------------
print("\nCategorias com menor PageRank médio (10 menores):")
print(pr_por_cat.tail(10))

# -----------------------------
# 8. Questão 10: Vizinhança de um artigo do top 5 PageRank
# -----------------------------
top5_article = top10_pagerank[0][0]  # artigo de maior PageRank
in_neighbors = list(G.predecessors(top5_article))
out_neighbors = list(G.successors(top5_article))

print(f"\nArtigo do top 5 PageRank: {top5_article}")
print(f"Recebe links de {len(in_neighbors)} artigos")
print(f"Aponta para {len(out_neighbors)} artigos")

# -----------------------------
# 9. Questão 11: Artigo com alto grau de saída mas PageRank baixo
# -----------------------------
out_degree = dict(G.out_degree())
# Considerando grau de saída > 100 como alto
high_out = {n:d for n,d in out_degree.items() if d > 100}
low_pr_high_out = sorted(high_out.keys(), key=lambda x: pagerank.get(x,0))[:5]

print("\nArtigos com alto grau de saída (>100) e PageRank baixo:")
for a in low_pr_high_out:
    print(f"{a} -> Out-degree: {out_degree[a]}, PR: {pagerank.get(a,0):.5f}")

# -----------------------------
# 10. Questão 12: Artigo ponte entre categorias
# -----------------------------
# Um exemplo clássico: English_language
bridge_article = "English_language"
in_neighbors_bridge = list(G.predecessors(bridge_article))
out_neighbors_bridge = list(G.successors(bridge_article))

print(f"\nArtigo ponte: {bridge_article}")
print(f"Recebe links de {len(in_neighbors_bridge)} artigos de diferentes categorias")
print(f"Aponta para {len(out_neighbors_bridge)} artigos de diferentes categorias")
print(f"PageRank: {pagerank.get(bridge_article,0):.5f}")

