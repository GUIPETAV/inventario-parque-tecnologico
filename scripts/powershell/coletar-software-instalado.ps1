<#
.SYNOPSIS
    Coleta lista de software instalado
.DESCRIPTION
    Lista todos os programas instalados no computador
#>

Write-Host "Coletando software instalado..." -ForegroundColor Yellow

$SoftwareList = @()

# Método 1: Registro (64-bit)
$SoftwareList += Get-ItemProperty HKLM:\Software\Microsoft\Windows\CurrentVersion\Uninstall\* |
    Where-Object { $_.DisplayName } |
    Select-Object DisplayName, DisplayVersion, Publisher, InstallDate

# Método 2: Registro (32-bit em sistema 64-bit)
if (Test-Path 'HKLM:\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall\*') {
    $SoftwareList += Get-ItemProperty HKLM:\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall\* |
        Where-Object { $_.DisplayName } |
        Select-Object DisplayName, DisplayVersion, Publisher, InstallDate
}

# Remover duplicatas e ordenar
$SoftwareList = $SoftwareList | 
    Sort-Object DisplayName -Unique |
    Select-Object @{Name='Software';Expression={$_.DisplayName}},
                  @{Name='Versao';Expression={$_.DisplayVersion}},
                  @{Name='Fabricante';Expression={$_.Publisher}},
                  @{Name='Data_Instalacao';Expression={$_.InstallDate}},
                  @{Name='Computador';Expression={$env:COMPUTERNAME}},
                  @{Name='Data_Coleta';Expression={(Get-Date).ToString("yyyy-MM-dd")}}

# Exportar para CSV
$SoftwareList | Export-Csv -Path "software_$($env:COMPUTERNAME).csv" -NoTypeInformation -Encoding UTF8

Write-Host "Total de programas encontrados: $($SoftwareList.Count)" -ForegroundColor Green
Write-Host "Arquivo salvo: software_$($env:COMPUTERNAME).csv" -ForegroundColor Green

# Exibir primeiros 10
$SoftwareList | Select-Object -First 10 | Format-Table -AutoSize
