# Contato E-mail: felipekian@yahoo.com.br

# MAPEAMENTO AUTOMÁTICO DE ROTAS PARA VIA EXPRESSA DE ÔNIBUS : UMA ABORDAGEM COM ALGORITMOS EVOLUTIVOS COM ÊNFASE NA CIDADE DE BOA VISTA RR

## COMO EXECUTAR O PROJETO

 * Precisa instalar o **Anaconda** Python 3 -> https://www.anaconda.com/distribution/
 * Precisa instalar a lib **DEAP** -> https://deap.readthedocs.io/en/master/
 * Precisa instalar a lib **OSMnx** -> https://osmnx.readthedocs.io/en/stable/
 * Escolher uma das implementações:
    * Com **AG onemax (experimento I)**
    * Com **AG onemax + DFS (experimento II)**
    * Com **AG NSGA-II 3 obj (experimento III)**
    * Com **AG NSGA-II 5 obj (experimento IV)**

# EXECUÇÃO DE COMPARAÇÃO DOS MÉTODOS IMPLEMENTADOS

* **500 Gerações**
* **50 Cromossomos**

## PARA MAIS DETALHES CONFIRA O ARTIGO E O TCC ( NA PASTA  TCC E ARTIGO )


# ARQUITETURA PROPOSTA

![](imagens_markdown/arquitura_proposta.png)

![](imagens_markdown/exemplo_execucao.png)


# MAPA COMPLETO E COM TRATAMENTO

![](imagens_markdown/mapa_completo.png)

![](imagens_markdown/mapa_filtrado.png)


# RESULTADO EXPERIMENTO I - ONEMAX

![](imagens_markdown/grafico_quant_arestas_selecionadas_onemax.png)

![](imagens_markdown/grafico_tam_clicos_onemax.png)

![](imagens_markdown/mapaOnimax.png)

* Rota 1 - 13 Arestas:
    * 1ª - Avenida Amazonas
    * 2ª - Avenida Glaycon de Paiva
    * 3ª - Rua Araújo Filho
    * 4ª - Avenida Capitão Ene Garcez
    * 5ª - Rua Coronel Pinto
    * 6ª - Avenida Capitão Júlio Bezerra
    * 7ª - Avenida Amazonas


# RESULTADO EXPERIMENTO II - ONEMAX + DFS

![](imagens_markdown/grafico_quantidade_arestas_dfs.png)

![](imagens_markdown/grafico_rotas_validadas_dfs.png)

![](imagens_markdown/rota5_dfs.png)

* Rota 5 - 38 Arestas:
    * 1ª - Avenida Amazonas
    * 2ª - Avenida Mário Homem de Melo
    * 3ª - Rua Ajuricaba
    * 4ª - Rua Dom Pedro I
    * 5ª - Rua Cerejo Cruz
    * 6ª - Avenida Terêncio Lima
    * 7ª - Avenida Major Williams
    * 8ª - Rua Valério Magalhães
    * 9ª - Rua Coronel Mota
    * 10ª - Rua Professor Agnelo Bitencourt
    * 11ª - Rua Alfredo Cruz
    * 12ª - Avenida Capitão Júlio Bezerra
    * 13ª - Rua Coronel Pinto
    * 14ª - Avenida Ville Roy
    * 15ª - Avenida Amazonas


# RESULTADO EXPERIMENTO III - NSGA-II COM 3 OBJETIVOS 

![](imagens_markdown/grafico_distancia_percorrida_nsgaii_3obj.png)

![](imagens_markdown/grafico_quantidade_de_arestas_nsgaii_3obj.png)

![](imagens_markdown/grafico_quantidade_de_arestas_selecionadas_nsgaii_3obj.png)

![](imagens_markdown/grafico_rotas_validadas_nsgaii_3obj.png)

![](imagens_markdown/grafico_tempo_execucao_geracao_nsgaii_3obj.png)

![](imagens_markdown/rota10_nsgaii_3obj.png)

* Rota 10 - 46 Arestas:
     * Avenida Amazonas
     * Avenida Ville Roy
     * Rua Araújo Filho
     * Avenida Capitão Ene Garcez
     * Avenida Capitão Ene Garcêz
     * Rua Alfredo Cruz
     * Rua Professor Agnelo Bitencourt
     * Avenida Major Williams
     * Avenida Nossa Senhora da Consolata
     * Rua Barão do Rio Branco
     * Rua Coronel Mota
     * Avenida Amazonas


# RESULTADO EXPERIMENTO IV - NSGA-II COM 5 OBJETIVOS

![](imagens_markdown/grafico_distancia_percorrida_nsgaii_5obj.png)

![](imagens_markdown/grafico_distancia_percorrida_rotas_validadas_nsgaii_5obj.png)

![](imagens_markdown/grafico_quantidade_arestas_conexas_nsgaii_5obj.png)

![](imagens_markdown/grafico_quantidade_arestas_selecionadas_nsgaii_5obj.png)

![](imagens_markdown/grafico_quantidade_de_arestas_rotas_nsgaii_5obj.png)

![](imagens_markdown/grafico_tempo_execucao_nsgaii_5obj.png)

![](imagens_markdown/grafico_rotas_nsgaii_5obj.png)

![](imagens_markdown/rotas40_nsgaii_5obj.png)

* Rota 40 - 120 Arestas:
    * Avenida Amazonas
    * Avenida Ville Roy
    * Rua Araújo Filho
    * Avenida Glaycon de Paiva
    * Rua Ajuricaba
    * Rua Cecília Brasil
    * Rua Professor Diomedes Souto Maior
    * Rua Cerejo Cruz
    * Avenida Nossa Senhora da Consolata
    * Avenida Presidente Castelo Branco
    * Avenida Terêncio Lima
    * Rua Dom Pedro I
    * Avenida Capitão Ene Garcês
    * Avenida Forte São Joaquim
    * Rua Major Manoel Correia
    * Avenida Major Williams
    * Rua Valério Magalhães
    * Rua Coronel Mota
    * Rua Barão do Rio Branco
    * Rua Professor Agnelo Bitencourt
    * Avenida Benjamin Constant
    * Rua Coronel Pinto
    * Rua Alfredo Cruz
    * Avenida Amazonas
    
    
# VISÃO GERAL DAS RODADAS EXPERIMENTAIS

**LADO A LADO DA ÚLTIMA RODADA (RESULTADOS MOSTRADOS ACIMA)**

![](imagens_markdown/teste7.png)

![](imagens_markdown/TotArestasExperimentos.png)

**LADO A LADO TODAS AS RODADAS EXPERIMENTAIS**

![](imagens_markdown/testeAll.png)

![](imagens_markdown/testeArestasTotal.png)


# OBRIGADO POR PRESTIGIAR ESTUDO TRABALHO

# CONTADO E-mail: felipekian@yahoo.com.br
