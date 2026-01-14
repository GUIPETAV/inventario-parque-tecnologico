# 📋 Plano de Aula - Inventário de Parque Tecnológico

## 📌 Informações Gerais

**Duração Total:** 4-5 horas (pode ser dividido em múltiplas sessões)  
**Público-Alvo:** Profissionais de TI, analistas de infraestrutura, gestores de TI  
**Nível:** Intermediário  
**Pré-requisitos:** 
- Conhecimento básico de Excel
- Familiaridade com conceitos de TI
- Desejável: noções de PowerShell e Python

---

## 🎯 Objetivos de Aprendizagem

Ao final desta aula, o aluno será capaz de:

1. Compreender os conceitos fundamentais de ITAM (IT Asset Management)
2. Criar e gerenciar inventários de hardware e software no Excel
3. Implementar controles de licenças e compliance
4. Automatizar coleta de dados com scripts
5. Construir dashboards executivos no Power BI
6. Aplicar análises de custos e otimização de recursos

---

## 📚 Módulo 1: Fundamentos de ITAM (30 min)

### 1.1 O que é Gestão de Ativos de TI (10 min)

**Conceitos-chave:**
- Definição de ITAM (IT Asset Management)
- Importância para a organização
- Benefícios: redução de custos, compliance, segurança
- Diferença entre inventário e gestão de ativos

**Atividade:**
- Discussão: Quais são os principais desafios de inventário na sua organização?

### 1.2 Tipos de Ativos (10 min)

**Hardware:**
- Desktops, notebooks, servidores
- Dispositivos móveis (tablets, smartphones)
- Equipamentos de rede (switches, roteadores, firewalls)
- Periféricos (impressoras, monitores, etc.)

**Software:**
- Sistemas operacionais
- Aplicações corporativas
- Ferramentas de produtividade
- Licenças e subscrições

**Outros Ativos:**
- Infraestrutura (racks, cabeamento)
- Contratos de suporte e manutenção
- Documentação técnica

### 1.3 Ciclo de Vida dos Ativos (10 min)

**Fases:**
1. **Planejamento:** Identificação de necessidades
2. **Aquisição:** Compra e procurement
3. **Implantação:** Configuração e entrega
4. **Operação:** Uso diário e suporte
5. **Manutenção:** Reparos e upgrades
6. **Descarte:** Fim de vida útil e disposal

**Métricas Importantes:**
- **TCO (Total Cost of Ownership):** Custo total de propriedade
- **ROI (Return on Investment):** Retorno sobre investimento
- **Depreciação:** Perda de valor ao longo do tempo
- **MTBF (Mean Time Between Failures):** Tempo médio entre falhas
- **MTTR (Mean Time To Repair):** Tempo médio de reparo

---

## 💻 Módulo 2: Excel para Inventário de TI (60 min)

### 2.1 Estruturação de Dados (20 min)

#### Tabela de Hardware (Campos Essenciais)

**Campos Obrigatórios:**
- ID_Ativo (único)
- Tipo (Desktop, Notebook, Servidor, etc.)
- Marca e Modelo
- Número de Série
- Data de Aquisição
- Status (Ativo, Inativo, Manutenção)
- Localização
- Departamento

**Campos Importantes:**
- Especificações técnicas (CPU, RAM, Storage)
- Sistema Operacional
- Valor de Aquisição
- Garantia (início e fim)
- Usuário responsável

**Demonstração Prática:**
- Abrir `excel/template-inventario-hardware.xlsx`
- Explicar cada campo e sua importância
- Mostrar validação de dados (listas suspensas)
- Inserir 3-5 registros de exemplo

#### Tabela de Software/Licenças

**Campos Essenciais:**
- ID_Licença
- Software e Versão
- Tipo de Licença (Perpétua, Subscrição, OEM)
- Quantidade Adquirida vs Utilizada
- Data de Validade
- Valor
- Chave/Serial

**Demonstração:**
- Abrir `excel/template-licencas-software.xlsx`
- Explicar controle de licenças disponíveis
- Mostrar alertas de vencimento

#### Relacionamentos entre Tabelas

**Conceito:**
- Como vincular hardware e software
- Tabela de instalações (muitos para muitos)
- Histórico de manutenções por ativo

### 2.2 Fórmulas e Automações (20 min)

#### Cálculo de Idade dos Equipamentos

```excel
=SE([@Data_Aquisicao]="";"";DATEDIF([@Data_Aquisicao];HOJE();"Y"))
```

