# 📊 Exercício 1: Análise ABC de Ativos

## 🎯 Objetivo
Aplicar a metodologia de Análise ABC (Curva de Pareto) para classificar os ativos de TI com base no valor, identificando quais equipamentos representam a maior parte do investimento.

## 📚 Conceito: Análise ABC

A Análise ABC é uma técnica de classificação que divide itens em três categorias:

- **Classe A:** 20% dos itens que representam 80% do valor total (alta prioridade)
- **Classe B:** 30% dos itens que representam 15% do valor total (média prioridade)
- **Classe C:** 50% dos itens que representam 5% do valor total (baixa prioridade)

## 📝 Instruções

### Passo 1: Preparar os Dados (5 min)

1. Abra o arquivo `excel/template-inventario-hardware.xlsx`
2. Se ainda não tiver dados, importe: `dados-exemplo/hardware-sample.csv`
   - No Excel: Dados → Obter Dados → De Texto/CSV
   - Selecione o arquivo
   - Clique em "Carregar"

3. Verifique se todas as colunas estão corretas:
   - ID_Ativo
   - Tipo
   - Marca
   - Modelo
   - Valor_Aquisicao
   - Status

### Passo 2: Ordenar por Valor (2 min)

1. Selecione toda a tabela de dados
2. Vá em: Dados → Classificar
3. Ordenar por: **Valor_Aquisicao**
4. Ordem: **Do Maior para o Menor**

### Passo 3: Criar Colunas Calculadas (10 min)

Adicione as seguintes colunas à direita dos seus dados:

#### Coluna 1: Valor Acumulado

```excel
=SOMA($E$2:E2)
```

**Explicação:**
- `$E$2` é fixo (primeira célula de valor)
- `E2` é relativo (célula atual)
- Ao arrastar para baixo, acumula os valores

**Insira em:** Coluna "Valor_Acumulado"
**Comece em:** Segunda linha da tabela

#### Coluna 2: Percentual Acumulado

```excel
=Valor_Acumulado / SOMA($E$2:$E$51) * 100
```

**Explicação:**
- Divide o valor acumulado pelo total
- Multiplica por 100 para obter percentual

**Insira em:** Coluna "Percentual_Acumulado"

#### Coluna 3: Classificação ABC

```excel
=SE([@Percentual_Acumulado]<=80;"A";SE([@Percentual_Acumulado]<=95;"B";"C"))
```

**Explicação:**
- Se percentual ≤ 80% → Classe A
- Se percentual ≤ 95% → Classe B
- Caso contrário → Classe C

**Insira em:** Coluna "Classificacao_ABC"

### Passo 4: Formatar Tabela (3 min)

1. Aplique formatação condicional na coluna "Classificacao_ABC":
   - Classe A: Verde escuro (alto valor)
   - Classe B: Amarelo (médio valor)
   - Classe C: Cinza claro (baixo valor)

2. Formate a coluna "Valor_Aquisicao":
   - Formato: Moeda (R$)
   - 2 casas decimais

3. Formate "Percentual_Acumulado":
   - Formato: Percentual
   - 1 casa decimal

### Passo 5: Criar Visualizações (15 min)

#### Gráfico 1: Curva ABC (Gráfico de Pareto)

1. Selecione: ID_Ativo, Valor_Aquisicao, Percentual_Acumulado
2. Inserir → Gráficos Recomendados
3. Escolha: **Combinação** (Colunas + Linha)
4. Configure:
   - Eixo Principal: Valor_Aquisicao (Coluna)
   - Eixo Secundário: Percentual_Acumulado (Linha)
5. Adicione linha horizontal em 80% para marcar limite Classe A

**Título sugerido:** "Curva ABC - Concentração de Valor dos Ativos"

#### Gráfico 2: Distribuição por Classe

1. Crie Tabela Dinâmica:
   - Linhas: Classificacao_ABC
   - Valores: 
     - Contagem de ID_Ativo
     - Soma de Valor_Aquisicao

2. Insira Gráfico de Pizza:
   - Dados: Valor_Aquisicao por Classe
   - Mostrar percentuais

**Título sugerido:** "Distribuição de Valor por Classe ABC"

#### Gráfico 3: Análise por Tipo de Equipamento

1. Crie Tabela Dinâmica:
   - Linhas: Tipo
   - Colunas: Classificacao_ABC
   - Valores: Contagem de ID_Ativo

2. Insira Gráfico de Barras Empilhadas

