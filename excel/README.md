# 📊 Templates Excel para Gestão de Inventário de Parque Tecnológico

Este diretório contém 4 templates profissionais em Excel para gerenciamento completo de inventário de TI, incluindo hardware, licenças de software e manutenções.

## 📋 Arquivos Disponíveis

### 1. **template-inventario-hardware.xlsx**
Template completo para gerenciamento de todos os equipamentos de hardware.

#### Abas:
- **Hardware** - Registro detalhado de todos os equipamentos
- **Validações** - Listas para preenchimento de dropdowns
- **Dashboard** - KPIs e instruções de uso

#### Colunas (Hardware):
| Coluna | Descrição | Formato |
|--------|-----------|---------|
| ID_Ativo | Identificador único | Texto (ex: HW-001) |
| Tipo | Tipo de equipamento | Dropdown (Desktop, Notebook, Servidor, etc.) |
| Marca | Fabricante | Texto |
| Modelo | Modelo do equipamento | Texto |
| Numero_Serie | Número de série | Texto |
| Processador | Processador instalado | Texto |
| RAM_GB | Memória RAM em GB | Número |
| Armazenamento_GB | Capacidade de armazenamento | Número |
| Tipo_Armazenamento | Tipo de armazenamento | Dropdown (SSD, HDD, NVMe, SAS) |
| Sistema_Operacional | Sistema operacional | Dropdown |
| Versao_SO | Versão do SO | Texto |
| Data_Aquisicao | Data de compra | Data (dd/mm/yyyy) |
| Valor_Aquisicao | Valor em Reais | Moeda (R$) |
| Garantia_Inicio | Início da garantia | Data (dd/mm/yyyy) |
| Garantia_Fim | Fim da garantia | Data (dd/mm/yyyy) |
| Localizacao | Localização física | Dropdown |
| Departamento | Departamento responsável | Dropdown |
| Usuario | Usuário atribuído | Texto |
| Status | Status do equipamento | Dropdown (Ativo, Inativo, Manutenção, Descartado) |
| Observacoes | Observações adicionais | Texto |

#### Validações disponíveis:
- **Tipos**: Desktop, Notebook, Servidor, Impressora, Switch, Roteador, Firewall
- **Status**: Ativo, Inativo, Manutenção, Descartado, Emprestado
- **Departamentos**: TI, RH, Financeiro, Gerência, Operações, Vendas, Administrativo
- **Localizações**: Sala TI, Data Center, Sala de Reuniões, Recepção, Administrativo
- **Tipos de Armazenamento**: SSD, HDD, NVMe, SAS, SATA
- **Sistemas Operacionais**: Windows 10, Windows 11, Ubuntu, CentOS, macOS, Linux

#### KPIs disponíveis (Dashboard):
- Total de Ativos
- Ativos Ativos
- Ativos em Manutenção
- Ativos Descartados

---

### 2. **template-licencas-software.xlsx**
Template para gerenciamento de licenças de software e compliance.

#### Abas:
- **Licenças** - Registro de todas as licenças
- **Validações** - Listas para dropdowns

#### Colunas (Licenças):
| Coluna | Descrição | Formato |
|--------|-----------|---------|
| ID_Licenca | Identificador único | Texto (ex: LIC-001) |
| Software | Nome do software | Texto |
| Versao | Versão da licença | Texto |
| Fabricante | Fabricante do software | Dropdown |
| Tipo_Licenca | Tipo de licença | Dropdown (Volumen, Perpetua, Subscricao, Trial) |
| Quantidade_Adquirida | Qty adquirida | Número |
| Quantidade_Utilizada | Qty em uso | Número |
| Licencas_Disponiveis | Qty disponível | **Fórmula**: =Quantidade_Adquirida - Quantidade_Utilizada |
| Chave_Serial | Chave de ativação | Texto |
| Data_Compra | Data de aquisição | Data (dd/mm/yyyy) |
| Data_Validade | Data de expiração | Data (dd/mm/yyyy) |
| Valor_Unitario | Preço unitário | Moeda (R$) |
| Valor_Total | Valor total | **Fórmula**: =Quantidade_Adquirida × Valor_Unitario |
| Status_Licenca | Status da licença | **Fórmula**: =IF(Data_Validade < HOJE(); "Expirada"; "Ativa") |
| Fornecedor | Fornecedor/Revenda | Texto |
| Nota_Fiscal | Número NF | Texto |
| Observacoes | Observações | Texto |

