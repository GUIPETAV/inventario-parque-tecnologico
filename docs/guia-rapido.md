# 🚀 Guia Rápido - Inventário de Parque Tecnológico

Este guia fornece um caminho rápido para começar a usar os materiais de inventário de TI.

---

## ⏱️ Começando em 15 Minutos

### Passo 1: Instalar Pré-requisitos (5 min)

#### Ferramentas Necessárias

✅ **Microsoft Excel** (versão 2016 ou superior)
- Já instalado no Windows com Office
- Ou use Office 365 online

✅ **Power BI Desktop** (gratuito)
```
Download: https://powerbi.microsoft.com/desktop/
Tamanho: ~350 MB
Tempo de instalação: ~5 minutos
```

✅ **Python 3.8+** (opcional - apenas para scripts)
```
Download: https://www.python.org/downloads/
Marque: "Add Python to PATH" durante instalação
```

✅ **PowerShell** (já incluído no Windows)
- Versão mínima: 5.1
- Verificar versão: `$PSVersionTable.PSVersion`

### Passo 2: Baixar os Materiais (2 min)

```bash
# Clone o repositório
git clone https://github.com/GUIPETAV/inventario-parque-tecnologico.git

# Entre no diretório
cd inventario-parque-tecnologico
```

**Ou baixe o ZIP:**
- Acesse: https://github.com/GUIPETAV/inventario-parque-tecnologico
- Clique em "Code" → "Download ZIP"
- Extraia para uma pasta de sua preferência

### Passo 3: Configurar Python (3 min - opcional)

```bash
# Entre na pasta de scripts Python
cd scripts/python

# Instale as dependências
pip install -r requirements.txt
```

**Bibliotecas instaladas:**
- pandas (manipulação de dados)
- numpy (cálculos)
- openpyxl (leitura/escrita Excel)
- matplotlib (gráficos)
- seaborn (visualizações)

### Passo 4: Testar os Templates (5 min)

1. **Abra o Excel:**
   ```
   excel/template-inventario-hardware.xlsx
   ```

2. **Explore as abas:**
   - Hardware (tabela principal)
   - Validações (listas para dropdowns)
   - Dashboard (visualizações)

3. **Teste inserindo dados:**
   - Adicione 2-3 equipamentos
   - Veja as fórmulas calcularem automaticamente
   - Observe o dashboard atualizar

---

## 📋 Fluxo de Trabalho Básico

### Para Inventariar Hardware

#### Opção 1: Manual (Excel)

1. Abra `excel/template-inventario-hardware.xlsx`
2. Na aba "Hardware", preencha os campos:
   - ID_Ativo: HW001, HW002, etc.
   - Tipo: Selecione da lista suspensa
   - Marca/Modelo: Digite
   - Data_Aquisicao: Use formato de data
   - Valor_Aquisicao: Número com 2 decimais
3. As colunas calculadas (Idade, Status Garantia) preenchem automaticamente
4. Veja o dashboard atualizar

#### Opção 2: Automatizada (PowerShell)

```powershell
# Execute o script de coleta
cd scripts/powershell
.\coletar-inventario-hardware.ps1

# Arquivo criado: inventario_NOMEPC.csv
# Importe no Excel: Dados → Obter Dados → De Texto/CSV
```

### Para Controlar Licenças

1. Abra `excel/template-licencas-software.xlsx`
2. Na aba "Licenças", registre:
   - Software e versão
   - Quantidade adquirida
   - Quantidade utilizada
   - Data de validade
3. O Excel calcula automaticamente:
   - Licenças disponíveis
   - Status (Ativa, Vencendo, Vencida)
   - Alertas

### Para Analisar Dados

```bash
# Execute o script de análise
cd scripts/python
python analisar-inventario.py

# Resultado: Relatório completo no terminal
```

**O script analisa:**
- Total de ativos e distribuição
- Idade média dos equipamentos
- Alertas de garantia
- Taxa de utilização de licenças
- Valor total do parque

---

## 🎨 Criar Seu Primeiro Dashboard

### No Excel (10 minutos)

1. **Prepare os dados:**
   - Certifique-se de que seus dados estão em uma Tabela (Ctrl+T)
   - Dados devem ter cabeçalhos

2. **Insira um Gráfico de Pizza:**
   - Selecione: Inserir → Gráficos → Pizza
   - Dados: Tipo de equipamento
   - Personalize cores e título

3. **Adicione KPIs:**
   - Use células com fórmulas grandes e em negrito
   - Exemplo: `=CONT.VALORES(Tabela[ID_Ativo])`
   - Aplique formatação condicional

4. **Crie Tabela Dinâmica:**
   - Inserir → Tabela Dinâmica
   - Linhas: Departamento
   - Valores: Soma de Valor_Aquisicao

### No Power BI (20 minutos)

1. **Abra o Power BI Desktop**

2. **Importe Dados:**
   - Obter Dados → Texto/CSV
   - Selecione `dados-exemplo/hardware-sample.csv`
   - Clique em "Carregar"

3. **Crie Visualizações:**
   - **Cartão:** Arraste "ID_Ativo" para área de trabalho, escolha visual "Cartão"
   - **Gráfico de Barras:** Eixo = Tipo, Valores = Contagem de ID_Ativo
   - **Gráfico de Pizza:** Legenda = Departamento, Valores = Contagem

4. **Adicione Segmentadores:**
   - Visual "Segmentação de Dados"
   - Campo: Departamento ou Status

5. **Salve:**
   - Arquivo → Salvar como → meu-dashboard.pbix

---

## 💡 Casos de Uso Rápidos

### Caso 1: Identificar Garantias Vencendo

