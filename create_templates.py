#!/usr/bin/env python3
"""
Script to create professional Excel template files for inventory management.
Uses openpyxl library to create formatted workbooks with validation sheets.
"""

from openpyxl import Workbook
from openpyxl.styles import (
    Font, PatternFill, Alignment, Border, Side, numbers
)
from openpyxl.utils import get_column_letter
from datetime import datetime, timedelta
import os

# Define constants for styling
HEADER_FILL = PatternFill(start_color="003366", end_color="003366", fill_type="solid")
HEADER_FONT = Font(color="FFFFFF", bold=True, size=11)
BORDER_STYLE = Border(
    left=Side(style='thin'),
    right=Side(style='thin'),
    top=Side(style='thin'),
    bottom=Side(style='thin')
)
LIGHT_BLUE_FILL = PatternFill(start_color="E8F0F5", end_color="E8F0F5", fill_type="solid")
CENTER_ALIGNMENT = Alignment(horizontal="center", vertical="center", wrap_text=True)
LEFT_ALIGNMENT = Alignment(horizontal="left", vertical="center", wrap_text=True)

def set_column_width(ws, column_widths):
    """Set column widths for a worksheet."""
    for col, width in column_widths.items():
        ws.column_dimensions[col].width = width

def format_header_row(ws, headers, start_row=1):
    """Format header row with styling."""
    for col, header in enumerate(headers, 1):
        cell = ws.cell(row=start_row, column=col)
        cell.value = header
        cell.font = HEADER_FONT
        cell.fill = HEADER_FILL
        cell.alignment = CENTER_ALIGNMENT
        cell.border = BORDER_STYLE

def format_data_row(ws, row_num, row_data, start_col=1, alternate_color=False):
    """Format a data row with borders and optional alternating color."""
    for col, value in enumerate(row_data, start_col):
        cell = ws.cell(row=row_num, column=col)
        cell.value = value
        cell.border = BORDER_STYLE
        cell.alignment = LEFT_ALIGNMENT
        if alternate_color:
            cell.fill = LIGHT_BLUE_FILL

def freeze_panes(ws, freeze_cell="A2"):
    """Freeze panes at specified cell."""
    ws.freeze_panes = freeze_cell

