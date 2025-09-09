# Análise da Rede de Aeroportos (inf-USAir97.mtx)

### Informações Básicas do Grafo
- **Número de nós:** 332  
- **Número de arestas:** 2126  
- **Densidade:** 0.0387 (≈ 3,87%)  
- **Grau médio:** 12.81  
- **Tipo:** Grafo não-direcionado  
- **Conexo:** Sim  

---

### Medidas de Centralidade

**Top 5 nós – Centralidade de Grau (mais conexões diretas):**
1. Nó **117** → 0.4199  
2. Nó **260** → 0.3565  
3. Nó **254** → 0.3051  
4. Nó **151** → 0.2840  
5. Nó **181** → 0.2840  

**Top 5 nós – Centralidade de Intermediação (*Betweenness*, “pontes” da rede):**
1. Nó **117** → 0.1904  
2. Nó **260** → 0.1696  
3. Nó **7** → 0.1287 _(mesmo sem estar entre os top em grau, é um conector importante)_  
4. Nó **46** → 0.0917  
5. Nó **151** → 0.0882  

**Top 5 nós – Centralidade de Proximidade (*Closeness*):**
1. Nó **117** → 0.6073  
2. Nó **260** → 0.5544  
3. Nó **66** → 0.5400  
4. Nó **254** → 0.5356  
5. Nó **200** → 0.5330  

---

### Interpretação dos Resultados

- **Aeroportos mais centrais:**  
  O nó **117** se destaca em todas as métricas, indicando que é o aeroporto mais estratégico da rede.  

- **Aeroporto conector:**  
  O nó **7**, embora não tenha grau alto, possui **betweenness** relevante (0.1287), funcionando como “ponte” entre regiões da rede.  

- **Densidade da rede:**  
  A rede é **esparsa** (apenas **3,87%** das conexões possíveis estão presentes).  
  Isso indica que **nem todos os aeroportos estão diretamente conectados entre si**, refletindo a estrutura real da malha aérea, que depende de **hubs centrais** para integração.  

---

### Questões Respondidas

- **Quais são os aeroportos mais centrais?**  
  Principalmente o **nó 117**, seguido de **260**, **254**, **151** e **181**.  

- **Existe algum aeroporto que conecta regiões desconectadas?**  
  Sim, o **nó 7** se destaca por sua intermediação, mesmo sem alto grau.  

- **A rede é densa ou esparsa? O que isso indica?**  
  A rede é **esparsa**, o que mostra dependência de poucos hubs para manter a conectividade global.  
