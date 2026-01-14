# ⚠️ Exercício 2: Gestão de Garantias

## 🎯 Objetivo
Criar um sistema de controle e alertas de garantias dos equipamentos, identificando ativos que necessitam renovação ou substituição, e calcular o investimento necessário.

## 📚 Conceito: Gestão de Garantias

A gestão adequada de garantias permite:
- ✅ Reduzir custos de manutenção
- ✅ Evitar paradas não programadas
- ✅ Planejar renovações com antecedência
- ✅ Negociar melhores condições com fornecedores
- ✅ Manter conformidade com políticas de TI

## 📝 Instruções

### Passo 1: Preparar os Dados (5 min)

1. Abra o arquivo com inventário de hardware
2. Certifique-se de ter as colunas:
   - ID_Ativo
   - Tipo
   - Marca
   - Modelo
   - Data_Aquisicao
   - Valor_Aquisicao
   - Garantia_Inicio
   - Garantia_Fim
   - Status

3. Se necessário, importe os dados de exemplo:
   ```
   dados-exemplo/hardware-sample.csv
   ```

### Passo 2: Criar Colunas Calculadas (10 min)

Adicione as seguintes colunas:

#### Coluna 1: Dias para Vencimento

```excel
=SE([@Garantia_Fim]="";"";DIAS([@Garantia_Fim];HOJE()))
```

**Explicação:**
- DIAS calcula a diferença entre duas datas
- Positivo = ainda tem garantia
- Negativo = garantia vencida
- Vazio se não houver data de garantia

#### Coluna 2: Status da Garantia

```excel
=SE([@Garantia_Fim]="";
    "Sem Informação";
    SE([@Garantia_Fim]<HOJE();
        "VENCIDA";
        SE([@Garantia_Fim]<=HOJE()+30;
            "CRÍTICO - Vence em " & DIAS([@Garantia_Fim];HOJE()) & " dias";
            SE([@Garantia_Fim]<=HOJE()+60;
                "ALERTA - Vence em " & DIAS([@Garantia_Fim];HOJE()) & " dias";
                SE([@Garantia_Fim]<=HOJE()+90;
                    "ATENÇÃO - Vence em " & DIAS([@Garantia_Fim];HOJE()) & " dias";
                    "EM GARANTIA"
                )
            )
        )
    )
)
```

**Status possíveis:**
- 🔴 CRÍTICO: Vence em até 30 dias
- 🟠 ALERTA: Vence em 31-60 dias
- 🟡 ATENÇÃO: Vence em 61-90 dias
- 🟢 EM GARANTIA: Vence em mais de 90 dias
- ⚫ VENCIDA: Já passou
- ⚪ Sem Informação: Não cadastrada

#### Coluna 3: Categoria de Prioridade

```excel
=SE([@Status_Garantia]="VENCIDA";"P1 - URGENTE";
   SE(ÉNÚM(PROCURAR("CRÍTICO";[@Status_Garantia]));"P2 - MUITO ALTA";
   SE(ÉNÚM(PROCURAR("ALERTA";[@Status_Garantia]));"P3 - ALTA";
   SE(ÉNÚM(PROCURAR("ATENÇÃO";[@Status_Garantia]));"P4 - MÉDIA";
   "P5 - BAIXA"))))
```

#### Coluna 4: Custo Estimado de Renovação

```excel
=[@Valor_Aquisicao] * 
 SE([@Tipo]="Servidor";0.25;
 SE([@Tipo]="Notebook";0.15;
 SE([@Tipo]="Desktop";0.10;0.12)))
```

**Explicação:**
- Servidor: 25% do valor (manutenção cara)
- Notebook: 15% do valor
- Desktop: 10% do valor
- Outros: 12% do valor

### Passo 3: Aplicar Formatação Condicional (5 min)

1. **Coluna "Status_Garantia":**
   - Contém "CRÍTICO": Vermelho escuro + branco
   - Contém "ALERTA": Laranja + preto
   - Contém "ATENÇÃO": Amarelo + preto
   - "VENCIDA": Vermelho claro
   - "EM GARANTIA": Verde claro