def create_template_inventario_hardware():
    """Create template-inventario-hardware.xlsx"""
    wb = Workbook()
    
    # ===== ABA 1: HARDWARE =====
    ws_hardware = wb.active
    ws_hardware.title = "Hardware"
    
    headers = [
        "ID_Ativo", "Tipo", "Marca", "Modelo", "Numero_Serie",
        "Processador", "RAM_GB", "Armazenamento_GB", "Tipo_Armazenamento",
        "Sistema_Operacional", "Versao_SO", "Data_Aquisicao", "Valor_Aquisicao",
        "Garantia_Inicio", "Garantia_Fim", "Localizacao", "Departamento",
        "Usuario", "Status", "Observacoes"
    ]
    
    format_header_row(ws_hardware, headers)
    
    # Example data rows
    example_data = [
        [
            "HW-001", "Desktop", "Dell", "OptiPlex 7090", "R123456789",
            "Intel i7-11700", 16, 512, "SSD",
            "Windows", "11 Pro", datetime(2023, 6, 15), 4500.00,
            datetime(2023, 6, 15), datetime(2024, 6, 15), "Sala TI - Rack A1",
            "TI", "João Silva", "Ativo", "Em uso - Servidor web"
        ],
        [
            "HW-002", "Notebook", "Lenovo", "ThinkPad X13", "N987654321",
            "Intel i5-1135G7", 8, 256, "SSD",
            "Windows", "11", datetime(2023, 9, 22), 3200.00,
            datetime(2023, 9, 22), datetime(2024, 9, 22), "Sala de Reuniões",
            "Gerência", "Maria Santos", "Ativo", "Notebook executivo"
        ],
        [
            "HW-003", "Servidor", "HP", "ProLiant DL380", "S654321098",
            "Intel Xeon Gold 6248", 128, 2048, "SAS",
            "Linux", "Ubuntu 22.04", datetime(2022, 3, 10), 25000.00,
            datetime(2022, 3, 10), datetime(2025, 3, 10), "Data Center - Rack D2",
            "TI", "Carlos Oliveira", "Ativo", "Servidor de banco de dados principal"
        ]
    ]
    
    for row_idx, row_data in enumerate(example_data, 2):
        format_data_row(ws_hardware, row_idx, row_data, alternate_color=(row_idx % 2 == 0))
    
    # Format specific columns
    ws_hardware.column_dimensions['L'].number_format = 'dd/mm/yyyy'  # Data_Aquisicao
    ws_hardware.column_dimensions['M'].number_format = 'R$ #,##0.00'  # Valor_Aquisicao
    ws_hardware.column_dimensions['N'].number_format = 'dd/mm/yyyy'  # Garantia_Inicio
    ws_hardware.column_dimensions['O'].number_format = 'dd/mm/yyyy'  # Garantia_Fim
    
    column_widths_hw = {
        'A': 12, 'B': 12, 'C': 12, 'D': 15, 'E': 15, 'F': 20, 'G': 10, 'H': 15,
        'I': 15, 'J': 15, 'K': 10, 'L': 14, 'M': 14, 'N': 14, 'O': 14, 'P': 18,
        'Q': 12, 'R': 15, 'S': 10, 'T': 20
    }
    set_column_width(ws_hardware, column_widths_hw)
    freeze_panes(ws_hardware)
    
    # ===== ABA 2: VALIDAÇÕES =====
    ws_validacoes = wb.create_sheet("Validações")
    
    # Lists for dropdowns
    validation_data = {
        "Tipos": ["Desktop", "Notebook", "Servidor", "Impressora", "Switch", "Roteador", "Firewall"],
        "Status": ["Ativo", "Inativo", "Manutenção", "Descartado", "Emprestado"],
        "Departamentos": ["TI", "RH", "Financeiro", "Gerência", "Operações", "Vendas", "Administrativo"],
        "Localizacoes": ["Sala TI", "Data Center", "Sala de Reuniões", "Recepção", "Administrativo"],
        "TiposArmazenamento": ["SSD", "HDD", "NVMe", "SAS", "SATA"],
        "SistemasOperacionais": ["Windows 10", "Windows 11", "Ubuntu", "CentOS", "macOS", "Linux"]
    }
    
    col = 1
    for category, values in validation_data.items():
        ws_validacoes.cell(row=1, column=col).value = category
        ws_validacoes.cell(row=1, column=col).font = HEADER_FONT
        ws_validacoes.cell(row=1, column=col).fill = HEADER_FILL
        
        for idx, value in enumerate(values, 2):
            ws_validacoes.cell(row=idx, column=col).value = value
        col += 1
    
    set_column_width(ws_validacoes, {chr(64 + i): 18 for i in range(1, len(validation_data) + 1)})
    
    # ===== ABA 3: DASHBOARD =====
    ws_dashboard = wb.create_sheet("Dashboard")
    
    ws_dashboard['A1'].value = "DASHBOARD - INVENTÁRIO DE HARDWARE"
    ws_dashboard['A1'].font = Font(bold=True, size=14, color="003366")
    ws_dashboard['A1'].alignment = CENTER_ALIGNMENT
    ws_dashboard.merge_cells('A1:D1')
    
    ws_dashboard['A3'].value = "KPIs E MÉTRICAS"
    ws_dashboard['A3'].font = Font(bold=True, size=12)
    
    ws_dashboard['A5'].value = "Total de Ativos:"
    ws_dashboard['B5'].value = '=COUNTA(Hardware!A2:A1000)-1'
    ws_dashboard['B5'].font = Font(bold=True, size=11, color="003366")
    
    ws_dashboard['A6'].value = "Ativos Ativos:"
    ws_dashboard['B6'].value = '=COUNTIF(Hardware!S2:S1000,"Ativo")'
    ws_dashboard['B6'].font = Font(bold=True, size=11)
    
    ws_dashboard['A7'].value = "Ativos em Manutenção:"
    ws_dashboard['B7'].value = '=COUNTIF(Hardware!S2:S1000,"Manutenção")'
    ws_dashboard['B7'].font = Font(bold=True, size=11)
    
    ws_dashboard['A8'].value = "Ativos Descartados:"
    ws_dashboard['B8'].value = '=COUNTIF(Hardware!S2:S1000,"Descartado")'
    ws_dashboard['B8'].font = Font(bold=True, size=11)
    
    ws_dashboard['A10'].value = "INSTRUÇÕES:"
    ws_dashboard['A10'].font = Font(bold=True, size=11)
    ws_dashboard['A11'].value = "1. Adicione dados na aba 'Hardware' com informações dos equipamentos"
    ws_dashboard['A12'].value = "2. Use as validações da aba 'Validações' para preenchimento de listas"
    ws_dashboard['A13'].value = "3. Os KPIs acima são atualizados automaticamente"
    ws_dashboard['A14'].value = "4. Mantenha o formato dos dados para o funcionamento correto das fórmulas"
    
    set_column_width(ws_dashboard, {'A': 40, 'B': 20, 'C': 20, 'D': 20})
    
    wb.save('excel/template-inventario-hardware.xlsx')
    print("✓ template-inventario-hardware.xlsx criado com sucesso")

