Get-Service | Where-Object {$_.Status -eq "Stopped"}  |
    Export-Csv -Path .\WmiData.csv -NoTypeInformation
Import-Csv -Path .\WmiData.csv