**Explicação:**
- DATEDIF calcula diferença entre datas
- "Y" retorna anos completos
- SE trata células vazias

#### Alertas de Garantia Vencendo

```excel
=SE(E([@Garantia_Fim]>=HOJE();[@Garantia_Fim]<=HOJE()+90);"VENCENDO EM "&DIAS([@Garantia_Fim];HOJE())&" DIAS";"")
```

**Aplicação:**
- Identificar garantias vencendo em 90 dias
- Criar alertas visuais com formatação condicional

#### Análise de Custos por Departamento

```excel
=SOMASE(Tabela[Departamento];"TI";Tabela[Valor_Aquisicao])
```

**Uso:**
- Calcular investimento por área
- Identificar departamentos com maior custo

#### Formatação Condicional

**Exemplos:**
- Status de garantia: Verde (OK), Amarelo (Vencendo), Vermelho (Vencida)
- Idade do equipamento: Vermelho se > 5 anos
- Status do ativo: Cores diferentes por situação

**Exercício Prático:**
- Alunos aplicam fórmulas no template
- Criam formatação condicional personalizada
- Testam com dados de exemplo

### 2.3 Dashboard no Excel (20 min)

#### Componentes do Dashboard

**KPIs Principais:**
- Total de Ativos
- Valor Total do Parque
- Garantias Vencendo (30/60/90 dias)
- Equipamentos em Manutenção

**Gráficos Recomendados:**
1. **Gráfico de Pizza:** Distribuição por tipo de equipamento
2. **Gráfico de Barras:** Ativos por departamento
3. **Gráfico de Linha:** Evolução de aquisições ao longo do tempo
4. **Tabela Dinâmica:** Valor total por categoria

**Demonstração:**
- Abrir `excel/dashboard-excel-exemplo.xlsx`
- Explicar cada visualização
- Mostrar interatividade com filtros

**Exercício:**
- Criar um gráfico de pizza mostrando distribuição de RAM (4GB, 8GB, 16GB, etc.)
- Adicionar um indicador de idade média dos equipamentos

---

## 📊 Módulo 3: Power BI para Gestão de Ativos (90 min)

### 3.1 Importação e Modelagem (30 min)

#### Conectar Dados do Excel/CSV

**Passo a Passo:**
1. Abrir Power BI Desktop
2. Obter Dados → CSV/Excel
3. Selecionar arquivos: hardware-sample.csv, licencas-sample.csv, manutencao-sample.csv
4. Transformar dados (Power Query)
   - Remover colunas desnecessárias
   - Alterar tipos de dados
   - Tratar valores nulos

#### Criar Relacionamentos

**Modelo de Dados:**
```
Hardware (1) ----< (*) Manutenção
  ↓ ID_Ativo          ↓ ID_Ativo

Licenças (1) ----< (*) Instalações
  ↓ ID_Licença        ↓ ID_Licença
                      ↓ ID_Ativo
```

**Configuração:**
- Relacionamento 1:N entre Hardware e Manutenção
- Chave: ID_Ativo
- Cardinalidade e direção do filtro

#### Medidas DAX Essenciais

```dax
// Total de Ativos
Total Ativos = COUNTROWS(Hardware)

// Ativos Ativos
Ativos Ativos = CALCULATE(COUNTROWS(Hardware), Hardware[Status] = "Ativo")

// Valor Total do Parque
Valor Total = SUM(Hardware[Valor_Aquisicao])

// Garantias Vencendo em 30 dias
Garantias Vencendo 30d = 
CALCULATE(
    COUNTROWS(Hardware),
    Hardware[Garantia_Fim] >= TODAY(),
    Hardware[Garantia_Fim] <= TODAY() + 30
)

// Idade Média dos Equipamentos
Idade Média = AVERAGE(Hardware[Idade_Anos])

// Taxa de Utilização de Licenças
Taxa Utilização Licenças = 
DIVIDE(
    SUM(Licencas[Quantidade_Utilizada]),
    SUM(Licencas[Quantidade_Adquirida]),
    0
) * 100
```

**Demonstração:**
- Criar cada medida no Power BI
- Explicar sintaxe DAX
- Testar medidas em cartões

### 3.2 Dashboard Executivo (40 min)

#### Página 1: Visão Geral

**Layout:**
- Cabeçalho com logo e título
- 4 cartões KPI no topo
- 2 gráficos principais no meio
- 1 tabela detalhada na parte inferior

**Visualizações:**