def create_template_licencas_software():
    """Create template-licencas-software.xlsx"""
    wb = Workbook()
    
    # ===== ABA 1: LICENÇAS =====
    ws_licencas = wb.active
    ws_licencas.title = "Licenças"
    
    headers = [
        "ID_Licenca", "Software", "Versao", "Fabricante", "Tipo_Licenca",
        "Quantidade_Adquirida", "Quantidade_Utilizada", "Licencas_Disponiveis",
        "Chave_Serial", "Data_Compra", "Data_Validade", "Valor_Unitario",
        "Valor_Total", "Status_Licenca", "Fornecedor", "Nota_Fiscal", "Observacoes"
    ]
    
    format_header_row(ws_licencas, headers)
    
    # Example data rows
    example_data = [
        [
            "LIC-001", "Microsoft Office", "2021", "Microsoft", "Volumen",
            50, 45, "=F2-G2", "XX-XXXX-XXXX-XXXX-XXXX",
            datetime(2023, 1, 15), datetime(2024, 1, 15), 150.00,
            "=F2*L2", "=IF(K2<TODAY(),'Expirada','Ativa')",
            "Softwares Brasil", "NF-001234", "Licenças corporativas"
        ],
        [
            "LIC-002", "AutoCAD", "2024", "Autodesk", "Perpetua",
            10, 8, "=F3-G3", "YY-YYYY-YYYY-YYYY-YYYY",
            datetime(2023, 6, 20), datetime(2026, 6, 20), 2500.00,
            "=F3*L3", "=IF(K3<TODAY(),'Expirada','Ativa')",
            "Tech Solutions", "NF-005678", "Renovação anual"
        ]
    ]
    
    for row_idx, row_data in enumerate(example_data, 2):
        format_data_row(ws_licencas, row_idx, row_data, alternate_color=(row_idx % 2 == 0))
    
    # Format specific columns
    ws_licencas.column_dimensions['J'].number_format = 'dd/mm/yyyy'  # Data_Compra
    ws_licencas.column_dimensions['K'].number_format = 'dd/mm/yyyy'  # Data_Validade
    ws_licencas.column_dimensions['L'].number_format = 'R$ #,##0.00'  # Valor_Unitario
    ws_licencas.column_dimensions['M'].number_format = 'R$ #,##0.00'  # Valor_Total
    
    column_widths_lic = {
        'A': 12, 'B': 18, 'C': 10, 'D': 15, 'E': 15, 'F': 16, 'G': 15, 'H': 15,
        'I': 20, 'J': 14, 'K': 14, 'L': 14, 'M': 14, 'N': 14, 'O': 15, 'P': 15, 'Q': 20
    }
    set_column_width(ws_licencas, column_widths_lic)
    freeze_panes(ws_licencas)
    
    # ===== ABA 2: VALIDAÇÕES =====
    ws_validacoes = wb.create_sheet("Validações")
    
    validation_data = {
        "Tipos_Licenca": ["Volumen", "Perpetua", "Subscricao", "Trial", "Freeware", "Open Source"],
        "Status": ["Ativa", "Expirada", "Suspensa", "Renovação Pendente"],
        "Fabricantes": ["Microsoft", "Autodesk", "Adobe", "JetBrains", "VMware", "Oracle"]
    }
    
    col = 1
    for category, values in validation_data.items():
        ws_validacoes.cell(row=1, column=col).value = category
        ws_validacoes.cell(row=1, column=col).font = HEADER_FONT
        ws_validacoes.cell(row=1, column=col).fill = HEADER_FILL
        
        for idx, value in enumerate(values, 2):
            ws_validacoes.cell(row=idx, column=col).value = value
        col += 1
    
    set_column_width(ws_validacoes, {'A': 20, 'B': 20, 'C': 20})
    
    wb.save('excel/template-licencas-software.xlsx')
    print("✓ template-licencas-software.xlsx criado com sucesso")

