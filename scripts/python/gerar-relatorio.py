"""
Script para gerar relatório de inventário em formato profissional
"""

import pandas as pd
import numpy as np
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

def carregar_dados(arquivo):
    """Carrega dados do inventário"""
    try:
        df = pd.read_csv(arquivo, encoding='utf-8')
        return df
    except:
        try:
            df = pd.read_csv(arquivo, encoding='latin-1')
            return df
        except FileNotFoundError:
            return None

def gerar_cabecalho():
    """Gera cabeçalho do relatório"""
    print("\n" + "=" * 80)
    print(" " * 20 + "RELATÓRIO DE INVENTÁRIO DE TI")
    print(" " * 25 + f"Data: {datetime.now().strftime('%d/%m/%Y %H:%M')}")
    print("=" * 80)

def gerar_sumario_executivo(df_hardware, df_licencas):
    """Gera sumário executivo"""
    print("\n📊 SUMÁRIO EXECUTIVO")
    print("-" * 80)
    
    if df_hardware is not None:
        total_ativos = len(df_hardware)
        ativos_ativos = len(df_hardware[df_hardware['Status'] == 'Ativo'])
        valor_total = df_hardware['Valor_Aquisicao'].sum() if 'Valor_Aquisicao' in df_hardware.columns else 0
        
        print(f"Total de Ativos de Hardware: {total_ativos}")
        print(f"Ativos em Operação: {ativos_ativos} ({ativos_ativos/total_ativos*100:.1f}%)")
        print(f"Valor Total do Parque: R$ {valor_total:,.2f}")
    
    if df_licencas is not None:
        total_licencas = df_licencas['Quantidade_Adquirida'].sum() if 'Quantidade_Adquirida' in df_licencas.columns else len(df_licencas)
        print(f"Total de Licenças: {total_licencas}")

def gerar_alertas(df_hardware, df_licencas):
    """Gera alertas críticos"""
    print("\n⚠️  ALERTAS CRÍTICOS")
    print("-" * 80)
    
    alertas = []
    
    # Alertas de hardware
    if df_hardware is not None:
        # Garantias vencendo
        if 'Garantia_Fim' in df_hardware.columns:
            df_hardware['Garantia_Fim'] = pd.to_datetime(df_hardware['Garantia_Fim'], errors='coerce')
            hoje = datetime.now()
            vencendo = df_hardware[
                (df_hardware['Garantia_Fim'] >= hoje) & 
                (df_hardware['Garantia_Fim'] <= hoje + pd.Timedelta(days=30))
            ]
            if len(vencendo) > 0:
                alertas.append(f"🔴 {len(vencendo)} equipamento(s) com garantia vencendo em 30 dias")
        
        # Equipamentos em manutenção
        if 'Status' in df_hardware.columns:
            manutencao = df_hardware[df_hardware['Status'] == 'Manutenção']
            if len(manutencao) > 0:
                alertas.append(f"🟡 {len(manutencao)} equipamento(s) em manutenção")
        
        # Equipamentos antigos
        if 'Data_Aquisicao' in df_hardware.columns:
            df_hardware['Data_Aquisicao'] = pd.to_datetime(df_hardware['Data_Aquisicao'], errors='coerce')
            df_hardware['Idade_Anos'] = (datetime.now() - df_hardware['Data_Aquisicao']).dt.days / 365.25
            antigos = df_hardware[df_hardware['Idade_Anos'] > 5]
            if len(antigos) > 0:
                alertas.append(f"🟠 {len(antigos)} equipamento(s) com mais de 5 anos de uso")
    
    # Alertas de licenças
    if df_licencas is not None:
        # Licenças vencendo
        if 'Data_Validade' in df_licencas.columns:
            df_licencas['Data_Validade'] = pd.to_datetime(df_licencas['Data_Validade'], errors='coerce')
            hoje = datetime.now()
            vencendo = df_licencas[
                (df_licencas['Data_Validade'] >= hoje) & 
                (df_licencas['Data_Validade'] <= hoje + pd.Timedelta(days=90))
            ]
            if len(vencendo) > 0:
                alertas.append(f"🔴 {len(vencendo)} licença(s) vencendo em 90 dias")
        
        # Licenças em excesso
        if 'Quantidade_Adquirida' in df_licencas.columns and 'Quantidade_Utilizada' in df_licencas.columns:
            excesso = df_licencas[df_licencas['Quantidade_Utilizada'] > df_licencas['Quantidade_Adquirida']]
            if len(excesso) > 0:
                alertas.append(f"🔴 {len(excesso)} licença(s) com uso acima do adquirido (RISCO COMPLIANCE)")
            
            # Subutilização
            df_licencas['Taxa_Utilizacao'] = df_licencas['Quantidade_Utilizada'] / df_licencas['Quantidade_Adquirida'] * 100
            subutilizadas = df_licencas[df_licencas['Taxa_Utilizacao'] < 50]
            if len(subutilizadas) > 0:
                alertas.append(f"🟡 {len(subutilizadas)} licença(s) com menos de 50% de utilização")
    
    if alertas:
        for alerta in alertas:
            print(f"  {alerta}")
    else:
        print("  ✅ Nenhum alerta crítico identificado")

