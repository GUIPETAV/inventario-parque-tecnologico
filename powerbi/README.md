# 📊 Dashboard Power BI - Inventário de TI

## 📌 Descrição

Este diretório contém instruções completas para criar um dashboard profissional de gestão de ativos de TI no Power BI Desktop.

**Nota:** Arquivos .pbix não foram incluídos neste repositório devido ao tamanho. Siga as instruções abaixo para criar seu próprio dashboard baseado no modelo especificado.

---

## 🎯 Objetivo do Dashboard

Fornecer uma visão executiva, interativa e em tempo real do inventário de TI, permitindo:

- ✅ Monitoramento de KPIs críticos
- ✅ Análise de distribuição de ativos
- ✅ Alertas de garantias e licenças
- ✅ Controle de custos e investimentos
- ✅ Identificação de oportunidades de otimização
- ✅ Suporte a decisões estratégicas

---

## 📊 Estrutura do Dashboard

### Página 1: Visão Geral Executiva
**Público-alvo:** Diretoria e C-Level

#### KPIs Principais (Cartões)
1. **Total de Ativos** - Quantidade total de equipamentos
2. **Valor do Parque** - Investimento total em R$
3. **Taxa de Ativos Ativos** - Percentual em operação
4. **Garantias Vencendo** - Alertas próximos 30 dias
5. **Idade Média** - Anos médios do parque

#### Visualizações
- **Gráfico de Barras:** Distribuição por tipo de equipamento
- **Gráfico de Rosca:** Distribuição por departamento
- **Gráfico de Área:** Evolução temporal de aquisições
- **Tabela:** Top 10 ativos por valor

#### Filtros (Segmentadores)
- Departamento
- Status (Ativo, Inativo, Manutenção)
- Ano de Aquisição
- Localização

---

### Página 2: Análise de Hardware
**Público-alvo:** Gerentes de TI e Infraestrutura

#### KPIs Específicos
- Total de Desktops/Notebooks/Servidores
- Equipamentos em manutenção
- Equipamentos com mais de 5 anos
- Distribuição de sistemas operacionais

#### Visualizações
- **Matriz:** Configurações (RAM x Processador)
- **Gráfico de Colunas:** Distribuição por faixa de idade
- **Gráfico de Barras:** Status de garantias
- **Gráfico de Pizza:** Tipos de armazenamento (SSD/HDD)
- **Tabela Detalhada:** Lista completa com specs

#### Alertas Visuais
- 🔴 Garantias vencidas
- 🟠 Equipamentos antigos (>5 anos)
- 🟡 Em manutenção prolongada

---

### Página 3: Gestão de Licenças
**Público-alvo:** Gestor de Licenças e Compliance

#### KPIs Específicos
- Total de Licenças Adquiridas
- Taxa de Utilização (%)
- Licenças Disponíveis
- Investimento Total em Licenças
- Licenças Vencendo (30/60/90 dias)

#### Visualizações
- **Gráfico de Barras Horizontais:** Top 10 softwares por quantidade
- **Gráfico de Dispersão:** Adquiridas vs Utilizadas
  - Linha de referência Y=X (uso ideal)
  - Pontos acima = risco compliance
  - Pontos abaixo = subutilização
- **Gráfico de Colunas Empilhadas:** Utilização por fabricante
- **Tabela de Alertas:** Licenças em situação crítica

#### Indicadores de Compliance
- ✅ Verde: Taxa 80-100%
- ⚠️ Amarelo: Taxa <80% (subutilização)
- ❌ Vermelho: Uso >100% (risco legal)

---

### Página 4: Histórico de Manutenção
**Público-alvo:** Equipe de Suporte e Manutenção

#### KPIs Específicos
- Total de Manutenções (período)
- Custo Total de Manutenção
- Custo Médio por Manutenção
- Tempo Médio de Parada
- Equipamentos Mais Problemáticos

#### Visualizações
- **Gráfico de Colunas:** Custos por tipo de manutenção
- **Gráfico de Linha:** Evolução mensal de manutenções
- **Gráfico de Barras:** Equipamentos com mais chamados
- **Mapa de Calor:** Manutenções por departamento x mês
- **Tabela:** Últimas manutenções realizadas

#### Análise de Tendências
- Identificar equipamentos problemáticos
- Custos crescentes (avaliar substituição)
- Padrões sazonais

---

## 🧮 Medidas DAX Essenciais