#### Fórmulas Automáticas:
- **Licencas_Disponiveis**: Calcula automaticamente licenças disponíveis
- **Status_Licenca**: Indica automaticamente se a licença está ativa ou expirada

#### Validações:
- **Tipos de Licença**: Volumen, Perpetua, Subscricao, Trial, Freeware, Open Source
- **Status**: Ativa, Expirada, Suspensa, Renovação Pendente
- **Fabricantes**: Microsoft, Autodesk, Adobe, JetBrains, VMware, Oracle

---

### 3. **template-manutencao.xlsx**
Template para registro e acompanhamento de manutenções.

#### Abas:
- **Manutenções** - Histórico de manutenções realizadas
- **Validações** - Listas para dropdowns

#### Colunas (Manutenções):
| Coluna | Descrição | Formato |
|--------|-----------|---------|
| ID_Manutencao | Identificador único | Texto (ex: MNT-001) |
| ID_Ativo | Equipamento relacionado | Texto (referência HW-XXX) |
| Tipo_Ativo | Tipo do equipamento | Dropdown |
| Data_Manutencao | Data da manutenção | Data (dd/mm/yyyy) |
| Tipo_Manutencao | Tipo de manutenção | Dropdown (Preventiva, Corretiva, Adaptativa, Preditiva) |
| Problema_Relatado | Descrição do problema | Texto |
| Solucao_Aplicada | Solução implementada | Texto |
| Tecnico_Responsavel | Técnico que realizou | Dropdown |
| Custo | Custo da manutenção | Moeda (R$) |
| Status | Status da manutenção | Dropdown (Pendente, Em Andamento, Concluído, Cancelado) |
| Tempo_Parada_Horas | Horas de parada | Número |
| Observacoes | Observações adicionais | Texto |

#### Validações:
- **Tipos de Ativo**: Desktop, Notebook, Servidor, Impressora, Switch, Roteador
- **Tipos de Manutenção**: Preventiva, Corretiva, Adaptativa, Preditiva
- **Status**: Pendente, Em Andamento, Concluído, Cancelado
- **Técnicos**: Técnico Carlos, Técnico Roberto, Técnico Ana, Técnico Paulo

---

### 4. **dashboard-excel-exemplo.xlsx**
Dashboard completo com exemplos de dados e visualizações.

#### Abas:
1. **Dashboard** - Visão geral com KPIs e indicadores visuais
2. **Dados Hardware** - 7 exemplos de equipamentos
3. **Análise** - Análises automáticas com gráficos e percentuais

#### Funcionalidades:
- **KPI Cards coloridos** com:
  - Total de Ativos
  - Ativos Ativos
  - Taxa de Utilização
  - Valor Total
- **Dados de exemplo** para 7 equipamentos
- **Análises automáticas** com:
  - Contagem por tipo de ativo
  - Percentuais calculados
  - Contagem por status
- **Formatação profissional** com cores e indicadores visuais

---

## 🎨 Características Técnicas Comuns