def create_template_manutencao():
    """Create template-manutencao.xlsx"""
    wb = Workbook()
    
    # ===== ABA 1: MANUTENÇÕES =====
    ws_manutencao = wb.active
    ws_manutencao.title = "Manutenções"
    
    headers = [
        "ID_Manutencao", "ID_Ativo", "Tipo_Ativo", "Data_Manutencao",
        "Tipo_Manutencao", "Problema_Relatado", "Solucao_Aplicada",
        "Tecnico_Responsavel", "Custo", "Status", "Tempo_Parada_Horas", "Observacoes"
    ]
    
    format_header_row(ws_manutencao, headers)
    
    # Example data rows
    example_data = [
        [
            "MNT-001", "HW-001", "Desktop", datetime(2024, 1, 10),
            "Preventiva", "Limpeza interna", "Limpeza de ventiladores e dissipadores",
            "Técnico Carlos", 150.00, "Concluído", 0.5, "Manutenção rotineira preventiva"
        ],
        [
            "MNT-002", "HW-003", "Servidor", datetime(2024, 1, 8),
            "Corretiva", "Aquecimento excessivo", "Substituição de pasta térmica e ventiladores",
            "Técnico Roberto", 800.00, "Concluído", 4.0, "Servidor retornou ao normal"
        ]
    ]
    
    for row_idx, row_data in enumerate(example_data, 2):
        format_data_row(ws_manutencao, row_idx, row_data, alternate_color=(row_idx % 2 == 0))
    
    # Format specific columns
    ws_manutencao.column_dimensions['D'].number_format = 'dd/mm/yyyy'  # Data_Manutencao
    ws_manutencao.column_dimensions['I'].number_format = 'R$ #,##0.00'  # Custo
    
    column_widths_mnt = {
        'A': 12, 'B': 12, 'C': 12, 'D': 14, 'E': 14, 'F': 25, 'G': 25,
        'H': 18, 'I': 12, 'J': 12, 'K': 15, 'L': 25
    }
    set_column_width(ws_manutencao, column_widths_mnt)
    freeze_panes(ws_manutencao)
    
    # ===== ABA 2: VALIDAÇÕES =====
    ws_validacoes = wb.create_sheet("Validações")
    
    validation_data = {
        "Tipos_Ativo": ["Desktop", "Notebook", "Servidor", "Impressora", "Switch", "Roteador"],
        "Tipos_Manutencao": ["Preventiva", "Corretiva", "Adaptativa", "Preditiva"],
        "Status": ["Pendente", "Em Andamento", "Concluído", "Cancelado"],
        "Tecnicos": ["Técnico Carlos", "Técnico Roberto", "Técnico Ana", "Técnico Paulo"]
    }
    
    col = 1
    for category, values in validation_data.items():
        ws_validacoes.cell(row=1, column=col).value = category
        ws_validacoes.cell(row=1, column=col).font = HEADER_FONT
        ws_validacoes.cell(row=1, column=col).fill = HEADER_FILL
        
        for idx, value in enumerate(values, 2):
            ws_validacoes.cell(row=idx, column=col).value = value
        col += 1
    
    set_column_width(ws_validacoes, {'A': 18, 'B': 18, 'C': 14, 'D': 18})
    
    wb.save('excel/template-manutencao.xlsx')
    print("✓ template-manutencao.xlsx criado com sucesso")

