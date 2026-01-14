<#
.SYNOPSIS
    Exporta dados de inventário para Excel
.DESCRIPTION
    Consolida múltiplos arquivos CSV de inventário e exporta para Excel
.PARAMETER InputPath
    Caminho da pasta contendo os arquivos CSV
.PARAMETER OutputFile
    Nome do arquivo Excel de saída
.EXAMPLE
    .\exportar-para-excel.ps1 -InputPath "." -OutputFile "inventario-consolidado.xlsx"
#>

param(
    [Parameter(Mandatory=$false)]
    [string]$InputPath = ".",
    
    [Parameter(Mandatory=$false)]
    [string]$OutputFile = "inventario-consolidado.csv"
)

Write-Host "Exportando inventário para Excel..." -ForegroundColor Yellow

# Verificar se há arquivos de inventário
$ArquivosHardware = Get-ChildItem -Path $InputPath -Filter "inventario_*.csv"
$ArquivosSoftware = Get-ChildItem -Path $InputPath -Filter "software_*.csv"

if ($ArquivosHardware.Count -eq 0) {
    Write-Host "⚠️  Nenhum arquivo de inventário de hardware encontrado." -ForegroundColor Yellow
    Write-Host "Execute primeiro: .\coletar-inventario-hardware.ps1" -ForegroundColor Cyan
    exit
}

# Consolidar hardware
Write-Host "`nConsolidando arquivos de hardware..." -ForegroundColor Cyan
$DadosHardware = @()
foreach ($arquivo in $ArquivosHardware) {
    $dados = Import-Csv -Path $arquivo.FullName -Encoding UTF8
    $DadosHardware += $dados
}

Write-Host "✅ Total de registros de hardware: $($DadosHardware.Count)" -ForegroundColor Green

# Consolidar software (se existir)
if ($ArquivosSoftware.Count -gt 0) {
    Write-Host "`nConsolidando arquivos de software..." -ForegroundColor Cyan
    $DadosSoftware = @()
    foreach ($arquivo in $ArquivosSoftware) {
        $dados = Import-Csv -Path $arquivo.FullName -Encoding UTF8
        $DadosSoftware += $dados
    }
    Write-Host "✅ Total de registros de software: $($DadosSoftware.Count)" -ForegroundColor Green
}

# Exportar hardware consolidado
$ArquivoHardware = "hardware-" + $OutputFile
$DadosHardware | Export-Csv -Path $ArquivoHardware -NoTypeInformation -Encoding UTF8
Write-Host "`n✅ Hardware exportado para: $ArquivoHardware" -ForegroundColor Green

# Exportar software consolidado (se existir)
if ($ArquivosSoftware.Count -gt 0) {
    $ArquivoSoftwareOut = "software-" + $OutputFile
    $DadosSoftware | Export-Csv -Path $ArquivoSoftwareOut -NoTypeInformation -Encoding UTF8
    Write-Host "✅ Software exportado para: $ArquivoSoftwareOut" -ForegroundColor Green
}

Write-Host "`n📊 Resumo:" -ForegroundColor Cyan
Write-Host "   Computadores inventariados: $($DadosHardware.Count)" -ForegroundColor White
if ($ArquivosSoftware.Count -gt 0) {
    Write-Host "   Total de software encontrado: $($DadosSoftware.Count)" -ForegroundColor White
}

Write-Host "`n💡 Dica: Importe os arquivos CSV no Excel ou Power BI para análise." -ForegroundColor Yellow
Write-Host "   Use: Dados → Obter Dados → De Texto/CSV" -ForegroundColor Yellow
