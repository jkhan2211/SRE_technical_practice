o create a solid PowerShell assessment for evaluating proficiency in the language, you can include a variety of tasks focusing on core skills like scripting, automation, working with objects, and managing Windows services and systems. Here's a suggested PowerShell assessment test:

PowerShell Assessment Test:

Section 1: Basic Scripting (20 points)
1. Write a script that prints "Hello, World!" to the console.
(5 points)

```
Write-Host "Hello, World!"
```

2. Write a PowerShell script to create a text file named TestFile.txt in the current user's Documents folder, and write the string "This is a test file" into it.
(5 points)

```
$docPath = [System.IO.Path]::Combine($env:USERPROFILE, "Documents", "TestFile.txt")
New-Item -Path $docPath -ItemType File -Force
Set-Content -Path $docPath -Value 'This is a test file'
```

3. Write a script that takes an array of numbers and outputs only the even numbers.
(10 points)
```
$numbers = @(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
for ($i = 0; $i -lt $numbers.Length; $i++) {
    if ($numbers[$i] % 2 -eq 0) {  # Check if the number is even
        Write-Host $numbers[$i]
    }
}
```
----------------------------------------------------------------------------------------
Section 2: Working with Cmdlets (30 points)
4. Get a list of all processes running on the system that are consuming more than 100 MB of memory.
(10 points)
```
Get-Process | Where-Object {$_.WorkingSet64 -gt 100MB} | Select-Object Name, Id, WorkingSet64
```

5. Retrieve the 5 most recent entries from the Application event log.
(10 points)
```
Get-EventLog -LogName Application -newest 5
```

6. Write a command that fetches all services on the system that are in the 'Stopped' state and exports the list to a CSV file.
(10 points)

```
Get-Service | Where-Object {$_.Status -eq "Stopped"}  |
    Export-Csv -Path .\WmiData.csv -NoTypeInformation
```

------------------------------------------------------------------------------------------------------
Section 3: Functions and Error Handling (30 points)
7. Create a PowerShell function named Get-DiskSpace that accepts a drive letter as a parameter and returns the free space available on the drive.
(15 points)

```
Function Get-DiskSpace()
{   
    param(
        [string]$Drive
    )

        # Retrieve information about the specified drive
    $diskInfo = Get-WmiObject -Class Win32_LogicalDisk -ComputerName LOCALHOST | Where-Object { $_.DeviceID -eq $Drive -and $_.DriveType -eq 3 }
     $freeSpaceGB = [int]($diskInfo.FreeSpace / 1GB)
        Write-Host "Free space on drive $Drive $freeSpaceGB GB"


}

#Write-Host Get-WmiObject -Class Win32_LogicalDisk -ComputerName LOCALHOST | ? {$_. Drive -eq 3} | select DeviceID, {[int]($_.Size /1GB)}, {[int]($_.FreeSpace /1GB)}
Get-DiskSpace -Drive "D:"

```
8. Modify the Get-DiskSpace function to include error handling. If the drive letter is invalid, the function should output an error message.
(15 points)

```
Function Get-DiskSpace {
    param(
        [string]$Drive  # Accepts a drive letter as a parameter
    )

    # Retrieve information about the specified drive
    $diskInfo = Get-WmiObject -Class Win32_LogicalDisk -ComputerName LOCALHOST | 
                Where-Object { $_.DeviceID -eq $Drive -and $_.DriveType -eq 3 }

    if ($diskInfo) {
         # Calculate and display the free space in GB
        $freeSpaceGB = [int]($diskInfo.FreeSpace / 1GB)
        Write-Host "Free space on drive $Drive $freeSpaceGB GB"
    } else {
        Write-Host "Drive $Drive does not exist, please check"
    }
    
}

# Example usage
Get-DiskSpace -Drive "K:"
```

----------------------------------------------------------------------------------------------------------

Section 4: Automation & System Administration (20 points)
9. Write a PowerShell script that automates the creation of user accounts in Active Directory from a CSV file containing fields FirstName, LastName, Username, and Password.
(10 points)

10. Write a PowerShell script that checks if a specific Windows service (e.g., Spooler) is running. If it's not running, start the service. If it is running, restart the service.
(10 points)







Scoring Guide:
Basic Scripting (20 points): Test basic understanding of PowerShell syntax and script-writing abilities.
Cmdlets (30 points): Assess understanding of core cmdlets and ability to interact with system processes and logs.
Functions and Error Handling (30 points): Evaluate the ability to create reusable code and handle errors gracefully.
Automation (20 points): Test knowledge of automation, Active Directory management, and Windows services.
The total score is 100 points. You can modify the difficulty based on the candidate's experience level and the specific tasks your team handles.






