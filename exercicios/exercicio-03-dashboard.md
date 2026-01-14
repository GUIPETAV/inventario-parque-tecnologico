# 📊 Exercício 3: Dashboard Executivo no Power BI

## 🎯 Objetivo
Criar um dashboard interativo e profissional no Power BI para visualizar e analisar o inventário de ativos de TI, apresentando KPIs, tendências e insights acionáveis para a diretoria.

## 📚 Conceito: Business Intelligence para ITAM

Um dashboard executivo eficaz deve:
- ✅ Ser visualmente atrativo e profissional
- ✅ Apresentar informações claras e objetivas
- ✅ Permitir drill-down para detalhes
- ✅ Ser interativo e filtráve
- ✅ Contar uma história com os dados
- ✅ Gerar insights acionáveis

## 🛠️ Pré-requisitos

- Power BI Desktop instalado ([Download gratuito](https://powerbi.microsoft.com/desktop/))
- Dados de exemplo nas pastas:
  - `dados-exemplo/hardware-sample.csv`
  - `dados-exemplo/licencas-sample.csv`
  - `dados-exemplo/manutencao-sample.csv`

## 📝 Instruções

### Parte 1: Importação e Modelagem (20 min)

#### Passo 1.1: Importar Dados

1. Abra o Power BI Desktop
2. Clique em **Obter Dados** → **Texto/CSV**

3. Importe os 3 arquivos:
   - `hardware-sample.csv` → Renomeie tabela para "Hardware"
   - `licencas-sample.csv` → Renomeie para "Licencas"
   - `manutencao-sample.csv` → Renomeie para "Manutencao"

4. Para cada arquivo:
   - Clique em "Transformar Dados"
   - Verifique tipos de dados:
     - Datas devem ser tipo **Data**
     - Valores devem ser tipo **Número Decimal**
     - Textos tipo **Texto**
   - Remova espaços em branco: Transformar → Formatar → Limpar

#### Passo 1.2: Criar Relacionamentos

1. Vá em **Modelo** (ícone à esquerda)

2. Crie relacionamento:
   ```
   Hardware[ID_Ativo] → Manutencao[ID_Ativo]
   Cardinalidade: Um para Muitos (1:*)
   Direção: Ambas
   ```

3. Verifique se relacionamento está ativo (linha sólida)

#### Passo 1.3: Criar Tabela de Calendário

No Power BI, vá em **Dados** → **Nova Tabela** e insira:

```dax
Calendario = 
ADDCOLUMNS(
    CALENDAR(DATE(2020,1,1), DATE(2026,12,31)),
    "Ano", YEAR([Date]),
    "Mês", FORMAT([Date], "MMM"),
    "MesAno", FORMAT([Date], "MMM/YY"),
    "Trimestre", "T" & FORMAT([Date], "Q"),
    "NomeMes", FORMAT([Date], "MMMM")
)
```

Relacione com Hardware[Data_Aquisicao]

### Parte 2: Criar Medidas DAX (25 min)

#### Medidas Básicas

Vá em **Dados** → Clique com botão direito em "Hardware" → **Nova Medida**

```dax
Total Ativos = COUNTROWS(Hardware)
```

```dax
Ativos Ativos = 
CALCULATE(
    COUNTROWS(Hardware),
    Hardware[Status] = "Ativo"
)
```

```dax
Taxa Ativos Ativos = 
DIVIDE([Ativos Ativos], [Total Ativos], 0)
```

```dax
Valor Total Parque = SUM(Hardware[Valor_Aquisicao])
```

```dax
Valor Médio Ativo = 
DIVIDE([Valor Total Parque], [Total Ativos], 0)
```

#### Medidas de Garantia

```dax
Garantias Vencendo 30d = 
CALCULATE(
    COUNTROWS(Hardware),
    Hardware[Garantia_Fim] >= TODAY(),
    Hardware[Garantia_Fim] <= TODAY() + 30
)
```

```dax
Garantias Vencendo 60d = 
CALCULATE(
    COUNTROWS(Hardware),
    Hardware[Garantia_Fim] >= TODAY(),
    Hardware[Garantia_Fim] <= TODAY() + 60
)
```

```dax
Garantias Vencendo 90d = 
CALCULATE(
    COUNTROWS(Hardware),
    Hardware[Garantia_Fim] >= TODAY(),
    Hardware[Garantia_Fim] <= TODAY() + 90
)
```

```dax
Garantias Vencidas = 
CALCULATE(
    COUNTROWS(Hardware),
    Hardware[Garantia_Fim] < TODAY()
)
```

#### Medidas de Idade

```dax
Idade Média = 
AVERAGE(
    DATEDIFF(Hardware[Data_Aquisicao], TODAY(), YEAR)
)
```

```dax
Ativos Antigos (>5 anos) = 
CALCULATE(
    COUNTROWS(Hardware),
    DATEDIFF(Hardware[Data_Aquisicao], TODAY(), YEAR) > 5
)
```

#### Medidas de Licenças

```dax
Total Licencas = SUM(Licencas[Quantidade_Adquirida])
```

```dax
Licencas Utilizadas = SUM(Licencas[Quantidade_Utilizada])
```

```dax
Taxa Utilizacao Licencas = 
DIVIDE([Licencas Utilizadas], [Total Licencas], 0)
```

```dax
Licencas Disponiveis = [Total Licencas] - [Licencas Utilizadas]
```

```dax
Investimento Licencas = SUM(Licencas[Valor_Total])
```

#### Medidas de Manutenção

```dax
Total Manutencoes = COUNTROWS(Manutencao)
```

```dax
Custo Total Manutencao = SUM(Manutencao[Custo])
```

```dax
Tempo Medio Parada = 
AVERAGE(Manutencao[Tempo_Parada_Horas])
```

```dax
Custo Medio Manutencao = 
DIVIDE([Custo Total Manutencao], [Total Manutencoes], 0)
```

### Parte 3: Construir Página 1 - Visão Geral (30 min)

#### Layout da Página:

```
┌─────────────────────────────────────────────────────┐
│  📊 INVENTÁRIO DE TI - VISÃO EXECUTIVA             │
├──────────┬──────────┬──────────┬──────────┬─────────┤
│ [KPI 1]  │ [KPI 2]  │ [KPI 3]  │ [KPI 4]  │ [KPI 5]│
├──────────┴──────────┴──────────┴──────────┴─────────┤
│                                                      │
│  [Gráfico Barras - Tipo]    [Gráfico Pizza - Dept] │
│                                                      │
├──────────────────────────────────────────────────────┤
│  [Gráfico Linha - Evolução]                         │
├──────────────────────────────────────────────────────┤
│  [Tabela - Top 10 por Valor]                        │
└──────────────────────────────────────────────────────┘
```

#### 1. Cabeçalho

- Adicione caixa de texto no topo
- Texto: "📊 INVENTÁRIO DE TI - VISÃO EXECUTIVA"
- Fonte: Segoe UI, 24pt, Negrito
- Cor de fundo: Azul escuro (#003366)
- Cor do texto: Branco

#### 2. KPIs (Cartões)

Insira 5 **Cartões** com as medidas:

1. **Total de Ativos**
   - Medida: [Total Ativos]
   - Título: "Total de Ativos"
   - Cor: Azul

2. **Valor Total**
   - Medida: [Valor Total Parque]
   - Formato: Moeda R$
   - Título: "Valor do Parque"
   - Cor: Verde

3. **Taxa Ativos**
   - Medida: [Taxa Ativos Ativos]
   - Formato: Percentual
   - Título: "% Ativos em Operação"
   - Cor: Laranja

4. **Garantias Vencendo**
   - Medida: [Garantias Vencendo 30d]
   - Título: "Garantias Vencendo (30d)"
   - Cor: Vermelho

5. **Idade Média**
   - Medida: [Idade Média]
   - Formato: 1 decimal + " anos"
   - Título: "Idade Média"
   - Cor: Roxo

#### 3. Gráfico de Barras Clusterizado

- **Eixo:** Hardware[Tipo]
- **Valores:** [Total Ativos]
- **Título:** "Distribuição por Tipo de Equipamento"
- **Cores:** Gradiente azul
- **Rótulos de dados:** Ativados

#### 4. Gráfico de Rosca (Donut)

- **Legenda:** Hardware[Departamento]
- **Valores:** [Total Ativos]
- **Título:** "Ativos por Departamento"
- **Rótulos:** Percentuais

#### 5. Gráfico de Área

- **Eixo X:** Calendario[MesAno]
- **Eixo Y:** [Total Ativos]
- **Título:** "Evolução de Aquisições"
- **Cor:** Gradiente verde

#### 6. Tabela

Colunas:
- Hardware[Tipo]
- Hardware[Marca]
- Hardware[Modelo]
- [Valor Total Parque]
- Hardware[Departamento]

Configuração:
- Ordenar por Valor (decrescente)
- Top 10
- Formatação condicional em valor (barra de dados)

#### 7. Segmentadores (Filtros)

Adicione 3 **Segmentação de Dados**:
1. Hardware[Departamento]
2. Hardware[Status]
3. Calendario[Ano]

Estilo: Botões ou Lista

### Parte 4: Construir Página 2 - Hardware Detalhado (20 min)

#### Visualizações:

1. **Matriz: Configurações**
   - Linhas: Hardware[Processador]
   - Colunas: Hardware[RAM_GB]
   - Valores: [Total Ativos]

2. **Gráfico de Colunas Empilhadas: Idade**
   - Eixo: Criar grupos de idade (0-2, 3-4, 5+)
   - Valores: [Total Ativos]
   - Legenda: Hardware[Status]

3. **Gráfico de Barras: Garantias**
   - Categorias: "Vencida", "30d", "60d", "90d", "OK"
   - Valores: Medidas correspondentes

4. **Cartão KPI: Alertas**
   - [Ativos Antigos (>5 anos)]
   - [Garantias Vencidas]
   - Alertas visuais (vermelho se > 0)

### Parte 5: Construir Página 3 - Licenças (20 min)

#### Visualizações:

1. **KPIs:**
   - [Total Licencas]
   - [Taxa Utilizacao Licencas]
   - [Licencas Disponiveis]
   - [Investimento Licencas]

2. **Gráfico de Barras Horizontais:**
   - Eixo: Licencas[Software] (Top 10)
   - Valores: [Total Licencas]

3. **Gráfico de Dispersão:**
   - Eixo X: Licencas[Quantidade_Adquirida]
   - Eixo Y: Licencas[Quantidade_Utilizada]
   - Detalhes: Licencas[Software]
   - Linha de tendência: Y=X (ideal)

4. **Tabela: Alertas de Licenças**
   - Filtro: Onde Utilizada > Adquirida
   - Colunas: Software, Adquirida, Utilizada, Diferença

### Parte 6: Construir Página 4 - Manutenção (15 min)

#### Visualizações:

1. **KPIs:**
   - [Total Manutencoes]
   - [Custo Total Manutencao]
   - [Custo Medio Manutencao]
   - [Tempo Medio Parada]

2. **Gráfico de Colunas: Custos por Tipo**
   - Eixo: Manutencao[Tipo_Manutencao]
   - Valores: [Custo Total Manutencao]

3. **Gráfico de Linha: Evolução Mensal**
   - Eixo: Manutencao[Data_Manutencao] (Mês)
   - Valores: [Total Manutencoes], [Custo Total Manutencao]

4. **Tabela: Equipamentos com Mais Manutenções**
   - Agrupar por Hardware[ID_Ativo]
   - Contar manutenções
   - Somar custos

### Parte 7: Design e Refinamento (15 min)

#### Aplicar Tema Profissional:

1. Vá em **Exibir** → **Temas**
2. Escolha um tema corporativo (ex: "Executive")
3. Ou personalize:
   - Cor primária: #003366 (Azul escuro)
   - Cor secundária: #00A6A6 (Verde-azulado)
   - Cor de destaque: #FF6B35 (Laranja)

#### Formatação Geral:

- **Fonte padrão:** Segoe UI
- **Tamanho título:** 14pt
- **Bordas:** Arredondadas
- **Sombras:** Leves
- **Espaçamento:** Consistente (10px)

#### Adicionar Navegação:

1. Insira **Botões** no topo de cada página
2. Botões: "Visão Geral", "Hardware", "Licenças", "Manutenção"
3. Configure ação: **Navegação de página**

#### Adicionar Logos/Imagens:

1. Insira logo da empresa (canto superior direito)
2. Adicione ícones aos títulos
3. Use imagens para deixar visual mais atrativo

### Parte 8: Interatividade Avançada (10 min)

#### Configurar Drill-through:

1. Na página "Visão Geral", clique com botão direito no gráfico
2. Adicione **Drill-through** para página "Hardware"
3. Campo: Hardware[ID_Ativo]

#### Criar Dicas de Ferramentas:

1. Crie página oculta "Tooltip_Hardware"
2. Adicione detalhes: Specs, Garantia, Últimas Manutenções
3. Configure nas propriedades do visual

#### Adicionar Indicadores:

1. Crie **Indicadores** para diferentes visualizações
2. Ex: "Visão por Tipo" vs "Visão por Departamento"
3. Adicione botões para alternar

## 📊 Checklist de Qualidade

Verifique se seu dashboard tem:

### Conteúdo:
- [ ] Todos os KPIs principais visíveis
- [ ] Gráficos variados e apropriados
- [ ] Filtros interativos funcionando
- [ ] Dados atualizados corretamente

### Design:
- [ ] Paleta de cores consistente
- [ ] Layout organizado e limpo
- [ ] Textos legíveis (tamanho adequado)
- [ ] Logo/identidade visual

### Funcionalidade:
- [ ] Todos os relacionamentos funcionando
- [ ] Medidas calculando corretamente
- [ ] Filtros aplicando cross-filtering
- [ ] Navegação entre páginas funcional

### Profissionalismo:
- [ ] Sem erros de DAX
- [ ] Títulos descritivos
- [ ] Formatação numérica adequada (moeda, %)
- [ ] Sem dados de teste visíveis

## 🎯 Entregáveis

1. ✅ Arquivo .pbix completo (4 páginas)
2. ✅ Screenshot de cada página
3. ✅ Documento com:
   - Lista de todas as medidas DAX
   - Descrição dos insights principais
   - Recomendações baseadas nos dados

## 💡 Insights Esperados

Seu dashboard deve responder:

1. **Qual é a saúde geral do parque de TI?**
2. **Onde está concentrado o maior investimento?**
3. **Quais departamentos têm mais ativos?**
4. **Há equipamentos críticos próximos ao fim de garantia?**
5. **As licenças estão sendo bem utilizadas?**
6. **Qual é o custo de manutenção por tipo de equipamento?**
7. **Há tendência de aumento ou redução do parque?**

## 🏆 Critérios de Avaliação

| Critério | Peso | Pontos |
|----------|------|--------|
| Modelagem de dados correta | 20% | /20 |
| Medidas DAX funcionais | 25% | /25 |
| Visualizações apropriadas | 20% | /20 |
| Design profissional | 15% | /15 |
| Interatividade e filtros | 10% | /10 |
| Insights e recomendações | 10% | /10 |
| **TOTAL** | **100%** | **/100** |

## 🚀 Desafios Extras (Opcional)

Para quem quer ir além:

1. **Criar medidas de Time Intelligence:**
   - YTD (Year to Date)
   - MoM (Month over Month)
   - Comparação com ano anterior

2. **Implementar RLS (Row Level Security):**
   - Criar roles por departamento
   - Cada gestor vê apenas seus ativos

3. **Adicionar análise preditiva:**
   - Previsão de aquisições futuras
   - Estimativa de custos de manutenção

4. **Integrar com outras fontes:**
   - Dados financeiros (budget)
   - Tickets de suporte
   - Pesquisas de satisfação

## 📚 Recursos Adicionais

- [DAX Patterns](https://www.daxpatterns.com/)
- [Power BI Documentation](https://docs.microsoft.com/power-bi/)
- [Community Forum](https://community.powerbi.com/)

## 💼 Apresentação Executiva

Prepare uma apresentação de 5 minutos demonstrando:

1. **Situação Atual** (KPIs principais)
2. **Alertas e Riscos** (garantias, licenças)
3. **Oportunidades** (otimizações identificadas)
4. **Recomendações** (ações propostas)

---

**Tempo estimado:** 2-3 horas  
**Dificuldade:** ⭐⭐⭐⭐☆ (Avançado)  
**Pré-requisitos:** Power BI básico, DAX básico

**Boa sorte! 🚀**