**Título sugerido:** "Distribuição ABC por Tipo de Equipamento"

### Passo 6: Análise e Insights (10 min)

Responda às seguintes perguntas com base nos seus dados:

#### Questões para Análise:

1. **Quantos ativos estão na Classe A?**
   - Número: _____
   - Percentual do total: _____%
   - Valor representado: R$ _____

2. **Quais tipos de equipamentos predominam na Classe A?**
   - Liste os 3 principais tipos

3. **Qual é o valor do ativo mais caro?**
   - ID: _____
   - Tipo: _____
   - Valor: R$ _____

4. **Os ativos Classe A representam que percentual do valor total?**
   - Resposta: _____%
   - Está próximo dos 80% teóricos? _____

5. **Identifique equipamentos Classe C com mais de 3 anos:**
   - Estes são candidatos a descarte/doação
   - Quantos encontrou? _____

## 📊 Exemplo de Resultado Esperado

### Tabela Resumo ABC

| Classe | Quantidade | % Qtd | Valor Total | % Valor |
|--------|-----------|-------|-------------|---------|
| A | 10 | 20% | R$ 240.000 | 80% |
| B | 15 | 30% | R$ 45.000 | 15% |
| C | 25 | 50% | R$ 15.000 | 5% |
| **Total** | **50** | **100%** | **R$ 300.000** | **100%** |

## 💡 Insights Acionáveis

Com base na sua análise ABC, identifique:

### Ações Recomendadas para Classe A:

✅ **Prioridade Máxima:**
- [ ] Garantir que todos têm garantia ativa
- [ ] Implementar backup/DR robusto
- [ ] Monitoramento proativo
- [ ] Contratos de suporte premium
- [ ] Seguro contra danos/roubo

### Ações Recomendadas para Classe B:

⚠️ **Prioridade Média:**
- [ ] Garantia básica adequada
- [ ] Backup regular
- [ ] Manutenção preventiva semestral

### Ações Recomendadas para Classe C:

ℹ️ **Prioridade Baixa:**
- [ ] Avaliar necessidade de manutenção
- [ ] Considerar descarte se > 5 anos
- [ ] Sem necessidade de garantia estendida
- [ ] Candidatos a doação quando substituídos

## 🎯 Entregáveis

Ao final deste exercício, você deve ter:

1. ✅ Planilha Excel com classificação ABC completa
2. ✅ 3 gráficos de visualização
3. ✅ Tabela resumo por classe
4. ✅ Lista de insights e recomendações
5. ✅ Plano de ação priorizado

## 🏆 Critérios de Avaliação

| Critério | Peso | Pontos |
|----------|------|--------|
| Fórmulas corretas | 30% | /30 |
| Gráficos adequados | 25% | /25 |
| Análise de insights | 25% | /25 |
| Recomendações acionáveis | 20% | /20 |
| **TOTAL** | **100%** | **/100** |

## 📚 Recursos Adicionais

### Leitura Recomendada:
- Gestão de Ativos de TI - Capítulo sobre Priorização
- Análise ABC/Curva de Pareto aplicada a ITAM

### Vídeos Sugeridos:
- "Como fazer Análise ABC no Excel" (YouTube)
- "Curva de Pareto para Gestão de Ativos"

## 🤔 Perguntas Frequentes

**P: E se meu resultado não for exatamente 80-15-5?**
R: A regra 80-15-5 é teórica. Na prática, pode variar (ex: 75-20-5 ou 85-12-3). O importante é identificar onde está a concentração de valor.

**P: Devo considerar apenas o valor de aquisição?**
R: Para esta análise sim. Em análises avançadas, você pode usar TCO (Total Cost of Ownership) que inclui manutenção e operação.

**P: Como lidar com ativos sem valor de aquisição?**
R: Estime um valor de mercado ou use o valor médio de ativos similares. Não os exclua da análise.

**P: Posso fazer análise ABC por departamento?**
R: Sim! Use filtros ou crie análises separadas. Isso ajuda cada área a priorizar seus ativos.

## 🔄 Próximos Passos

Após completar este exercício:
1. Vá para **Exercício 2: Gestão de Garantias**
2. Aplique classificação ABC em licenças de software
3. Crie dashboard executivo combinando ABC + outros KPIs

---

**Tempo estimado:** 45 minutos  
**Dificuldade:** ⭐⭐☆☆☆ (Intermediário)  
**Pré-requisitos:** Excel básico, fórmulas SE e SOMA

**Boa sorte! 🚀**
