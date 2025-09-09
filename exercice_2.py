import networkx as nx
from scipy.io import mmread
import os

def carregar_grafo(caminho_arquivo):
    if not os.path.exists(caminho_arquivo):
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho_arquivo}")
    
    print(f"Arquivo encontrado: {caminho_arquivo}")
    matriz = mmread(caminho_arquivo)
    return nx.from_scipy_sparse_array(matriz)

def exibir_info_basica(grafo):
    print(f"Número de nós: {grafo.number_of_nodes()}")
    print(f"Número de arestas: {grafo.number_of_edges()}")
    print(f"Densidade: {nx.density(grafo):.6f}")
    print(f"Grau médio: {sum(dict(grafo.degree()).values()) / grafo.number_of_nodes():.2f}")
    
    tipo = "direcionado" if nx.is_directed(grafo) else "não-direcionado"
    print(f"Tipo: Grafo {tipo}")
    
    if not nx.is_directed(grafo):
        conexo = nx.is_connected(grafo)
        print(f"Grafo conexo: {conexo}")
        if not conexo:
            print(f"Número de componentes conexos: {nx.number_connected_components(grafo)}")

def exibir_centralidades(grafo, top_n=5):
    print("\n--- MEDIDAS DE CENTRALIDADE ---")
    
    # Centralidade de grau
    if nx.is_directed(grafo):
        in_degree = nx.in_degree_centrality(grafo)
        out_degree = nx.out_degree_centrality(grafo)
        
        print(f"\nTop {top_n} nós - Centralidade de grau de entrada:")
        for no, centralidade in sorted(in_degree.items(), key=lambda x: x[1], reverse=True)[:top_n]:
            print(f"Nó {no}: {centralidade:.4f}")
            
        print(f"\nTop {top_n} nós - Centralidade de grau de saída:")
        for no, centralidade in sorted(out_degree.items(), key=lambda x: x[1], reverse=True)[:top_n]:
            print(f"Nó {no}: {centralidade:.4f}")
    else:
        degree = nx.degree_centrality(grafo)
        print(f"\nTop {top_n} nós - Centralidade de grau:")
        for no, centralidade in sorted(degree.items(), key=lambda x: x[1], reverse=True)[:top_n]:
            print(f"Nó {no}: {centralidade:.4f}")
    
    # Betweenness centrality (amostragem para grafos grandes)
    k = min(100, grafo.number_of_nodes())
    betweenness = nx.betweenness_centrality(grafo, k=k)
    print(f"\nTop {top_n} nós - Betweenness centrality:")
    for no, centralidade in sorted(betweenness.items(), key=lambda x: x[1], reverse=True)[:top_n]:
        print(f"Nó {no}: {centralidade:.4f}")
    
    # Closeness centrality
    closeness = nx.closeness_centrality(grafo)
    print(f"\nTop {top_n} nós - Closeness centrality:")
    for no, centralidade in sorted(closeness.items(), key=lambda x: x[1], reverse=True)[:top_n]:
        print(f"Nó {no}: {centralidade:.4f}")

def main():
    caminho = os.path.normpath(os.path.expanduser("/home/zeim/Downloads/inf-USAir97.mtx"))
    
    try:
        grafo = carregar_grafo(caminho)
        
        print("\n--- INFORMAÇÕES BÁSICAS DO GRAFO ---")
        exibir_info_basica(grafo)
        
        exibir_centralidades(grafo)
        
    except FileNotFoundError as e:
        print(f"Erro: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    main()
