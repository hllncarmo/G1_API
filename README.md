
# Aprendizado por Projeto Integrado (API)

Projeto baseado na metodologia Ágil SCRUM, procurando desenvolver a Proatividade, Autonomia, Colaboração e Entrega de Resultados dos estudantes envolvidos

# Índice
* [Projeto](#projeto)
* [Equipe](#equipe)
* [Objetivo do Projeto](#objetivo-do-projeto)
* [Cronograma das Sprints](#cronograma)
* [Backlog do produto](#Backlog-do-produto)
* [Burndown](#Burndown)
* [Competências desenvolvidas](#competências-desenvolvidas)
* [Autores](#autores)

# Projeto 
Projeto pedagógico alicerçado na Metodologia API para ensino-aprendizado focado no desenvolvimento de competências e fundamentada nos pilares de aprendizado com problemas reais (RPBL), validação externa e mentalidade ágil.  
Os resultados dos projetos devem obedecer ao Aviso Legal disponível no site da Fatec SJC com definição das datas do kickoff e das sprints.

Sprint | Previsão | Status| Histórico|
|------|--------|------|--------|
|Kick Off | 08/03/2024 | Concluído || 
|01| 19/04/2024 | Concluída | [Ver Relatório](https://github.com/hllncarmo/G1_API/blob/main/Docs/RelatórioS1.pdf) | 
|02| 10/05/2024 | Concluída | [Ver Relatório](https://github.com/hllncarmo/G1_API/blob/main/Docs/RelatorioSprint2.pdf) | 
|03| 07/06/2024 | A fazer | [Ver Relatório]() | 
|04| 21/06/2024| A fazer | [Ver Relatório]() | 
|Feira de Soluções| 27/06/2024 | A fazer |[Ver Relatório]() | 

# Equipe
![Equipe](https://github.com/hllncarmo/G1_API/blob/main/WhatsApp%20Image%202024-04-15%20at%2012.26.31.jpeg)

# Objetivo do Projeto
Análise de produtividade de veículos, de otimização de distribuição e de custos de rotas de uma empresa embarcadora de carga
* Criar e modelar banco de dados em SQL.
* Criação de visualizador de indicadores no BI.
* Aplicação do método de transporte para otimização da distribuição.

## Tecnologias Utilizadas
 ### Tecnológias Específicas/Apoio
 * Jira
 * Power Bi
 * Excel
 * Power Point
 * MySQL
 * Chat GPT e Copilot
 * Phyton

## Cronograma
Ao clicar você será redirecionado ao cronograma detalhado desse projeto, lá é possivel encontar as datas das atividades, o responsável por cada atividade, o estágio em que cada atividade se encontra e a qual sprint cada atividade pertence.

#### Cronograma das Sprints[ (clique aqui)](https://g3log-2semestre.atlassian.net/jira/software/projects/GA3/boards/2/backlog)

Requisitos funcionais 
- Conteúdo da apresentação   
- Relatórios 
  
Requisitos não funcionais
- Usar tecnologias especifícas/apoio/tecnológicas
- Metodologias ágil
- Power BI / Jira
- MySQL
- Chat GPT e Copilot
- Phyton

# Backlog do produto

## Sprint 1. Concepção

<details>
<summary>Tarefas Sprint 1</summary>
 
- [x] Criar relatório da Sprint;
- [x] Estruturar Jira;
- [x] Estruturar Github;
- [x] Verificar a existência de erros nas bases de dados apresentadas e identificá-los;
- [x] Fazer Burndown da Estimativa das atividades;
- [x] Estruturar base de dados MySQL;

</details>

<details>
<summary>MVP Sprint 1</summary>

![MVP2](https://github.com/hllncarmo/G1_API/blob/main/Img/MVP1.png)
![MVP2](https://github.com/hllncarmo/G1_API/blob/main/Img/MVP2.png)

</details>

<details>
<summary>Burndown Sprint 1</summary>
 
![BRDW1](https://github.com/hllncarmo/G1_API/blob/main/Img/Burndown.png)

</details>

## Sprint 2. Back-end

<details>
<summary>Tarefas Sprint 2</summary>
 
- [X] Estabelecer conexão MySQL > PowerBI
- [X] Criar estrutura de dados PowerBI
- [X] Criar padrão das views para PowerBI
- [X] Criar Código inicial para Otimização
- [X] Definir modelo de otimização
- [X] Criar os KPIs
- [X] Corrigir outliers e erros da base
- [X] Tirar dúvidas com o cliente
- [X] Montar views iniciais para o projeto
- [X] Criar relatório da sprint
- [X] Fazer Power Point para apresentação da sprint
- [X] Atualizar GitHub
</details>

<details>
<summary>MVP Sprint 2</summary>

### MVP da Sprint 2
- Telas Inicias Para o Power Bi
  ![MVPS2](https://github.com/hllncarmo/G1_API/blob/main/Img/TelaBi.jpg)
- Primeiro Código para otimização
```python 
 from pulp import LpMinimize, LpProblem, lpSum, LpVariable, LpStatus

   # Define the problem data
  plants = [3403208, 3423909, 3424402]  # 3 plants
  customers = [2301, 2302, 2303, 2304, 2305, 
               2306, 2307, 2308, 2309, 2310, 
               2311, 2312, 2313, 2314, 2315, 
               2316, 2317, 2318, 2319, 2320, 
               2321, 2322, 2323, 2324, 2325, 
               2326, 2327, 2328, 2329, 2330, 
               2331, 2332, 2333, 2334, 2335, 
               2336, 2337, 2338, 2339, 2340, 
               2341, 2342, 2343, 2344, 2345, 
               2346, 2347, 2348, 2349, 2350, 
               2351]  # 51 customers
  
  transportation_costs = {
  	(3423909, 2311): 0.0008195227607521,
  	(3403208, 2301): 0.083098556,
  	(3403208, 2302): 0.0959718,
  	(3403208, 2303): 0.073410231,
  	(3403208, 2304): 0.000833955,
  	(3403208, 2305): 0.000754846,
  	(3403208, 2306): 0.000857057,
  	(3403208, 2307): 0.1063934,
  	(3403208, 2308): 0.000818302,
  	(3403208, 2309): 0.000970116,
  	(3403208, 2310): 0.001763784,
  	(3403208, 2311): 0.00065115,
  	(3403208, 2312): 0.001376759,
  	(3403208, 2313): 0.188478712,
  	(3403208, 2314): 0.050510988,
  	(3403208, 2315): 0.001593072,
  	(3403208, 2316): 0.001849338,
  	(3403208, 2317): 0.092174201,
  	(3403208, 2318): 0.001238375,
  	(3403208, 2319): 0.001328067,
  	(3403208, 2320): 0.152242067,
  	(3403208, 2321): 0.089610694,
  	(3403208, 2322): 0.001277949,
  	(3403208, 2323): 0.155357067,
  	(3403208, 2324): 0.000963045,
  	(3403208, 2325): 0.124359978,
  	(3403208, 2326): 0.000638521,
  	(3403208, 2327): 0.001089962,
  	(3403208, 2328): 0.001099177,
  	(3403208, 2329): 0.195217885,
  	(3403208, 2330): 0.071775025,
  	(3403208, 2331): 0.001126749,
  	(3403208, 2332): 0.062108438,
  	(3403208, 2333): 0.107758794,
  	(3403208, 2334): 0.001241036,
  	(3403208, 2335): 0.001076807,
  	(3403208, 2336): 999999,
  	(3403208, 2337): 999999,
  	(3403208, 2338): 999999,
  	(3403208, 2339): 0.11130875,
  	(3403208, 2340): 0.00175132,
  	(3403208, 2341): 0.001677139,
  	(3403208, 2342): 0.001269774,
  	(3403208, 2343): 0.001600825,
  	(3403208, 2344): 0.001103101,
  	(3403208, 2345): 0.001273323,
  	(3403208, 2346): 0.07951125,
  	(3403208, 2347): 0.00505025,
  	(3403208, 2348): 0.001069554,
  	(3403208, 2349): 0.1966195,
  	(3403208, 2350): 0.000737253,
  	(3403208, 2351): 0.035504178,
  	(3423909, 2301): 999999,
  	(3423909, 2302): 999999,
  	(3423909, 2303): 999999,
  	(3423909, 2304): 999999,
  	(3423909, 2305): 0.002361481,
  	(3423909, 2306): 999999,
  	(3423909, 2307): 999999,
  	(3423909, 2308): 0.002435014,
  	(3423909, 2309): 0.011163711,
  	(3423909, 2310): 0.000490668,
  	(3423909, 2311): 0.002173528,
  	(3423909, 2312): 999999,
  	(3423909, 2313): 999999,
  	(3423909, 2314): 999999,
  	(3423909, 2315): 999999,
  	(3423909, 2316): 999999,
  	(3423909, 2317): 999999,
  	(3423909, 2318): 999999,
  	(3423909, 2319): 999999,
  	(3423909, 2320): 999999,
  	(3423909, 2321): 999999,
  	(3423909, 2322): 999999,
  	(3423909, 2323): 999999,
  	(3423909, 2324): 0.0645915,
  	(3423909, 2325): 999999,
  	(3423909, 2326): 0.000976607,
  	(3423909, 2327): 0.074768885,
  	(3423909, 2328): 0.000369302,
  	(3423909, 2329): 0.000629951,
  	(3423909, 2330): 0.000674545,
  	(3423909, 2331): 0.001068954,
  	(3423909, 2332): 0.063041611,
  	(3423909, 2333): 0.628467,
  	(3423909, 2334): 0.005974944,
  	(3423909, 2335): 0.004159029,
  	(3423909, 2336): 0.001160086,
  	(3423909, 2337): 0.000669215,
  	(3423909, 2338): 0.000895017,
  	(3423909, 2339): 0.059599383,
  	(3423909, 2340): 0.000570971,
  	(3423909, 2341): 0.00096336,
  	(3423909, 2342): 0.000885295,
  	(3423909, 2343): 0.000527028,
  	(3423909, 2344): 999999,
  	(3423909, 2345): 999999,
  	(3423909, 2346): 999999,
  	(3423909, 2347): 0.00098037,
  	(3423909, 2348): 0.001231035,
  	(3423909, 2349): 0.073297456,
  	(3423909, 2350): 0.001075844,
  	(3423909, 2351): 0.063783659,
  	(3424402, 2301): 0.000346899,
  	(3424402, 2302): 0.000561724,
  	(3424402, 2303): 0.000784609,
  	(3424402, 2304): 0.000677017,
  	(3424402, 2305): 0.000298686,
  	(3424402, 2306): 0.000691641,
  	(3424402, 2307): 0.000307238,
  	(3424402, 2308): 0.000687612,
  	(3424402, 2309): 0.00017592,
  	(3424402, 2310): 0.004571612,
  	(3424402, 2311): 0.000300203,
  	(3424402, 2312): 999999,
  	(3424402, 2313): 999999,
  	(3424402, 2314): 999999,
  	(3424402, 2315): 999999,
  	(3424402, 2316): 999999,
  	(3424402, 2317): 999999,
  	(3424402, 2318): 999999,
  	(3424402, 2319): 0.002830106,
  	(3424402, 2320): 0.08292375,
  	(3424402, 2321): 0.1658475,
  	(3424402, 2322): 0.001063248,
  	(3424402, 2323): 0.146365962,
  	(3424402, 2324): 0.054487753,
  	(3424402, 2325): 0.073182981,
  	(3424402, 2326): 0.000882541,
  	(3424402, 2327): 0.146365962,
  	(3424402, 2328): 0.000961346,
  	(3424402, 2329): 0.163528077,
  	(3424402, 2330): 0.066339,
  	(3424402, 2331): 0.000671448,
  	(3424402, 2332): 0.105039667,
  	(3424402, 2333): 0.1914395,
  	(3424402, 2334): 0.001022395,
  	(3424402, 2335): 0.000715582,
  	(3424402, 2336): 0.001899043,
  	(3424402, 2337): 0.001085629,
  	(3424402, 2338): 0.001241254,
  	(3424402, 2339): 999999,
  	(3424402, 2340): 999999,
  	(3424402, 2341): 999999,
  	(3424402, 2342): 999999,
  	(3424402, 2343): 999999,
  	(3424402, 2344): 0.000797775,
  	(3424402, 2345): 0.000914069,
  	(3424402, 2346): 0.042719844,
  	(3424402, 2347): 0.001318893,
  	(3424402, 2348): 0.001725242,
  	(3424402, 2349): 0.275556667,
  	(3424402, 2350): 0.001698401,
  	(3424402, 2351): 0.378577157
  }
  
  customer_demands = {
      2301:	5973721,
      2302:	1778080, 
      2303:	5958798, 
      2304:	896173, 
      2305:	3241494, 
      2306:	3244827, 
      2307:	12738726, 
      2308:	6792503, 
      2309:	7471374, 
      2310:	2098730, 
      2311:	7295028, 
      2312:	1350774, 
      2313:	1439856, 
      2314:	3977784, 
      2315:	3666906, 
      2316:	271034, 
      2317:	1272373, 
      2318:	569236, 
      2319:	1589336, 
      2320:	5063433, 
      2321:	10686204, 
      2322:	2495205, 
      2323:	1753764, 
      2324:	20427048, 
      2325:	7828763, 
      2326:	5788209, 
      2327:	11836544, 
      2328:	6145143, 
      2329:	13860432, 
      2330:	3482379, 
      2331:	4084642, 
      2332:	10839219, 
      2333:	1336988, 
      2334:	1898750, 
      2335:	14197671, 
      2336:	1716192, 
      2337:	827342, 
      2338:	2539443, 
      2339:	1789064, 
      2340:	973767, 
      2341:	5304924, 
      2342:	838856, 
      2343:	8150094, 
      2344:	678417, 
      2345:	3600095, 
      2346:	3522678, 
      2347:	3675315, 
      2348:	1310374, 
      2349:	1761137, 
      2350:	4402893, 
      2351:	1331761 
  }
  
  plant_supplies = {
      3403208: 90000000,
      3423909: 90000000,
      3424402: 90000000
  }
  
  # Create the linear programming problem
  prob = LpProblem("Transportation_Cost_Minimization", LpMinimize)
  
  # Define the decision variables
  shipments = LpVariable.dicts("Shipments", (plants, customers), 0, None, cat='Integer')
  
  # Define the objective function
  try:
      prob += lpSum([transportation_costs[(p, c)] * shipments[p][c] for p in plants for c in customers])
  except KeyError as e:
      print(f"Missing combination: {e}")
  # Define the constraints
  for p in plants:
      prob += lpSum([shipments[p][c] for c in customers]) <= plant_supplies[p]
  
  for c in customers:
      prob += lpSum([shipments[p][c] for p in plants]) == customer_demands[c]
  
  
  
  # Solve the problem
  prob.solve()
  
  # Print the results
  print("Status:", LpStatus[prob.status])
  for v in prob.variables():
      print(v.name, "=", v.varValue)

```

</details>


<details>
<summary>Burndown Sprint 2</summary>

![BRDW2](https://github.com/hllncarmo/G1_API/blob/main/Img/BurnDown2.jpg)

</details>

## Sprint 3. Front-end

<details>
<summary>Tarefas Sprint 3</summary>
 
- [X] Modelar telas adicionais do Power Bi
- [X] Modelar as visões para o padrão estabelecido
- [X] Utilizar o modelo definido para executar a otimização
- [X] Criar Visualização de otimização de rotas por veiculo
- [X] Montar views iniciais
- [X] Criar relatório da Sprint
- [X] Tirar dúvidas com o cliente
- [X] Atualizar GitHub
- [X] Verificar possibilidade de views complementares

</details>

<details>
<summary>MVP Sprint 3</summary>

### Visualizações no Power Bi com os dados da otimização
- Telas Power Bi
  ![MVPS2](https://github.com/hllncarmo/G1_API/blob/main/Img/TelaBi.jpg)
- Primeiro Código para otimização
```python
from pulp import LpMinimize, LpProblem, lpSum, LpVariable, LpStatus

# Define the problem data
plants = [3403208, 3423909, 3424402]  # 3 plants
customers = [2301, 2302, 2303, 2304, 2305, 
             2306, 2307, 2308, 2309, 2310, 
             2311, 2312, 2313, 2314, 2315, 
             2316, 2317, 2318, 2319, 2320, 
             2321, 2322, 2323, 2324, 2325, 
             2326, 2327, 2328, 2329, 2330, 
             2331, 2332, 2333, 2334, 2335, 
             2336, 2337, 2338, 2339, 2340, 
             2341, 2342, 2343, 2344, 2345, 
             2346, 2347, 2348, 2349, 2350, 
             2351]  # 51 customers

transportation_costs = {
	(3403208, 2301): 0.581689889,
	(3403208, 2302): 0.479859,
	(3403208, 2303): 0.440461389,
	(3403208, 2304): 0.456173529,
	(3403208, 2305): 0.492159853,
	(3403208, 2306): 0.544231152,
	(3403208, 2307): 0.531967,
	(3403208, 2308): 0.540897912,
	(3403208, 2309): 0.424910965,
	(3403208, 2310): 0.714332699,
	(3403208, 2311): 0.403713274,
	(3403208, 2312): 0.788882677,
	(3403208, 2313): 0.753914848,
	(3403208, 2314): 0.707153831,
	(3403208, 2315): 0.825211267,
	(3403208, 2316): 0.834051632,
	(3403208, 2317): 0.829567813,
	(3403208, 2318): 0.821042543,
	(3403208, 2319): 0.690594586,
	(3403208, 2320): 0.761210333,
	(3403208, 2321): 0.80649625,
	(3403208, 2322): 0.691370481,
	(3403208, 2323): 0.776785333,
	(3403208, 2324): 0.704948765,
	(3403208, 2325): 0.621799889,
	(3403208, 2326): 0.693433396,
	(3403208, 2327): 0.706295309,
	(3403208, 2328): 0.725456763,
	(3403208, 2329): 0.780871538,
	(3403208, 2330): 0.78952527,
	(3403208, 2331): 0.691823939,
	(3403208, 2332): 0.683192821,
	(3403208, 2333): 0.646552766,
	(3403208, 2334): 0.67760587,
	(3403208, 2335): 0.687003068,
	(3403208, 2336): 999999,
	(3403208, 2337): 999999,
	(3403208, 2338): 999999,
	(3403208, 2339): 0.89047,
	(3403208, 2340): 0.956220721,
	(3403208, 2341): 0.902300672,
	(3403208, 2342): 0.892650771,
	(3403208, 2343): 0.973301747,
	(3403208, 2344): 0.629870511,
	(3403208, 2345): 0.63538812,
	(3403208, 2346): 0.63609,
	(3403208, 2347): 0.424221,
	(3403208, 2348): 0.319796772,
	(3403208, 2349): 0.393239,
	(3403208, 2350): 0.388532513,
	(3403208, 2351): 0.426050139,
	(3423909, 2301): 999999,
	(3423909, 2302): 999999,
	(3423909, 2303): 999999,
	(3423909, 2304): 999999,
	(3423909, 2305): 0.384921411,
	(3423909, 2306): 999999,
	(3423909, 2307): 999999,
	(3423909, 2308): 0.384732184,
	(3423909, 2309): 0.424221,
	(3423909, 2310): 0.332182532,
	(3423909, 2311): 0.384714542,
	(3423909, 2312): 999999,
	(3423909, 2313): 999999,
	(3423909, 2314): 999999,
	(3423909, 2315): 999999,
	(3423909, 2316): 999999,
	(3423909, 2317): 999999,
	(3423909, 2318): 999999,
	(3423909, 2319): 999999,
	(3423909, 2320): 999999,
	(3423909, 2321): 999999,
	(3423909, 2322): 999999,
	(3423909, 2323): 999999,
	(3423909, 2324): 0.3229575,
	(3423909, 2325): 999999,
	(3423909, 2326): 0.353531597,
	(3423909, 2327): 0.373844423,
	(3423909, 2328): 0.354898829,
	(3423909, 2329): 0.367891282,
	(3423909, 2330): 0.420241744,
	(3423909, 2331): 0.351685809,
	(3423909, 2332): 0.378249667,
	(3423909, 2333): 0.628467,
	(3423909, 2334): 0.424221,
	(3423909, 2335): 0.424221,
	(3423909, 2336): 0.470995102,
	(3423909, 2337): 0.45372783,
	(3423909, 2338): 0.450193701,
	(3423909, 2339): 0.536394444,
	(3423909, 2340): 0.60808452,
	(3423909, 2341): 0.563565321,
	(3423909, 2342): 0.558621044,
	(3423909, 2343): 0.60713659,
	(3423909, 2344): 999999,
	(3423909, 2345): 999999,
	(3423909, 2346): 999999,
	(3423909, 2347): 0.677435774,
	(3423909, 2348): 0.720155369,
	(3423909, 2349): 0.586379648,
	(3423909, 2350): 0.673478162,
	(3423909, 2351): 0.637836585,
	(3424402, 2301): 0.442990636,
	(3424402, 2302): 0.409496915,
	(3424402, 2303): 0.407212002,
	(3424402, 2304): 0.394700974,
	(3424402, 2305): 0.41995255,
	(3424402, 2306): 0.401843269,
	(3424402, 2307): 0.423066157,
	(3424402, 2308): 0.401565675,
	(3424402, 2309): 0.467243454,
	(3424402, 2310): 0.416016692,
	(3424402, 2311): 0.548170849,
	(3424402, 2312): 999999,
	(3424402, 2313): 999999,
	(3424402, 2314): 999999,
	(3424402, 2315): 999999,
	(3424402, 2316): 999999,
	(3424402, 2317): 999999,
	(3424402, 2318): 999999,
	(3424402, 2319): 0.416025571,
	(3424402, 2320): 0.331695,
	(3424402, 2321): 0.331695,
	(3424402, 2322): 0.339176069,
	(3424402, 2323): 0.292731923,
	(3424402, 2324): 0.326926515,
	(3424402, 2325): 0.292731923,
	(3424402, 2326): 0.320362562,
	(3424402, 2327): 0.292731923,
	(3424402, 2328): 0.369156958,
	(3424402, 2329): 0.327056154,
	(3424402, 2330): 0.331695,
	(3424402, 2331): 0.349153,
	(3424402, 2332): 0.315119,
	(3424402, 2333): 0.382879,
	(3424402, 2334): 0.382879,
	(3424402, 2335): 0.342763801,
	(3424402, 2336): 0.719737191,
	(3424402, 2337): 0.699144814,
	(3424402, 2338): 0.693860886,
	(3424402, 2339): 999999,
	(3424402, 2340): 999999,
	(3424402, 2341): 999999,
	(3424402, 2342): 999999,
	(3424402, 2343): 999999,
	(3424402, 2344): 0.465102596,
	(3424402, 2345): 0.477143788,
	(3424402, 2346): 0.469918289,
	(3424402, 2347): 0.879701638,
	(3424402, 2348): 0.935080972,
	(3424402, 2349): 1.1022266667,
	(3424402, 2350): 1.0105483568,
	(3424402, 2351): 1.1357314706
}

customer_demands = {
    2301:	5973721,
    2302:	1778080, 
    2303:	5958798, 
    2304:	896173, 
    2305:	3241494, 
    2306:	3244827, 
    2307:	12738726, 
    2308:	6792503, 
    2309:	7471374, 
    2310:	2098730, 
    2311:	7295028, 
    2312:	1350774, 
    2313:	1439856, 
    2314:	3977784, 
    2315:	3666906, 
    2316:	271034, 
    2317:	1272373, 
    2318:	569236, 
    2319:	1589336, 
    2320:	5063433, 
    2321:	10686204, 
    2322:	2495205, 
    2323:	1753764, 
    2324:	20427048, 
    2325:	7828763, 
    2326:	5788209, 
    2327:	11836544, 
    2328:	6145143, 
    2329:	13860432, 
    2330:	3482379, 
    2331:	4084642, 
    2332:	10839219, 
    2333:	1336988, 
    2334:	1898750, 
    2335:	14197671, 
    2336:	1716192, 
    2337:	827342, 
    2338:	2539443, 
    2339:	1789064, 
    2340:	973767, 
    2341:	5304924, 
    2342:	838856, 
    2343:	8150094, 
    2344:	678417, 
    2345:	3600095, 
    2346:	3522678, 
    2347:	3675315, 
    2348:	1310374, 
    2349:	1761137, 
    2350:	4402893, 
    2351:	1331761 
}

plant_supplies = {
    3403208: 90000000,
    3423909: 90000000,
    3424402: 90000000
}
# Create the linear programming problem
prob = LpProblem("Transportation_Cost_Minimization", LpMinimize)

# Define the decision variables
shipments = LpVariable.dicts("Shipments", (plants, customers), 0, None, cat='Integer')

# Define the objective function
try:
    prob += lpSum([transportation_costs[(p, c)] * shipments[p][c] for p in plants for c in customers])
except KeyError as e:
    print(f"Missing combination: {e}")
# Define the constraints
for p in plants:
    prob += lpSum([shipments[p][c] for c in customers]) <= plant_supplies[p]

for c in customers:
    prob += lpSum([shipments[p][c] for p in plants]) == customer_demands[c]



# Solve the problem
prob.solve()

# Print the results
print("Status:", LpStatus[prob.status])
for v in prob.variables():
    print(v.name, "=", v.varValue)
```
</details>


<details>
<summary>Burndown Sprint 3</summary>

![BRDW2](https://github.com/hllncarmo/G1_API/blob/main/Img/BurnDown2.jpg)

</details>

## Sprint 4. Final

<details>
<summary>Tarefas Sprint 4</summary>

- [ ] Ajustes Finais no Power Bi
- [ ] Ajustes no código de otimização se necessários 
- [ ] Criar relatório final do projeto
- [ ] Tirar dúvidas com o cliente
- [ ] Criar apresentação para Sprint

</details>

<details>
<summary>MVP Sprint 4</summary>

### Conclusão do Projeto
### Apresentação Final

</details>

<details>
<summary>Burndown Sprint 4</summary>

![BRDW4](https://github.com/hllncarmo/G1_API/blob/main/Img/Burndown4.png)

</details>


# Competências desenvolvidas

## Hard Skill (saber tecnológico)
<details>
<summary>Hard Skills desenvolvidas</summary>
  
| Tecnologia/Metodologia | Classificação |
| ---------------------- | ------------- |
| GitHub | ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆  |
| Gestão de Projetos | ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ |
| Scrum Master | ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ |
| Prodct Owner | ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ |
| Markdown | ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ |
| Git Projects | ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ |
 
</details>

## Soft Skill (saber comportamental)
<details>
<summary>Soft Skills desenvolvidas</summary>

| Habilidades | Classificação |
| ---------------------- | ------------- |
| Colaboração | ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ |
| Proatividade| ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ |
| Comunicação | ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ |
| Adaptabilidade | ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ |
| Autonomia | ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ |

</details>

# Autores
|    Função     | Nome                                  |                                                                                                                                                      LinkedIn & GitHub                                                                                                                                                      |
| :-----------: | :------------------------------------ | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| Product Owner | Thayssa Andrade dos Santos        |      [![Linkedin Badge](https://img.shields.io/badge/Linkedin-blue?style=flat-square&logo=Linkedin&logoColor=white)](https://www.linkedin.com/in/thayssa-andrade-531a20200/)  |
| Scrum Master  | Ana Júlia do Couto Brandão        |         [![Linkedin Badge](https://img.shields.io/badge/Linkedin-blue?style=flat-square&logo=Linkedin&logoColor=white)](https://www.linkedin.com/in/ana-j%C3%BAlia-couto-brand%C3%A3o-60a78b20b/)        | 
|  Team Member  | Hellen de Sousa Santos Carmo      |   [![Linkedin Badge](https://img.shields.io/badge/Linkedin-blue?style=flat-square&logo=Linkedin&logoColor=white)](https://www.linkedin.com/in/hellen-sousa-26717b27b/) [![GitHub Badge](https://img.shields.io/badge/GitHub-111217?style=flat-square&logo=github&logoColor=white)](https://github.com/hllncarmo)   |
|  Team Member  | Marcos Vinicius Restani Avanzini  |   [![Linkedin Badge](https://img.shields.io/badge/Linkedin-blue?style=flat-square&logo=Linkedin&logoColor=white)](https://www.linkedin.com/in/marcos-avanzini-7544331b6/) [![GitHub Badge](https://img.shields.io/badge/GitHub-111217?style=flat-square&logo=github&logoColor=white)](https://github.com/MarcosAvanzini)   |
|  Team Member  | Pedro Luís Cordeiro Dias Lourenço |           [![Linkedin Badge](https://img.shields.io/badge/Linkedin-blue?style=flat-square&logo=Linkedin&logoColor=white)](https://www.linkedin.com/in/pedro-lu%C3%ADs-louren%C3%A7o-785314225/)          |
|  Team Member  | Steffany Caroline Vieira Santo    |   [![Linkedin Badge](https://img.shields.io/badge/Linkedin-blue?style=flat-square&logo=Linkedin&logoColor=white)](https://www.linkedin.com/in/steffanysantovi) [![GitHub Badge](https://img.shields.io/badge/GitHub-111217?style=flat-square&logo=github&logoColor=white)](https://github.com/Steffanysantovi) |