**No Excel:**
```
1. Abra template-inventario-hardware.xlsx
2. Vá para aba "Hardware"
3. Filtre coluna "Status_Garantia" = "Em Garantia"
4. Ordene por "Garantia_Fim" (crescente)
5. Primeiros resultados = vencendo primeiro
```

**Resultado:** Lista de equipamentos para renovar urgentemente

### Caso 2: Calcular Investimento por Departamento

**Fórmula Excel:**
```excel
=SOMASE(Hardware[Departamento];"Financeiro";Hardware[Valor_Aquisicao])
```

**No Power BI:**
```dax
Investimento TI = CALCULATE(SUM(Hardware[Valor_Aquisicao]), Hardware[Departamento] = "TI")
```

### Caso 3: Detectar Subutilização de Licenças

**No Excel:**
```
1. Abra template-licencas-software.xlsx
2. Adicione coluna "Taxa_Uso"
3. Fórmula: =[@Quantidade_Utilizada]/[@Quantidade_Adquirida]
4. Filtre < 0,5 (menos de 50%)
```

**Ação:** Considerar reduzir licenças na renovação

---

## 📊 Templates Disponíveis

### 📄 template-inventario-hardware.xlsx
**Use para:** Inventário completo de hardware
**Campos principais:** Tipo, Marca, Modelo, Serial, Data Aquisição, Garantia
**Fórmulas automáticas:** Idade, Status Garantia, Alertas

### 📄 template-licencas-software.xlsx
**Use para:** Controle de licenças e compliance
**Campos principais:** Software, Quantidade, Validade, Chave
**Fórmulas automáticas:** Licenças disponíveis, Status, Alertas de vencimento

### 📄 template-manutencao.xlsx
**Use para:** Histórico de manutenções
**Campos principais:** ID_Ativo, Data, Tipo, Problema, Solução, Custo
**Análises:** Custos por equipamento, tempo de parada

### 📄 dashboard-excel-exemplo.xlsx
**Use para:** Visualização executiva
**Contém:** Gráficos, KPIs, tabelas dinâmicas prontas
**Personalize:** Conecte aos seus dados

---

## 🔧 Scripts Prontos para Usar

### coletar-inventario-hardware.ps1
**O que faz:** Coleta dados do computador atual
**Como usar:**
```powershell
.\coletar-inventario-hardware.ps1
```
**Resultado:** arquivo CSV com especificações completas

### coletar-software-instalado.ps1
**O que faz:** Lista todos os programas instalados
**Como usar:**
```powershell
.\coletar-software-instalado.ps1
```
**Resultado:** Lista completa de software

### analisar-inventario.py
**O que faz:** Análise estatística completa
**Como usar:**
```bash
python analisar-inventario.py
```
**Resultado:** Relatório com insights e alertas

---

## 🎯 Próximos Passos

### Depois de dominar o básico:

1. **📚 Estude o Plano de Aula Completo**
   - Arquivo: `docs/plano-de-aula.md`
   - Conteúdo: Teoria e prática detalhada

2. **🏋️ Faça os Exercícios Práticos**
   - Pasta: `exercicios/`
   - 3 exercícios progressivos
   - Soluções comentadas

3. **📖 Leia Melhores Práticas**
   - Arquivo: `docs/melhores-praticas.md`
   - Padrões e recomendações ITAM

4. **🚀 Automatize Seu Inventário**
   - Configure coleta automática
   - Agende execução semanal
   - Integre com seu fluxo de trabalho

---

## ❓ Perguntas Frequentes

### "Preciso saber programar?"
**Não!** Os templates Excel funcionam sem programação. Scripts são opcionais para automação.

### "Os scripts funcionam no Mac/Linux?"
PowerShell funciona no Windows. Python é multiplataforma. Para Mac/Linux, use apenas os scripts Python.

### "Posso usar com LibreOffice?"
Excel é recomendado devido a fórmulas específicas. LibreOffice pode ter compatibilidade parcial.

### "Como adaptar para minha empresa?"
1. Edite as listas de validação (departamentos, locais, etc.)
2. Adicione/remova campos conforme necessário
3. Ajuste fórmulas se mudar estrutura

### "Onde encontro ajuda?"
- 📖 Documentação completa em `docs/`
- 💬 Abra uma issue no GitHub
- 📧 Consulte a comunidade

---

## 🔍 Troubleshooting

### Erro ao abrir Excel: "Arquivo corrompido"
**Solução:** Clique com botão direito → Propriedades → Desbloquear

### PowerShell: "Execução de scripts desabilitada"
**Solução:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Python: "Módulo não encontrado"
**Solução:**
```bash
pip install --upgrade -r requirements.txt
```

### Power BI: "Não consegue conectar aos dados"
**Solução:** Verifique o caminho do arquivo CSV. Use caminho completo se necessário.

---

## 📞 Recursos de Ajuda

| Recurso | Link |
|---------|------|
| Documentação Completa | `docs/plano-de-aula.md` |
| Melhores Práticas | `docs/melhores-praticas.md` |
| Exercícios Práticos | `exercicios/` |
| Power BI Instruções | `powerbi/README.md` |
| Issues GitHub | https://github.com/GUIPETAV/inventario-parque-tecnologico/issues |

---

## ✅ Checklist de Início

- [ ] Python instalado (opcional)
- [ ] Repositório baixado
- [ ] Dependências Python instaladas (opcional)
- [ ] Template Excel aberto e testado
- [ ] Dados de exemplo explorados
- [ ] Primeiro gráfico criado
- [ ] Script de coleta executado (opcional)
- [ ] Power BI instalado e testado (opcional)

**Parabéns! Você está pronto para começar! 🎉**

---

**Tempo total estimado:** 15-30 minutos  
**Última atualização:** Janeiro 2026