### Formatação
- ✓ **Headers profissionais**: Azul (#003366) com texto branco, negrito, tamanho 11pt
- ✓ **Bordas**: Todas as células de dados possuem bordas
- ✓ **Alternância de cores**: Linhas alternadas em azul claro (#E8F0F5) para legibilidade
- ✓ **Alinhamento**: Centralizado nos headers, alinhado à esquerda nos dados

### Funcionalidades
- ✓ **Panes congeladas**: Primeira linha (headers) congelada para fácil navegação
- ✓ **Largura de colunas**: Auto-ajustada para o conteúdo
- ✓ **Formatação de números**:
  - Moeda: R$ #,##0.00
  - Datas: dd/mm/yyyy
  - Percentuais: 0%
- ✓ **Fórmulas automáticas**: Cálculos para KPIs e métricas
- ✓ **Validação de dados**: Dropdowns com listas pré-definidas

### Dados de Exemplo
- ✓ **Realistas**: Exemplos baseados em cenários reais
- ✓ **Completos**: Todos os campos preenchidos
- ✓ **Consistentes**: Dados relacionados entre si

---

## 📝 Como Usar

### Preenchimento Básico
1. Abra o template desejado
2. Clique na aba correspondente (ex: "Hardware")
3. Comece a preencher dados a partir da linha 2 (linha 1 é header)
4. Use os dropdowns nas colunas com validações
5. As fórmulas calcularão automaticamente

### Usando Validações
1. Acesse a aba "Validações"
2. Veja as listas disponíveis por categoria
3. Nos campos correspondentes, use a validação de dados do Excel
4. Selecione valores da lista dropdown

### Acessando KPIs
1. Abra o template-inventario-hardware.xlsx
2. Acesse a aba "Dashboard"
3. Os KPIs são atualizados automaticamente com os dados
4. Use as fórmulas como base para seus próprios cálculos

### Criando Validações (Excel)
1. Selecione a coluna/célula que deseja validar
2. Vá para: Dados → Validação
3. Escolha "Lista"
4. Em "Fonte", referencie as células da aba "Validações"
5. Exemplo: =Validações!$A$2:$A$7

---

## 🔧 Personalizações Recomendadas

### Para template-inventario-hardware.xlsx
1. Altere os valores de exemplo
2. Adicione mais categorias na aba "Validações"
3. Implemente validações de dados nas colunas com dropdown
4. Crie gráficos baseados no Dashboard

### Para template-licencas-software.xlsx
1. Mantenha atualizada a Data_Validade para controle
2. Use o Status_Licenca como indicador de renovação
3. Analise Licencas_Disponiveis regularmente
4. Crie alertas para licenças próximas do vencimento

### Para template-manutencao.xlsx
1. Mantenha histórico completo
2. Use para análise de falhas
3. Calcule tempo médio de parada por tipo
4. Identifique equipamentos com muitas manutenções

### Para dashboard-excel-exemplo.xlsx
1. Replique o dashboard para seus dados reais
2. Aumente o número de equipamentos
3. Crie gráficos a partir dos dados
4. Implemente em Power BI para análises avançadas

---

## 📊 Dicas de Análise

### Inventário de Hardware
- Monitore equipamentos próximos do fim de garantia
- Identifique obsoletos para descarte
- Analise distribuição por departamento
- Compare investimentos por tipo de ativo

### Licenças de Software
- Acompanhe expiração de licenças
- Calcule ROI por software
- Controle conformidade
- Planeje renovações com antecedência

### Manutenções
- Identifique equipamentos com muitas falhas
- Calcule custo médio de manutenção
- Monitore tempo de parada por equipamento
- Analise efetividade de preventivas

---

## 🛠️ Requisitos

- **Microsoft Excel** 2016 ou superior
- ou **LibreOffice Calc** 6.0+
- ou **Google Sheets** (compatível com importação)

---

## 📞 Suporte

Estes templates foram criados com:
- **Biblioteca**: openpyxl (Python)
- **Formato**: .xlsx (Open XML Spreadsheet)
- **Versão**: 1.0

Para questões sobre uso ou personalização, consulte a documentação do seu software de planilha.

---

## 📅 Histórico

- **v1.0** - 14/01/2026
  - ✓ Criação de 4 templates profissionais
  - ✓ Exemplos realistas de dados
  - ✓ Formatação profissional
  - ✓ Fórmulas automáticas
  - ✓ Validações de dados

---

**Desenvolvido para**: Gestão de Inventário de Parque Tecnológico  
**Autor**: Sistema de Geração Automática  
**Licença**: Livre para uso interno