1. **Cartões KPI:**
   - Total de Ativos
   - Valor Total do Parque (R$)
   - % Ativos Ativos
   - Garantias Vencendo

2. **Gráfico de Barras Clusterizado:**
   - Eixo: Tipo de Ativo
   - Valores: Contagem de Ativos
   - Título: "Distribuição por Tipo de Equipamento"

3. **Gráfico de Pizza:**
   - Legenda: Departamento
   - Valores: Contagem de Ativos
   - Título: "Distribuição por Departamento"

4. **Gráfico de Área:**
   - Eixo: Data_Aquisicao (mês/ano)
   - Valores: Contagem de Ativos
   - Título: "Evolução de Aquisições"

5. **Tabela:**
   - Colunas: Tipo, Marca, Modelo, Valor, Departamento
   - Ordenação: Valor (decrescente)
   - Título: "Top 10 Ativos por Valor"

#### Página 2: Análise de Hardware

**Visualizações Específicas:**
- Matriz: Configuração (RAM x Processador)
- Gráfico de Barras: Idade dos equipamentos (por faixa)
- Gráfico de Rosca: Status de Garantia
- Tabela: Alertas de garantia vencendo

#### Página 3: Gestão de Licenças

**Visualizações:**
- Cartão: Total de Licenças
- Cartão: Taxa de Utilização Média
- Gráfico de Barras: Licenças por Software (Top 10)
- Gráfico de Dispersão: Quantidade Adquirida x Utilizada
- Tabela: Licenças vencendo em 90 dias

#### Drill-down e Filtros

**Segmentadores (Slicers):**
- Departamento
- Tipo de Ativo
- Status
- Ano de Aquisição

**Interatividade:**
- Drill-through de tabela para detalhes
- Filtros cruzados entre visuais
- Tooltips personalizados

**Exercício Prático:**
- Alunos criam Página 1 completa
- Aplicam tema corporativo
- Configuram interações

### 3.3 Publicação e Compartilhamento (20 min)

**Opções:**
1. Salvar como arquivo .pbix
2. Publicar no Power BI Service (requer licença)
3. Exportar para PDF
4. Exportar para PowerPoint

**Boas Práticas:**
- Documentar medidas DAX
- Usar nomes descritivos
- Aplicar tema consistente
- Testar em diferentes resoluções

---

## ⚙️ Módulo 4: Automação com Scripts (45 min)

### 4.1 PowerShell para Coleta de Dados (25 min)

#### Script 1: Coleta de Inventário de Hardware

**Conceitos:**
- WMI (Windows Management Instrumentation)
- Cmdlets do PowerShell
- Exportação para CSV

**Demonstração:**
```powershell
.\scripts\powershell\coletar-inventario-hardware.ps1
```

**O que o script faz:**
1. Coleta informações do sistema (fabricante, modelo, serial)
2. Obtém dados do processador
3. Calcula memória RAM total
4. Lista discos e capacidade
5. Identifica sistema operacional
6. Exporta para CSV

**Análise do Código:**
- Get-ComputerInfo
- Get-WmiObject
- Criação de PSCustomObject
- Export-Csv

#### Script 2: Coleta de Software Instalado

**Demonstração:**
```powershell
.\scripts\powershell\coletar-software-instalado.ps1
```

**Funcionalidade:**
- Lê registro do Windows (32 e 64 bits)
- Lista programas instalados
- Remove duplicatas
- Exporta lista completa

**Uso Prático:**
- Auditorias de software
- Identificação de licenças necessárias
- Detecção de software não autorizado

### 4.2 Python para Análise (20 min)

#### Script de Análise de Inventário

**Bibliotecas Utilizadas:**
- pandas: Manipulação de dados
- numpy: Cálculos numéricos
- datetime: Trabalho com datas

**Demonstração:**
```bash
python scripts/python/analisar-inventario.py
```

**Análises Realizadas:**
1. Estatísticas gerais (total, média, etc.)
2. Distribuição por tipo/departamento
3. Análise de idade dos equipamentos
4. Alertas de garantia
5. Análise de configuração (RAM, CPU)
6. Cálculo de valor total do parque

**Análise de Licenças:**
- Taxa de utilização
- Identificação de subutilização (<50%)
- Detecção de uso excessivo (risco compliance)
- Alertas de vencimento

**Exercício:**
- Alunos executam o script
- Interpretam os resultados
- Identificam insights acionáveis

### 4.3 Integração com Excel

**Fluxo Completo:**
1. PowerShell coleta dados → CSV
2. Python analisa dados → Relatório
3. Excel/Power BI visualiza → Dashboard

