Function Get-DiskSpace {
    param(
        [string]$Drive  # Accepts a drive letter as a parameter
    )

    # Retrieve information about the specified drive
    $diskInfo = Get-WmiObject -Class Win32_LogicalDisk -ComputerName LOCALHOST | 
                Where-Object { $_.DeviceID -eq $Drive -and $_.DriveType -eq 3 }

    # Calculate and display the free space in GB
    $freeSpaceGB = [int]($diskInfo.FreeSpace / 1GB)
    Write-Host "Free space on drive $Drive $freeSpaceGB GB"
}

# Example usage
Get-DiskSpace -Drive "D:"