2. **Coluna "Dias_para_Vencimento":**
   - Escala de cores: Vermelho (0) → Amarelo (30) → Verde (90)

3. **Coluna "Categoria_Prioridade":**
   - P1: Vermelho forte
   - P2: Laranja forte
   - P3: Amarelo
   - P4: Azul claro
   - P5: Cinza

### Passo 4: Criar Relatórios (15 min)

#### Relatório 1: Lista Prioritária

Crie uma nova aba "Ação_Garantias" com:

1. **Filtro aplicado:**
   - Status_Garantia ≠ "EM GARANTIA"
   - Status ≠ "Descartado"

2. **Ordenação:**
   - Prioridade (P1 → P5)
   - Dias_para_Vencimento (crescente)

3. **Colunas visíveis:**
   - Prioridade
   - ID_Ativo
   - Tipo
   - Marca/Modelo
   - Status_Garantia
   - Garantia_Fim
   - Custo_Estimado_Renovacao
   - Ação_Recomendada

4. **Adicione coluna "Ação_Recomendada":**

```excel
=SE([@Categoria_Prioridade]="P1 - URGENTE";
    "Renovar IMEDIATAMENTE ou substituir";
    SE([@Categoria_Prioridade]="P2 - MUITO ALTA";
        "Solicitar cotação urgente";
        SE([@Categoria_Prioridade]="P3 - ALTA";
            "Planejar renovação este mês";
            "Incluir no planejamento próximo trimestre"
        )
    )
)
```

#### Relatório 2: Dashboard de Garantias

Crie uma nova aba "Dashboard_Garantias" com:

**KPIs (Cards grandes no topo):**

1. Total de Ativos com Garantia Vencida
   ```excel
   =CONT.SE(Tabela[Status_Garantia];"VENCIDA")
   ```

2. Garantias Vencendo em 30 dias
   ```excel
   =CONT.SE(Tabela[Status_Garantia];"CRÍTICO*")
   ```

3. Investimento Necessário (30 dias)
   ```excel
   =SOMASE(Tabela[Status_Garantia];"CRÍTICO*";Tabela[Custo_Estimado_Renovacao])
   ```

4. Investimento Necessário (90 dias)
   ```excel
   =SOMASES(Tabela[Custo_Estimado_Renovacao];
            Tabela[Dias_para_Vencimento];">0";
            Tabela[Dias_para_Vencimento];"<=90")
   ```

**Gráficos:**

1. **Gráfico de Pizza:** Distribuição por Status de Garantia
2. **Gráfico de Barras:** Equipamentos por Prioridade
3. **Gráfico de Colunas:** Custo de Renovação por Tipo
4. **Gráfico de Linha:** Vencimentos nos próximos 12 meses

### Passo 5: Criar Cronograma de Ações (10 min)

Crie uma tabela "Cronograma_Renovacoes":

| Mês | Qtd Vencendo | Custo Estimado | Status | Ação |
|-----|-------------|----------------|--------|------|
| Jan/2026 | 3 | R$ 4.500 | Pendente | Solicitar cotações |
| Fev/2026 | 5 | R$ 7.200 | Pendente | - |
| Mar/2026 | 2 | R$ 3.100 | Pendente | - |

**Fórmula para Qtd Vencendo (para Janeiro):**
```excel
=CONT.SE.S(Tabela[Garantia_Fim];
          ">=01/01/2026";
          Tabela[Garantia_Fim];
          "<=31/01/2026")
```

### Passo 6: Análise de Decisão (10 min)

Para cada equipamento em P1 ou P2, decida:

#### Critérios de Decisão:

**RENOVAR a garantia quando:**
- ✅ Equipamento tem menos de 3 anos
- ✅ Custo de renovação < 30% do valor de compra
- ✅ Equipamento crítico para operação
- ✅ Sem orçamento para substituição

**SUBSTITUIR quando:**
- ✅ Equipamento tem mais de 4 anos
- ✅ Custo de renovação > 40% do valor atual
- ✅ Histórico de muitas manutenções
- ✅ Equipamento obsoleto