**Automação:**
- Agendamento com Task Scheduler
- Executar diariamente/semanalmente
- Atualizar automaticamente dashboards

---

## 🎯 Módulo 5: Caso Prático (60 min)

### 5.1 Cenário Real (10 min)

**Contexto:**
Você é o novo analista de infraestrutura de uma empresa de 200 funcionários. A empresa nunca teve um inventário organizado. Seu desafio é:

1. Organizar o inventário de hardware existente
2. Controlar licenças de software
3. Identificar equipamentos para renovação
4. Criar dashboard para apresentação à diretoria

**Dados Fornecidos:**
- hardware-sample.csv (50 equipamentos)
- licencas-sample.csv (30 licenças)
- manutencao-sample.csv (histórico)

### 5.2 Exercício Completo (40 min)

#### Tarefa 1: Análise Exploratória (10 min)

**Atividades:**
1. Carregar dados no Excel
2. Identificar dados faltantes
3. Calcular estatísticas básicas:
   - Total de ativos
   - Valor total investido
   - Idade média dos equipamentos
   - Distribuição por tipo/departamento

#### Tarefa 2: Análise de Garantias (10 min)

**Atividades:**
1. Identificar equipamentos com garantia:
   - Vencida
   - Vencendo em 30 dias
   - Vencendo em 90 dias
2. Criar lista priorizada para renovação
3. Estimar custos de renovação/substituição

**Entregável:**
Planilha Excel com recomendações

#### Tarefa 3: Análise de Licenças (10 min)

**Atividades:**
1. Calcular taxa de utilização por software
2. Identificar licenças subutilizadas
3. Detectar uso excessivo (risco compliance)
4. Criar plano de otimização

**Entregável:**
Relatório com recomendações de compra/redução

#### Tarefa 4: Dashboard Executivo (10 min)

**Atividades:**
1. Criar dashboard no Power BI ou Excel
2. Incluir KPIs principais
3. Adicionar visualizações relevantes
4. Preparar narrativa para apresentação

**Entregável:**
Dashboard pronto para apresentação

### 5.3 Apresentação e Discussão (10 min)

**Atividades:**
- Alunos apresentam seus dashboards (2-3 min cada)
- Discussão de insights encontrados
- Feedback do instrutor
- Melhores práticas identificadas

---

## 📝 Avaliação e Certificação

### Critérios de Avaliação

**Conhecimento Teórico (30%):**
- Compreensão de conceitos ITAM
- Conhecimento de métricas e KPIs
- Entendimento do ciclo de vida

**Habilidades Técnicas (40%):**
- Uso correto de fórmulas Excel
- Criação de visualizações efetivas
- Execução de scripts

**Aplicação Prática (30%):**
- Qualidade das análises
- Insights acionáveis
- Apresentação profissional

### Certificado de Conclusão

Será emitido aos alunos que:
- Comparecerem a pelo menos 80% da aula
- Completarem todos os exercícios práticos
- Apresentarem o caso prático final

---

## 📚 Recursos Adicionais

### Leitura Recomendada

- ISO 19770 - IT Asset Management
- ITIL v4 - Service Asset and Configuration Management
- Microsoft Documentation - PowerShell e Power BI
- Gartner Research - ITAM Best Practices

### Ferramentas Complementares

- **Inventário:**
  - GLPI
  - Snipe-IT
  - Lansweeper

- **Licenciamento:**
  - Flexera
  - Snow License Manager

### Comunidades

- r/sysadmin
- r/PowerShell
- Power BI Community
- TechNet Forums

---

## 🎓 Próximos Passos

Após concluir este curso, os alunos podem:

1. **Implementar ITAM na sua organização:**
   - Adaptar templates às necessidades
   - Automatizar coleta de dados
   - Criar processos de atualização

2. **Aprofundar conhecimentos:**
   - Certificação ITIL
   - Cursos avançados de Power BI
   - Scripting avançado (PowerShell, Python)

3. **Explorar ferramentas profissionais:**
   - Sistemas CMDB
   - Ferramentas de ITSM
   - Plataformas de gestão de licenças

---

## 📞 Suporte ao Aluno

- **Dúvidas durante a aula:** Interrompa e pergunte
- **Suporte pós-aula:** Abra issues no GitHub
- **Material adicional:** Consulte a pasta `docs/`
- **Comunidade:** Participe das discussões

---

**Última atualização:** Janeiro 2026  
**Versão:** 1.0
