"""
Script para análise de inventário de TI
Realiza análises estatísticas e gera insights
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

def carregar_dados(arquivo):
    """Carrega dados do inventário"""
    try:
        df = pd.read_csv(arquivo, encoding='utf-8')
        return df
    except:
        df = pd.read_csv(arquivo, encoding='latin-1')
        return df

def analisar_hardware(df):
    """Analisa dados de hardware"""
    print("=" * 60)
    print("ANÁLISE DE HARDWARE")
    print("=" * 60)
    
    # Total de ativos
    print(f"\nTotal de Ativos: {len(df)}")
    
    # Distribuição por tipo
    print("\n📊 Distribuição por Tipo:")
    print(df['Tipo'].value_counts())
    
    # Distribuição por status
    print("\n📊 Distribuição por Status:")
    print(df['Status'].value_counts())
    
    # Distribuição por departamento
    print("\n📊 Distribuição por Departamento:")
    print(df['Departamento'].value_counts())
    
    # Análise de idade
    if 'Data_Aquisicao' in df.columns:
        df['Data_Aquisicao'] = pd.to_datetime(df['Data_Aquisicao'], errors='coerce')
        df['Idade_Anos'] = (datetime.now() - df['Data_Aquisicao']).dt.days / 365.25
        
        print(f"\n📊 Idade Média dos Equipamentos: {df['Idade_Anos'].mean():.1f} anos")
        print(f"   Equipamento mais antigo: {df['Idade_Anos'].max():.1f} anos")
        print(f"   Equipamento mais novo: {df['Idade_Anos'].min():.1f} anos")
    
    # Análise de garantia
    if 'Garantia_Fim' in df.columns:
        df['Garantia_Fim'] = pd.to_datetime(df['Garantia_Fim'], errors='coerce')
        hoje = datetime.now()
        
        em_garantia = df[df['Garantia_Fim'] >= hoje]
        vencidas = df[df['Garantia_Fim'] < hoje]
        vencendo_30 = df[(df['Garantia_Fim'] >= hoje) & (df['Garantia_Fim'] <= hoje + timedelta(days=30))]
        
        print(f"\n⚠️  ALERTAS DE GARANTIA:")
        print(f"   Em garantia: {len(em_garantia)}")
        print(f"   Vencendo em 30 dias: {len(vencendo_30)}")
        print(f"   Garantia vencida: {len(vencidas)}")
    
    # Análise de configuração
    if 'RAM_GB' in df.columns:
        print(f"\n💾 Análise de Memória RAM:")
        print(f"   Média: {df['RAM_GB'].mean():.1f} GB")
        print(f"   Configurações:")
        print(df['RAM_GB'].value_counts().sort_index())
    
    # Valor total do parque
    if 'Valor_Aquisicao' in df.columns:
        total_valor = df['Valor_Aquisicao'].sum()
        print(f"\n💰 Valor Total do Parque: R$ {total_valor:,.2f}")
        print(f"   Valor médio por ativo: R$ {df['Valor_Aquisicao'].mean():,.2f}")

def analisar_licencas(df):
    """Analisa dados de licenças"""
    print("\n" + "=" * 60)
    print("ANÁLISE DE LICENÇAS")
    print("=" * 60)
    
    # Total de licenças
    print(f"\nTotal de Licenças: {len(df)}")
    
    # Licenças por software
    print("\n📊 Top 10 Software:")
    print(df['Software'].value_counts().head(10))
    
    # Análise de utilização
    if 'Quantidade_Adquirida' in df.columns and 'Quantidade_Utilizada' in df.columns:
        df['Taxa_Utilizacao'] = (df['Quantidade_Utilizada'] / df['Quantidade_Adquirida'] * 100)
        df['Licencas_Disponiveis'] = df['Quantidade_Adquirida'] - df['Quantidade_Utilizada']
        
        print(f"\n📊 Taxa de Utilização Média: {df['Taxa_Utilizacao'].mean():.1f}%")
        
        subutilizadas = df[df['Taxa_Utilizacao'] < 50]
        print(f"\n⚠️  Licenças Subutilizadas (<50%): {len(subutilizadas)}")
        if len(subutilizadas) > 0:
            print(subutilizadas[['Software', 'Quantidade_Adquirida', 'Quantidade_Utilizada', 'Taxa_Utilizacao']])
        
        excesso = df[df['Quantidade_Utilizada'] > df['Quantidade_Adquirida']]
        print(f"\n❌ Licenças em Excesso (risco compliance): {len(excesso)}")
        if len(excesso) > 0:
            print(excesso[['Software', 'Quantidade_Adquirida', 'Quantidade_Utilizada']])
    
    # Análise de vencimento
    if 'Data_Validade' in df.columns:
        df['Data_Validade'] = pd.to_datetime(df['Data_Validade'], errors='coerce')
        hoje = datetime.now()
        
        vencendo_30 = df[(df['Data_Validade'] >= hoje) & (df['Data_Validade'] <= hoje + timedelta(days=30))]
        vencendo_90 = df[(df['Data_Validade'] >= hoje) & (df['Data_Validade'] <= hoje + timedelta(days=90))]
        vencidas = df[df['Data_Validade'] < hoje]
        
        print(f"\n⚠️  ALERTAS DE VENCIMENTO:")
        print(f"   Vencendo em 30 dias: {len(vencendo_30)}")
        print(f"   Vencendo em 90 dias: {len(vencendo_90)}")
        print(f"   Vencidas: {len(vencidas)}")
    
    # Valor total
    if 'Valor_Total' in df.columns:
        total_valor = df['Valor_Total'].sum()
        print(f"\n💰 Investimento Total em Licenças: R$ {total_valor:,.2f}")

def main():
    """Função principal"""
    print("🔍 ANÁLISE DE INVENTÁRIO DE PARQUE TECNOLÓGICO")
    print("=" * 60)
    
    # Analisar hardware
    try:
        df_hardware = carregar_dados('dados-exemplo/hardware-sample.csv')
        analisar_hardware(df_hardware)
    except FileNotFoundError:
        print("⚠️  Arquivo hardware-sample.csv não encontrado")
    except Exception as e:
        print(f"❌ Erro ao analisar hardware: {e}")
    
    # Analisar licenças
    try:
        df_licencas = carregar_dados('dados-exemplo/licencas-sample.csv')
        analisar_licencas(df_licencas)
    except FileNotFoundError:
        print("⚠️  Arquivo licencas-sample.csv não encontrado")
    except Exception as e:
        print(f"❌ Erro ao analisar licenças: {e}")
    
    print("\n" + "=" * 60)
    print("✅ Análise concluída!")
    print("=" * 60)

if __name__ == "__main__":
    main()
