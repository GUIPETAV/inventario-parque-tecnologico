# 🖥️ Inventário de Parque Tecnológico

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Excel](https://img.shields.io/badge/Excel-217346?logo=microsoft-excel&logoColor=white)](https://www.microsoft.com/excel)
[![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?logo=power-bi&logoColor=black)](https://powerbi.microsoft.com/)

> Material didático completo para ensinar gestão de inventário de ativos de TI usando Excel, Power BI e ferramentas de automação.

## 📖 Sobre o Projeto

Este repositório contém um conjunto completo de materiais educacionais para ensinar profissionais de TI a gerenciar o inventário de ativos tecnológicos de forma eficiente e profissional. O material foi desenvolvido para ser usado em aulas, workshops e treinamentos corporativos.

## 🎯 Objetivos de Aprendizagem

Ao final deste curso, o aluno será capaz de:

- ✅ Compreender os fundamentos de ITAM (IT Asset Management)
- ✅ Criar e gerenciar inventários de hardware usando Excel
- ✅ Controlar licenças de software e evitar problemas de compliance
- ✅ Automatizar a coleta de dados com PowerShell e Python
- ✅ Criar dashboards executivos no Power BI
- ✅ Implementar alertas de garantia e manutenção
- ✅ Realizar análises de custos e otimização de recursos

## 📁 Estrutura do Repositório

```
inventario-parque-tecnologico/
├── 📄 README.md                          # Este arquivo
├── 📂 docs/                              # Documentação do curso
│   ├── plano-de-aula.md                 # Plano de aula completo
│   ├── guia-rapido.md                   # Guia de início rápido
│   └── melhores-praticas.md             # Boas práticas de ITAM
├── 📂 excel/                             # Templates Excel
│   ├── template-inventario-hardware.xlsx
│   ├── template-licencas-software.xlsx
│   ├── template-manutencao.xlsx
│   └── dashboard-excel-exemplo.xlsx
├── 📂 powerbi/                           # Materiais Power BI
│   ├── README.md                        # Instruções do dashboard
│   └── modelo-dashboard.txt             # Descrição do modelo
├── 📂 scripts/                           # Scripts de automação
│   ├── powershell/                      # Scripts PowerShell
│   │   ├── coletar-inventario-hardware.ps1
│   │   ├── coletar-software-instalado.ps1
│   │   └── exportar-para-excel.ps1
│   └── python/                          # Scripts Python
│       ├── analisar-inventario.py
│       ├── gerar-relatorio.py
│       └── requirements.txt
├── 📂 dados-exemplo/                     # Dados de exemplo
│   ├── hardware-sample.csv
│   ├── software-sample.csv
│   ├── licencas-sample.csv
│   └── manutencao-sample.csv
└── 📂 exercicios/                        # Exercícios práticos
    ├── exercicio-01-analise-abc.md
    ├── exercicio-02-garantias.md
    └── exercicio-03-dashboard.md
```

## 🚀 Início Rápido

### Pré-requisitos

- 💻 Microsoft Excel 2016 ou superior (ou Office 365)
- 📊 Power BI Desktop (download gratuito)
- 🐍 Python 3.8+ (para scripts de análise)
- ⚡ PowerShell 5.1+ (já incluído no Windows)

### Instalação

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/GUIPETAV/inventario-parque-tecnologico.git
   cd inventario-parque-tecnologico
   ```

2. **Instale as dependências Python:**
   ```bash
   cd scripts/python
   pip install -r requirements.txt
   ```

3. **Abra os templates Excel:**
   - Navegue até a pasta `excel/`
   - Abra os templates no Microsoft Excel
   - Habilite macros se solicitado

4. **Configure o Power BI:**
   - Instale o [Power BI Desktop](https://powerbi.microsoft.com/desktop/)
   - Siga as instruções em `powerbi/README.md`

## 📚 Módulos do Curso

### Módulo 1: Fundamentos de ITAM (30 min)
Introdução aos conceitos de gestão de ativos de TI, tipos de ativos, ciclo de vida e métricas importantes.

**Material:** `docs/plano-de-aula.md` - Seção 1

### Módulo 2: Excel para Inventário (60 min)
Aprenda a criar e gerenciar inventários de hardware, software e licenças usando Excel com fórmulas avançadas e automações.

**Material:** 
- `excel/template-inventario-hardware.xlsx`
- `excel/template-licencas-software.xlsx`
- `excel/template-manutencao.xlsx`

### Módulo 3: Power BI para Dashboards (90 min)
Construa dashboards executivos interativos para visualizar e analisar o parque tecnológico.

**Material:** `powerbi/README.md`

### Módulo 4: Automação com Scripts (45 min)
Automatize a coleta de dados de inventário usando PowerShell e análise com Python.

**Material:** 
- `scripts/powershell/`
- `scripts/python/`

### Módulo 5: Exercícios Práticos (60 min)
Resolva casos práticos de análise ABC, gestão de garantias e criação de dashboards.

**Material:** `exercicios/`

## 🎓 Como Usar Este Material

### Para Instrutores

1. Leia o **plano de aula completo** em `docs/plano-de-aula.md`
2. Familiarize-se com os **templates Excel** e dados de exemplo
3. Prepare o ambiente testando os **scripts de automação**
4. Revise as **melhores práticas** em `docs/melhores-praticas.md`

### Para Alunos

1. Comece pelo **guia rápido** em `docs/guia-rapido.md`
2. Siga os módulos na ordem sugerida
3. Pratique com os **dados de exemplo** fornecidos
4. Complete os **exercícios práticos** ao final de cada módulo

## 📊 Exemplos de Uso

### Coleta Automatizada de Inventário

```powershell
# Execute o script PowerShell para coletar dados do hardware
.\scripts\powershell\coletar-inventario-hardware.ps1
```

### Análise de Dados com Python

```python
# Execute o script de análise
python scripts/python/analisar-inventario.py
```

### Dashboard no Excel

Abra `excel/dashboard-excel-exemplo.xlsx` para ver um exemplo completo de dashboard com:
- 📈 Gráficos de distribuição de ativos
- ⚠️ Alertas de garantia vencendo
- 💰 Análise de custos por departamento
- 📊 Métricas de utilização

## 🔧 Funcionalidades Principais

### Templates Excel
- ✅ Tabelas estruturadas com validação de dados
- ✅ Fórmulas automáticas para cálculo de idade e garantia
- ✅ Formatação condicional para alertas visuais
- ✅ Dashboards integrados com gráficos dinâmicos

### Scripts de Automação
- ✅ Coleta automática de informações de hardware via WMI
- ✅ Inventário de software instalado
- ✅ Exportação para CSV/Excel
- ✅ Análise estatística com Python

### Dados de Exemplo
- ✅ 50+ registros de hardware fictícios
- ✅ 30+ registros de licenças de software
- ✅ Histórico de manutenções
- ✅ Cenários variados para aprendizado

## 📖 Documentação Adicional

- **[Plano de Aula Completo](docs/plano-de-aula.md)** - Estrutura detalhada do curso
- **[Guia Rápido](docs/guia-rapido.md)** - Primeiros passos
- **[Melhores Práticas](docs/melhores-praticas.md)** - Recomendações de ITAM
- **[Instruções Power BI](powerbi/README.md)** - Como criar o dashboard

## 🤝 Contribuindo

Contribuições são bem-vindas! Se você tem sugestões de melhorias, novos exercícios ou correções:

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/NovaFuncionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/NovaFuncionalidade`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para detalhes.

## 👥 Autores

- **GUIPETAV** - *Criador do material* - [GitHub](https://github.com/GUIPETAV)

## 🙏 Agradecimentos

- Comunidade de ITAM por compartilhar conhecimento
- Profissionais de TI que contribuíram com casos de uso reais
- Alunos que testaram e deram feedback sobre o material

## 📞 Suporte

Se você tiver dúvidas ou problemas:

- 📧 Abra uma [Issue](https://github.com/GUIPETAV/inventario-parque-tecnologico/issues)
- 💬 Participe das discussões
- 📖 Consulte a documentação em `docs/`

---

⭐ **Se este material foi útil para você, considere dar uma estrela no repositório!** ⭐
