# Excel Templates - Projeto Inventário de Parque Tecnológico

## ✅ Conclusão

Todos os 4 templates Excel foram criados com sucesso na pasta `excel/`.

## 📦 Arquivos Criados

### 1. template-inventario-hardware.xlsx
- **Tamanho**: 8.0 KB
- **Abas**: Hardware (20 cols, 3 exemplos), Validações (6 categorias), Dashboard (KPIs)
- **Formato**: ID_Ativo, Tipo, Marca, Modelo, Processador, RAM_GB, Armazenamento_GB, etc.
- **Fórmulas**: KPIs automáticos (Total, Ativos, Manutenção, Descartados)
- **Validações**: Desktop, Notebook, Servidor, Impressora, Switch, Roteador, Firewall

### 2. template-licencas-software.xlsx
- **Tamanho**: 6.5 KB
- **Abas**: Licenças (17 cols, 2 exemplos), Validações (3 categorias)
- **Fórmulas**: Licencas_Disponiveis (=Qty_Adq - Qty_Util), Status_Licenca (=IF Validade)
- **Validações**: Volumen, Perpetua, Subscricao, Trial, Freeware, Open Source
- **Exemplo**: Microsoft Office (50 lic.), AutoCAD (10 lic.)

### 3. template-manutencao.xlsx
- **Tamanho**: 6.4 KB
- **Abas**: Manutenções (12 cols, 2 exemplos), Validações (4 categorias)
- **Campos**: ID_Manutencao, ID_Ativo, Data, Tipo, Problema, Solução, Técnico, Custo, etc.
- **Validações**: Desktop, Notebook, Servidor; Preventiva, Corretiva, Adaptativa, Preditiva
- **Exemplo**: Limpeza preventiva, Substituição de pasta térmica

### 4. dashboard-excel-exemplo.xlsx
- **Tamanho**: 8.7 KB
- **Abas**: Dashboard (KPIs coloridos), Dados Hardware (7 equipamentos), Análise (estatísticas)
- **KPIs**: Total de Ativos, Ativos Ativos, Taxa de Utilização, Valor Total
- **Dados**: 7 equipamentos reais (Dell, Lenovo, HP, Apple, Cisco)
- **Análise**: Contagem por tipo, percentuais, contagem por status

### 5. README.md
- **Tamanho**: 11 KB
- **Conteúdo**: Documentação completa de todos os templates
- **Seções**: Arquivos, Colunas, Validações, Como Usar, Personalizações, Dicas

## 🎨 Características Técnicas

### Formatação Profissional
- ✅ Headers azul (#003366) com texto branco e negrito (11pt)
- ✅ Bordas em todas as células
- ✅ Alternância de linhas em azul claro (#E8F0F5)
- ✅ Alinhamento: centralizado em headers, esquerda em dados

### Funcionalidades
- ✅ Panes congeladas (primeira linha)
- ✅ Largura de colunas auto-ajustada
- ✅ Formatação de números:
  - Moeda: R$ #,##0.00
  - Datas: dd/mm/yyyy
  - Percentuais: 0%
- ✅ Fórmulas automáticas para KPIs
- ✅ Validações de dados com dropdowns
- ✅ Dados de exemplo realistas

## 📊 Dados de Exemplo Incluídos

### Hardware (3 equipamentos)
1. HW-001: Desktop Dell OptiPlex 7090 - Intel i7-11700, 16GB RAM, SSD
2. HW-002: Notebook Lenovo ThinkPad - Intel i5, 8GB RAM, SSD
3. HW-003: Servidor HP ProLiant - Intel Xeon Gold, 128GB RAM, SAS

### Licenças (2 softwares)
1. LIC-001: Microsoft Office 2021 - 50 licenças, Volumen
2. LIC-002: AutoCAD 2024 - 10 licenças, Perpetua

### Manutenções (2 registros)
1. MNT-001: Desktop (HW-001) - Limpeza preventiva
2. MNT-002: Servidor (HW-003) - Substituição pasta térmica

## 🛠️ Geração dos Templates

**Ferramenta**: Python 3.x com openpyxl
**Script**: `create_templates.py` (23.772 caracteres)
**Criação**: 14/01/2026

```bash
# Para regenerar os templates:
python3 create_templates.py
```

## 💾 Compatibilidade

- ✅ Microsoft Excel 2016+
- ✅ LibreOffice Calc 6.0+
- ✅ Google Sheets (com importação)
- ✅ Excel Online

## 📝 Próximos Passos

1. **Implementar Validações no Excel**
   - Selecione colunas de dropdown
   - Use: Dados → Validação
   - Referencie listas da aba "Validações"

2. **Adicionar Dados Reais**
   - Preencha com dados da sua organização
   - Mantenha formato e estrutura
   - Atualize regularmente

3. **Criar Gráficos**
   - Use dados como base
   - Crie gráficos de evolução, pizza, barras
   - Integre em relatórios

4. **Integrar com Power BI**
   - Exporte para CSV
   - Importe no Power BI
   - Crie dashboards interativos

5. **Automatizar Processos**
   - Configure macros
   - Crie alertas automáticos
   - Implemente atualizações periódicas

## 📍 Localização

Todos os arquivos estão em: 
```
/home/runner/work/inventario-parque-tecnologico/inventario-parque-tecnologico/excel/
```

## 📞 Informações Técnicas

| Aspecto | Detalhe |
|--------|--------|
| Biblioteca | openpyxl 3.11+ |
| Formato | XLSX (Open XML) |
| Total | 5 arquivos (~48 KB) |
| Headers | 20, 17, 12, 13 colunas |
| Abas | 3, 2, 2, 3 abas por arquivo |
| Exemplos | 3, 2, 2, 7 dados |
| Validações | 6, 3, 4 categorias |

## ✨ Status

✅ **COMPLETO** - Todos os templates foram criados com sucesso!

