<#
.SYNOPSIS
    Coleta informações de hardware do computador local
.DESCRIPTION
    Script para coletar dados de inventário de hardware incluindo:
    - Informações do sistema
    - Processador
    - Memória RAM
    - Discos
    - Sistema operacional
.EXAMPLE
    .\coletar-inventario-hardware.ps1
#>

# Coletar informações do computador
$ComputerInfo = Get-ComputerInfo

# Informações do sistema
$Sistema = @{
    NomeComputador = $env:COMPUTERNAME
    Fabricante = $ComputerInfo.CsManufacturer
    Modelo = $ComputerInfo.CsModel
    NumeroSerie = (Get-WmiObject -Class Win32_BIOS).SerialNumber
}

# Informações do processador
$Processador = Get-WmiObject -Class Win32_Processor | Select-Object -First 1
$InfoProcessador = @{
    Nome = $Processador.Name
    Nucleos = $Processador.NumberOfCores
    Threads = $Processador.NumberOfLogicalProcessors
}

# Informações de memória
$MemoriaTotal = [math]::Round((Get-WmiObject -Class Win32_ComputerSystem).TotalPhysicalMemory / 1GB, 2)

# Informações de disco
$Discos = Get-WmiObject -Class Win32_DiskDrive | ForEach-Object {
    @{
        Modelo = $_.Model
        Tamanho = [math]::Round($_.Size / 1GB, 2)
        Tipo = if ($_.MediaType -match "SSD") { "SSD" } else { "HDD" }
    }
}

# Informações do sistema operacional
$SO = Get-WmiObject -Class Win32_OperatingSystem
$InfoSO = @{
    Nome = $SO.Caption
    Versao = $SO.Version
    Arquitetura = $SO.OSArchitecture
    DataInstalacao = $SO.ConvertToDateTime($SO.InstallDate).ToString("yyyy-MM-dd")
}

# Criar objeto com todas as informações
$Inventario = [PSCustomObject]@{
    NomeComputador = $Sistema.NomeComputador
    Fabricante = $Sistema.Fabricante
    Modelo = $Sistema.Modelo
    NumeroSerie = $Sistema.NumeroSerie
    Processador = $InfoProcessador.Nome
    Nucleos = $InfoProcessador.Nucleos
    RAM_GB = $MemoriaTotal
    Disco_Tamanho_GB = ($Discos | Measure-Object -Property Tamanho -Sum).Sum
    Tipo_Disco = ($Discos[0].Tipo)
    SO = $InfoSO.Nome
    Versao_SO = $InfoSO.Versao
    Arquitetura = $InfoSO.Arquitetura
    Data_Coleta = (Get-Date).ToString("yyyy-MM-dd HH:mm:ss")
}

# Exibir resultado
$Inventario | Format-List

# Exportar para CSV
$Inventario | Export-Csv -Path "inventario_$($env:COMPUTERNAME).csv" -NoTypeInformation -Encoding UTF8

Write-Host "Inventário coletado e salvo em inventario_$($env:COMPUTERNAME).csv" -ForegroundColor Green