def create_dashboard_excel_exemplo():
    """Create dashboard-excel-exemplo.xlsx with sample data and visualizations"""
    wb = Workbook()
    
    # ===== ABA 1: DASHBOARD =====
    ws_dashboard = wb.active
    ws_dashboard.title = "Dashboard"
    
    # Title
    ws_dashboard['A1'].value = "DASHBOARD DE GESTÃO DE INVENTÁRIO"
    ws_dashboard['A1'].font = Font(bold=True, size=16, color="FFFFFF")
    ws_dashboard['A1'].fill = PatternFill(start_color="003366", end_color="003366", fill_type="solid")
    ws_dashboard['A1'].alignment = CENTER_ALIGNMENT
    ws_dashboard.merge_cells('A1:F1')
    ws_dashboard.row_dimensions[1].height = 25
    
    # Date
    ws_dashboard['A2'].value = f"Atualizado em: {datetime.now().strftime('%d/%m/%Y')}"
    ws_dashboard['A2'].font = Font(italic=True, size=10)
    ws_dashboard.merge_cells('A2:F2')
    
    # ===== KPI SECTION =====
    ws_dashboard['A4'].value = "INDICADORES PRINCIPAIS (KPIs)"
    ws_dashboard['A4'].font = Font(bold=True, size=12, color="FFFFFF")
    ws_dashboard['A4'].fill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")
    ws_dashboard.merge_cells('A4:F4')
    
    kpi_labels = ["Total de Ativos", "Ativos Ativos", "Taxa de Utilização", "Valor Total"]
    kpi_values = ["25", "23", "92%", "R$ 52.500,00"]
    kpi_colors = ["4472C4", "70AD47", "FFC000", "C5504B"]
    
    col = 1
    for idx, (label, value, color) in enumerate(zip(kpi_labels, kpi_values, kpi_colors)):
        row = 5
        cell_label = ws_dashboard.cell(row=row, column=col)
        cell_label.value = label
        cell_label.font = Font(bold=True, size=10)
        cell_label.alignment = CENTER_ALIGNMENT
        cell_label.border = Border(
            bottom=Side(style='thin', color=color),
            left=Side(style='thin'),
            right=Side(style='thin'),
            top=Side(style='thin')
        )
        
        cell_value = ws_dashboard.cell(row=row+1, column=col)
        cell_value.value = value
        cell_value.font = Font(bold=True, size=14, color=color)
        cell_value.alignment = CENTER_ALIGNMENT
        cell_value.border = Border(
            left=Side(style='thin'),
            right=Side(style='thin'),
            bottom=Side(style='thin')
        )
        
        col += 1
    
    # ===== HARDWARE SAMPLE DATA SECTION =====
    ws_dashboard['A9'].value = "AMOSTRA DE DADOS - HARDWARE"
    ws_dashboard['A9'].font = Font(bold=True, size=11, color="FFFFFF")
    ws_dashboard['A9'].fill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")
    ws_dashboard.merge_cells('A9:F9')
    
    hw_headers = ["ID", "Tipo", "Marca", "Modelo", "Status", "Departamento"]
    format_header_row(ws_dashboard, hw_headers, start_row=10)
    
    hw_sample_data = [
        ["HW-001", "Desktop", "Dell", "OptiPlex 7090", "Ativo", "TI"],
        ["HW-002", "Notebook", "Lenovo", "ThinkPad X13", "Ativo", "Gerência"],
        ["HW-003", "Servidor", "HP", "ProLiant DL380", "Ativo", "TI"],
        ["HW-004", "Impressora", "HP", "LaserJet Pro", "Ativo", "Administrativo"],
        ["HW-005", "Switch", "Cisco", "Catalyst 2960", "Manutenção", "TI"]
    ]
    
    for row_idx, row_data in enumerate(hw_sample_data, 11):
        format_data_row(ws_dashboard, row_idx, row_data, alternate_color=(row_idx % 2 == 0))
    
    # ===== STATISTICS SECTION =====
    ws_dashboard['A17'].value = "ESTATÍSTICAS"
    ws_dashboard['A17'].font = Font(bold=True, size=11, color="FFFFFF")
    ws_dashboard['A17'].fill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")
    ws_dashboard.merge_cells('A17:F17')
    
    ws_dashboard['A19'].value = "Distribuição por Tipo:"
    ws_dashboard['A19'].font = Font(bold=True)
    ws_dashboard['A20'].value = "Desktop"
    ws_dashboard['B20'].value = 8
    ws_dashboard['A21'].value = "Notebook"
    ws_dashboard['B21'].value = 12
    ws_dashboard['A22'].value = "Servidor"
    ws_dashboard['B22'].value = 2
    ws_dashboard['A23'].value = "Outros"
    ws_dashboard['B23'].value = 3
    
    # ===== INSTRUCTIONS SECTION =====
    ws_dashboard['D19'].value = "INSTRUÇÕES DE USO:"
    ws_dashboard['D19'].font = Font(bold=True, size=11, color="003366")
    
    instructions = [
        "1. Este dashboard apresenta uma visão geral do inventário",
        "2. Os KPIs são atualizados automaticamente com base nos dados",
        "3. Use as outras abas para consultar dados detalhados",
        "4. Mantenha os dados sempre atualizados para relatórios precisos",
        "5. Para gráficos, considere usar o Excel Charts ou Power BI"
    ]
    
    for idx, instruction in enumerate(instructions, 20):
        ws_dashboard[f'D{idx}'].value = instruction
        ws_dashboard[f'D{idx}'].alignment = LEFT_ALIGNMENT
        ws_dashboard[f'D{idx}'].font = Font(size=9)
    
    set_column_width(ws_dashboard, {
        'A': 18, 'B': 15, 'C': 15, 'D': 35, 'E': 15, 'F': 15
    })
    
    # ===== ABA 2: DADOS HARDWARE =====
    ws_hardware = wb.create_sheet("Dados Hardware")
    
    hw_headers_full = [
        "ID_Ativo", "Tipo", "Marca", "Modelo", "Numero_Serie",
        "Processador", "RAM_GB", "Armazenamento_GB", "Data_Aquisicao",
        "Valor_Aquisicao", "Departamento", "Usuario", "Status"
    ]
    
    format_header_row(ws_hardware, hw_headers_full)
    
    hw_full_data = [
        ["HW-001", "Desktop", "Dell", "OptiPlex 7090", "R123456789", "Intel i7-11700", 16, 512, datetime(2023, 6, 15), 4500.00, "TI", "João Silva", "Ativo"],
        ["HW-002", "Notebook", "Lenovo", "ThinkPad X13", "N987654321", "Intel i5-1135G7", 8, 256, datetime(2023, 9, 22), 3200.00, "Gerência", "Maria Santos", "Ativo"],
        ["HW-003", "Servidor", "HP", "ProLiant DL380", "S654321098", "Intel Xeon Gold", 128, 2048, datetime(2022, 3, 10), 25000.00, "TI", "Carlos Oliveira", "Ativo"],
        ["HW-004", "Impressora", "HP", "LaserJet Pro", "P111222333", "N/A", 0, 0, datetime(2023, 1, 5), 2100.00, "Administrativo", "Ana Costa", "Ativo"],
        ["HW-005", "Switch", "Cisco", "Catalyst 2960", "S445566778", "N/A", 0, 0, datetime(2021, 12, 1), 3500.00, "TI", "Carlos Oliveira", "Manutenção"],
        ["HW-006", "Notebook", "Apple", "MacBook Pro", "M456789012", "Apple M1", 16, 512, datetime(2023, 11, 3), 8500.00, "Design", "Pedro Dias", "Ativo"],
        ["HW-007", "Desktop", "Lenovo", "ThinkCentre", "R234567890", "AMD Ryzen 5", 8, 256, datetime(2023, 7, 18), 2800.00, "Financeiro", "Laura Silva", "Ativo"]
    ]
    
    for row_idx, row_data in enumerate(hw_full_data, 2):
        format_data_row(ws_hardware, row_idx, row_data, alternate_color=(row_idx % 2 == 0))
    
    ws_hardware.column_dimensions['I'].number_format = 'dd/mm/yyyy'
    ws_hardware.column_dimensions['J'].number_format = 'R$ #,##0.00'
    
    column_widths_hw2 = {
        'A': 12, 'B': 12, 'C': 12, 'D': 15, 'E': 15, 'F': 18, 'G': 10, 'H': 15,
        'I': 14, 'J': 14, 'K': 14, 'L': 15, 'M': 12
    }
    set_column_width(ws_hardware, column_widths_hw2)
    freeze_panes(ws_hardware)
    
    # ===== ABA 3: ANÁLISE =====
    ws_analise = wb.create_sheet("Análise")
    
    ws_analise['A1'].value = "ANÁLISE E RELATÓRIOS"
    ws_analise['A1'].font = Font(bold=True, size=14, color="FFFFFF")
    ws_analise['A1'].fill = PatternFill(start_color="003366", end_color="003366", fill_type="solid")
    ws_analise['A1'].alignment = CENTER_ALIGNMENT
    ws_analise.merge_cells('A1:D1')
    ws_analise.row_dimensions[1].height = 20
    
    ws_analise['A3'].value = "Contagem por Tipo de Ativo"
    ws_analise['A3'].font = Font(bold=True, size=11)
    
    analysis_headers = ["Tipo de Ativo", "Quantidade", "Percentual"]
    format_header_row(ws_analise, analysis_headers, start_row=4)
    
    analysis_data = [
        ["Desktop", 2, "=B5/SUM($B$5:$B$9)"],
        ["Notebook", 2, "=B6/SUM($B$5:$B$9)"],
        ["Servidor", 1, "=B7/SUM($B$5:$B$9)"],
        ["Impressora", 1, "=B8/SUM($B$5:$B$9)"],
        ["Outros", 1, "=B9/SUM($B$5:$B$9)"]
    ]
    
    for row_idx, row_data in enumerate(analysis_data, 5):
        format_data_row(ws_analise, row_idx, row_data, alternate_color=(row_idx % 2 == 0))
    
    # Format percentage column
    for row in range(5, 10):
        ws_analise.cell(row=row, column=3).number_format = '0%'
    
    ws_analise['A11'].value = "Contagem por Status"
    ws_analise['A11'].font = Font(bold=True, size=11)
    
    status_headers = ["Status", "Quantidade"]
    format_header_row(ws_analise, status_headers, start_row=12)
    
    status_data = [
        ["Ativo", 6],
        ["Inativo", 0],
        ["Manutenção", 1]
    ]
    
    for row_idx, row_data in enumerate(status_data, 13):
        format_data_row(ws_analise, row_idx, row_data, alternate_color=(row_idx % 2 == 0))
    
    set_column_width(ws_analise, {'A': 25, 'B': 15, 'C': 15})
    
    wb.save('excel/dashboard-excel-exemplo.xlsx')
    print("✓ dashboard-excel-exemplo.xlsx criado com sucesso")

def main():
    """Main function to create all templates."""
    print("\n" + "="*60)
    print("Criando templates Excel para Inventário de Parque Tecnológico")
    print("="*60 + "\n")
    
    try:
        os.chdir('/home/runner/work/inventario-parque-tecnologico/inventario-parque-tecnologico')
        
        print("Criando templates...\n")
        create_template_inventario_hardware()
        create_template_licencas_software()
        create_template_manutencao()
        create_dashboard_excel_exemplo()
        
        print("\n" + "="*60)
        print("✓ Todos os templates foram criados com sucesso!")
        print("="*60)
        print("\nArquivos criados em excel/:")
        print("  1. template-inventario-hardware.xlsx")
        print("  2. template-licencas-software.xlsx")
        print("  3. template-manutencao.xlsx")
        print("  4. dashboard-excel-exemplo.xlsx")
        print("\n" + "="*60 + "\n")
        
    except Exception as e:
        print(f"\n✗ Erro ao criar templates: {str(e)}")
        import traceback
        traceback.print_exc()
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())