**MANTER sem garantia quando:**
- ✅ Equipamento não crítico
- ✅ Custo de renovação muito alto
- ✅ Próximo de substituição programada
- ✅ Backup disponível

Adicione coluna "Decisão" com a recomendação.

## 📊 Análises Requeridas

Responda às seguintes perguntas:

### Análise Quantitativa:

1. **Quantos equipamentos estão com garantia vencida?**
   - Resposta: _____
   - Percentual do total: _____%

2. **Quantos equipamentos vencem em 30 dias?**
   - Resposta: _____
   - Principais tipos: _____

3. **Qual é o investimento total necessário para renovar todas as garantias vencendo em 90 dias?**
   - Resposta: R$ _____

4. **Qual tipo de equipamento representa maior custo de renovação?**
   - Resposta: _____
   - Valor: R$ _____

### Análise Qualitativa:

5. **Existem equipamentos críticos sem garantia?**
   - Liste os 3 mais importantes

6. **Qual é o risco de não renovar as garantias P1/P2?**
   - Descreva impactos operacionais

7. **É possível negociar renovações em lote para reduzir custos?**
   - Agrupe por fabricante

## 💡 Plano de Ação

### Ações Imediatas (Esta Semana):

- [ ] Solicitar cotações para equipamentos P1 (vencidos)
- [ ] Aprovar orçamento emergencial se necessário
- [ ] Notificar gestores dos departamentos afetados

### Ações de Curto Prazo (Este Mês):

- [ ] Renovar garantias de equipamentos P2 (críticos)
- [ ] Avaliar substituição vs renovação (equipamentos >4 anos)
- [ ] Negociar condições com fornecedores

### Ações de Médio Prazo (Próximo Trimestre):

- [ ] Planejar renovações P3 e P4
- [ ] Criar política de gestão de garantias
- [ ] Implementar alertas automáticos

### Ações de Longo Prazo (Este Ano):

- [ ] Padronizar garantias mínimas por tipo
- [ ] Avaliar contratos de garantia estendida
- [ ] Incluir gestão de garantias no processo de compra

## 🎯 Entregáveis

1. ✅ Planilha com status de todas as garantias
2. ✅ Lista prioritária de ações
3. ✅ Dashboard visual
4. ✅ Cronograma de renovações (12 meses)
5. ✅ Estimativa de investimento necessário
6. ✅ Plano de ação detalhado

## 📧 Comunicação aos Stakeholders

Prepare um e-mail executivo com:

**Assunto:** [URGENTE] Garantias de Equipamentos - Ação Necessária

**Conteúdo:**
- Situação atual (números consolidados)
- Riscos identificados
- Investimento necessário
- Ações recomendadas
- Cronograma proposto

## 🏆 Critérios de Avaliação

| Critério | Peso | Pontos |
|----------|------|--------|
| Fórmulas e cálculos corretos | 25% | /25 |
| Dashboard informativo | 20% | /20 |
| Análise de prioridades | 20% | /20 |
| Plano de ação realista | 20% | /20 |
| Comunicação executiva | 15% | /15 |
| **TOTAL** | **100%** | **/100** |

## 💼 Caso Real

**Cenário:**
Você é o analista de TI. Durante a análise, descobriu que 15 servidores críticos estão com garantia vencida há 3 meses. O diretor financeiro diz que não há orçamento. O que fazer?

**Sua resposta/estratégia:**
_________________________________________________
_________________________________________________
_________________________________________________

## 🔄 Próximos Passos

Após completar este exercício:
1. Implemente sistema de alertas automáticos
2. Vá para **Exercício 3: Dashboard Executivo no Power BI**
3. Integre análise de garantias com análise ABC

---

**Tempo estimado:** 50 minutos  
**Dificuldade:** ⭐⭐⭐☆☆ (Intermediário+)  
**Pré-requisitos:** Excel intermediário, fórmulas condicionais

**Boa sorte! 🚀**