def gerar_recomendacoes(df_hardware, df_licencas):
    """Gera recomendações"""
    print("\n💡 RECOMENDAÇÕES")
    print("-" * 80)
    
    recomendacoes = []
    
    if df_hardware is not None:
        # Equipamentos antigos
        if 'Data_Aquisicao' in df_hardware.columns:
            df_hardware['Data_Aquisicao'] = pd.to_datetime(df_hardware['Data_Aquisicao'], errors='coerce')
            df_hardware['Idade_Anos'] = (datetime.now() - df_hardware['Data_Aquisicao']).dt.days / 365.25
            antigos = df_hardware[df_hardware['Idade_Anos'] > 5]
            if len(antigos) > 0:
                recomendacoes.append(f"Planejar substituição de {len(antigos)} equipamento(s) com mais de 5 anos")
        
        # Garantias vencidas
        if 'Garantia_Fim' in df_hardware.columns:
            df_hardware['Garantia_Fim'] = pd.to_datetime(df_hardware['Garantia_Fim'], errors='coerce')
            vencidas = df_hardware[df_hardware['Garantia_Fim'] < datetime.now()]
            if len(vencidas) > 0:
                recomendacoes.append(f"Avaliar renovação de garantia para {len(vencidas)} equipamento(s)")
    
    if df_licencas is not None:
        # Otimização de licenças
        if 'Quantidade_Adquirida' in df_licencas.columns and 'Quantidade_Utilizada' in df_licencas.columns:
            df_licencas['Taxa_Utilizacao'] = df_licencas['Quantidade_Utilizada'] / df_licencas['Quantidade_Adquirida'] * 100
            subutilizadas = df_licencas[df_licencas['Taxa_Utilizacao'] < 50]
            if len(subutilizadas) > 0:
                economia_potencial = (subutilizadas['Quantidade_Adquirida'] - subutilizadas['Quantidade_Utilizada']).sum()
                recomendacoes.append(f"Otimizar {len(subutilizadas)} licença(s) subutilizada(s) - Economia de {economia_potencial} licenças")
    
    if recomendacoes:
        for i, rec in enumerate(recomendacoes, 1):
            print(f"  {i}. {rec}")
    else:
        print("  ✅ Nenhuma recomendação pendente")

def gerar_graficos_texto(df_hardware):
    """Gera gráficos em modo texto"""
    if df_hardware is None:
        return
    
    print("\n📈 DISTRIBUIÇÕES")
    print("-" * 80)
    
    # Distribuição por tipo
    if 'Tipo' in df_hardware.columns:
        print("\nPor Tipo de Equipamento:")
        tipos = df_hardware['Tipo'].value_counts()
        max_count = tipos.max()
        for tipo, count in tipos.items():
            barra = "█" * int((count / max_count) * 40)
            print(f"  {tipo:20s} {barra} {count}")
    
    # Distribuição por departamento
    if 'Departamento' in df_hardware.columns:
        print("\nPor Departamento:")
        depts = df_hardware['Departamento'].value_counts()
        max_count = depts.max()
        for dept, count in depts.items():
            barra = "█" * int((count / max_count) * 40)
            print(f"  {dept:20s} {barra} {count}")

def gerar_rodape():
    """Gera rodapé do relatório"""
    print("\n" + "=" * 80)
    print("Relatório gerado automaticamente pelo Sistema de Inventário de TI")
    print(f"Gerado em: {datetime.now().strftime('%d/%m/%Y às %H:%M:%S')}")
    print("=" * 80 + "\n")

def main():
    """Função principal"""
    # Carregar dados
    df_hardware = carregar_dados('dados-exemplo/hardware-sample.csv')
    df_licencas = carregar_dados('dados-exemplo/licencas-sample.csv')
    
    # Gerar relatório
    gerar_cabecalho()
    gerar_sumario_executivo(df_hardware, df_licencas)
    gerar_alertas(df_hardware, df_licencas)
    gerar_recomendacoes(df_hardware, df_licencas)
    gerar_graficos_texto(df_hardware)
    gerar_rodape()
    
    # Salvar em arquivo
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"relatorio_inventario_{timestamp}.txt"
    
    print(f"💾 Relatório também foi salvo em: {filename}")

if __name__ == "__main__":
    main()