### Medidas Básicas de Hardware

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
Valor Médio por Ativo = 
DIVIDE([Valor Total Parque], [Total Ativos], 0)
```

### Medidas de Garantia

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

```dax
Status Garantia = 
SWITCH(
    TRUE(),
    [Garantias Vencidas] > 0, "🔴 CRÍTICO",
    [Garantias Vencendo 30d] > 0, "🟠 ALERTA",
    "✅ OK"
)
```

### Medidas de Idade e Obsolescência

```dax
Idade Média = 
AVERAGEX(
    Hardware,
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

```dax
Percentual Ativos Antigos = 
DIVIDE([Ativos Antigos (>5 anos)], [Total Ativos], 0)
```

### Medidas de Licenças

```dax
Total Licencas = SUM(Licencas[Quantidade_Adquirida])
```

```dax
Licencas Utilizadas = SUM(Licencas[Quantidade_Utilizada])
```

```dax
Licencas Disponiveis = [Total Licencas] - [Licencas Utilizadas]
```

```dax
Taxa Utilizacao Licencas = 
DIVIDE([Licencas Utilizadas], [Total Licencas], 0)
```

```dax
Status Compliance Licencas = 
VAR Taxa = [Taxa Utilizacao Licencas]
RETURN
SWITCH(
    TRUE(),
    Taxa > 1, "❌ RISCO COMPLIANCE",
    Taxa < 0.5, "⚠️ SUBUTILIZAÇÃO",
    "✅ OK"
)
```

```dax
Investimento Licencas = SUM(Licencas[Valor_Total])
```

```dax
Custo Médio por Licença = 
DIVIDE([Investimento Licencas], [Total Licencas], 0)
```

### Medidas de Manutenção

```dax
Total Manutencoes = COUNTROWS(Manutencao)
```

```dax
Custo Total Manutencao = SUM(Manutencao[Custo])
```

```dax
Custo Médio Manutencao = 
DIVIDE([Custo Total Manutencao], [Total Manutencoes], 0)
```

```dax
Tempo Médio Parada = AVERAGE(Manutencao[Tempo_Parada_Horas])
```

```dax
Custo Manutencao por Ativo = 
DIVIDE([Custo Total Manutencao], [Total Ativos], 0)
```

### Medidas de Time Intelligence

```dax
Aquisições YTD = 
TOTALYTD([Total Ativos], Calendario[Date])
```

```dax
Aquisições Mês Anterior = 
CALCULATE(
    [Total Ativos],
    DATEADD(Calendario[Date], -1, MONTH)
)
```

```dax
Crescimento MoM = 
DIVIDE(
    [Total Ativos] - [Aquisições Mês Anterior],
    [Aquisições Mês Anterior],
    0
)
```

---

## 🎨 Guia de Design

### Paleta de Cores Recomendada

**Tema Corporativo Azul:**
- Primária: `#003366` (Azul escuro)
- Secundária: `#0066CC` (Azul médio)
- Destaque: `#FF6B35` (Laranja)
- Sucesso: `#28A745` (Verde)
- Alerta: `#FFC107` (Amarelo)
- Erro: `#DC3545` (Vermelho)
- Neutro: `#6C757D` (Cinza)

**Tema Tech Verde:**
- Primária: `#00A86B` (Verde jade)
- Secundária: `#00CED1` (Turquesa)
- Destaque: `#FF6F61` (Coral)

### Fontes

- **Títulos:** Segoe UI Semibold, 16-20pt
- **Subtítulos:** Segoe UI, 12-14pt
- **Corpo:** Segoe UI, 10-11pt
- **KPIs:** Segoe UI Bold, 32-48pt

### Espaçamento

- Margem externa: 20px
- Entre seções: 15px
- Entre elementos: 10px
- Altura do cabeçalho: 80px

---

## 🚀 Como Criar o Dashboard

### Passo 1: Preparar o Ambiente

1. **Instale o Power BI Desktop:**
   - Download: https://powerbi.microsoft.com/desktop/
   - Versão recomendada: Mais recente

2. **Baixe os dados de exemplo:**
   - Navegue até `dados-exemplo/`
   - Arquivos necessários:
     - hardware-sample.csv
     - licencas-sample.csv
     - manutencao-sample.csv

### Passo 2: Importar Dados

1. Abra Power BI Desktop
2. **Obter Dados** → **Texto/CSV**
3. Selecione cada arquivo CSV
4. Clique em **Transformar Dados**
5. No Power Query:
   - Verifique tipos de dados
   - Remova colunas vazias
   - Renomeie tabelas (Hardware, Licencas, Manutencao)
6. **Fechar e Aplicar**

### Passo 3: Criar Modelo de Dados

1. Vá para visualização **Modelo**
2. Crie relacionamentos:
   ```
   Hardware[ID_Ativo] ← Manutencao[ID_Ativo]
   ```
3. Configure cardinalidade: 1:N (Um para Muitos)
4. Direção do filtro: Ambas

### Passo 4: Criar Tabela de Calendário

```dax
Calendario = 
ADDCOLUMNS(
    CALENDAR(DATE(2020,1,1), DATE(2026,12,31)),
    "Ano", YEAR([Date]),
    "Mês", MONTH([Date]),
    "MesNome", FORMAT([Date], "MMMM"),
    "MesAno", FORMAT([Date], "MMM/YY"),
    "Trimestre", "T" & QUARTER([Date])
)
```

Relacione: `Calendario[Date]` ← `Hardware[Data_Aquisicao]`

### Passo 5: Criar Medidas

Copie e cole todas as medidas DAX listadas na seção "Medidas DAX Essenciais"

### Passo 6: Construir Páginas

Siga a estrutura descrita em "Estrutura do Dashboard" para cada página.

### Passo 7: Aplicar Tema

1. **Exibir** → **Temas** → Escolha um tema
2. Ou personalize em **Personalizar tema atual**
3. Salve o tema para consistência

### Passo 8: Adicionar Navegação

1. Insira **Botões** no topo
2. Configure **Ação** → **Navegação de página**
3. Estilize para parecer uma barra de menu

### Passo 9: Testar Interatividade

1. Clique nos filtros - verifique se atualiza
2. Teste drill-through
3. Valide cálculos das medidas

### Passo 10: Salvar e Compartilhar

1. **Arquivo** → **Salvar como**
2. Nome: `Dashboard-Inventario-TI.pbix`
3. Opcional: Publicar no Power BI Service

---

## 📝 Checklist de Qualidade

Antes de considerar o dashboard completo, verifique:

### Dados
- [ ] Todos os dados importados corretamente
- [ ] Relacionamentos funcionando
- [ ] Sem erros nas medidas DAX
- [ ] Formatos corretos (data, moeda, número)

### Visual
- [ ] Paleta de cores consistente
- [ ] Fontes padronizadas
- [ ] Logo/identidade visual aplicada
- [ ] Layout organizado e alinhado
- [ ] Títulos descritivos e claros

### Funcional
- [ ] Filtros aplicando corretamente
- [ ] Cross-filtering entre visuais
- [ ] Navegação entre páginas funcional
- [ ] Drill-through configurado
- [ ] Tooltips informativos

### Conteúdo
- [ ] Todos os KPIs implementados
- [ ] Visualizações apropriadas aos dados
- [ ] Insights claramente comunicados
- [ ] Sem dados de teste visíveis

---

## 💡 Dicas e Melhores Práticas

### Performance

1. **Evite medidas complexas em tabelas grandes**
   - Use colunas calculadas quando possível
   - Prefira DirectQuery para dados enormes

2. **Otimize relacionamentos**
   - Use chaves inteiras quando possível
   - Evite relacionamentos muitos-para-muitos

3. **Limite linhas visíveis**
   - Use filtros de contexto
   - Top N em tabelas

### Usabilidade

1. **Menos é mais**
   - Máximo 7 visuais por página
   - Foco em informações chave

2. **Use hierarquias**
   - Permita drill-down natural
   - Ex: Ano → Trimestre → Mês

3. **Tooltips personalizados**
   - Crie páginas de tooltip
   - Adicione contexto adicional

### Manutenção

1. **Documente suas medidas**
   - Adicione descrições no DAX
   - Mantenha lista atualizada

2. **Versionamento**
   - Salve versões incrementais
   - Use controle de versão (Git + .pbix)

3. **Atualização de dados**
   - Configure refresh automático (Service)
   - Ou agende manual (Desktop)

---

## 📚 Recursos de Aprendizado

### Documentação Oficial
- [Power BI Docs](https://docs.microsoft.com/power-bi/)
- [DAX Reference](https://dax.guide/)
- [Power BI Community](https://community.powerbi.com/)

### Cursos Recomendados
- Microsoft Learn: Power BI
- Udemy: "Power BI A-Z"
- Coursera: "Data Visualization with Power BI"

### Livros
- "The Definitive Guide to DAX" - Alberto Ferrari & Marco Russo
- "Storytelling with Data" - Cole Nussbaumer Knaflic

### Canais YouTube
- Guy in a Cube
- SQLBI (Marco Russo)
- Curbal

---

## 🆘 Troubleshooting

### Erro: "Não é possível criar relacionamento"
**Solução:** Verifique se as colunas têm o mesmo tipo de dado

### Erro: "A medida não calcula corretamente"
**Solução:** Verifique contexto de filtro com CALCULATE()

### Erro: "Dashboard lento"
**Solução:** Reduza granularidade dos dados, use agregações

### Problema: "Filtros não funcionam"
**Solução:** Verifique direção do relacionamento (bi-direcional se necessário)

---

## 📧 Suporte

Dúvidas ou problemas?
- Abra uma [Issue no GitHub](https://github.com/GUIPETAV/inventario-parque-tecnologico/issues)
- Consulte a [documentação completa](../docs/)
- Participe da comunidade Power BI

---

**Última atualização:** Janeiro 2026  
**Versão:** 1.0  
**Autor:** GUIPETAV
