## 1. PowerShell Basics
```Cmdlets:``` PowerShell commands follow the verb-noun pattern.
```Get-Help:``` Displays help for commands (use -Online for more detailed help).
```Get-Command:``` Lists available commands.
```Get-Command -Name <cmdlet>:``` Provides details about a specific cmdlet.
```Get-Alias:``` Shows aliases for commands (e.g., ls for Get-ChildItem).

## 2. Variables
Declare a variable: ```$var = "Hello"```
Arrays: ```$arr = @(1, 2, 3)```
Hash Tables: ```$hash = @{key1 = "value1"; key2 = "value2"}```

## 3. Working with Files and Directories
List directory contents: ```Get-ChildItem (alias ls)```
Change directory: ```Set-Location <path> (alias cd)```
Create a directory: ```New-Item -Path <path> -ItemType Directory```
Copy files: ```Copy-Item -Path <source> -Destination <dest>```
Move files: ```Move-Item -Path <source> -Destination <dest>```
Delete files: ```Remove-Item -Path <file> (alias del or rm)```
Reading from a file: ```Get-Content <file>```
Writing to a file: ```Set-Content -Path <file> -Value <content>```

## 4. Pipelines and Filtering
Pipe output: ```Command1 | Command2```
Filtering: ```Get-Process | Where-Object {$_.CPU -gt 100}```
Selecting properties: ```Get-Process | Select-Object Name, CPU```
Sorting: ```Get-Process | Sort-Object CPU```

## 5. Loops and Conditionals
If statement:
```
if ($var -eq 5) {
    Write-Output "Var is 5"
}

```
ForEach loop:
```
$array = @(1, 2, 3)
foreach ($item in $array) {
    Write-Output $item
}
```
While loop:
```
$i = 0
while ($i -lt 5) {
    Write-Output $i
    $i++
}

```
## 6. Working with Processes
Get running processes: ```Get-Process (alias ps)```
Stop a process: ```Stop-Process -Name <process-name>```
## 7. System Information
Get system information: ```Get-ComputerInfo```
Get network configuration: ```Get-NetIPAddress```
List services: ```Get-Service```
Start and Stop:
```
Start-Service -Name <service-name>
Stop-Service -Name <service-name>
```
## 8. Users and Permissions
List users: ```Get-LocalUser```
Create a user: ```New-LocalUser -Name <username>```
Change permissions: ```Set-ACL```

## 9. Scripting
Create a script: Write commands in a ```.ps1``` file.
Run a script: ```.\script.ps1```
Execution policy: ```Set-ExecutionPolicy RemoteSigned``` (to allow scripts to run)

## 10. Remote Commands
```Invoke-Command -ComputerName <name> -ScriptBlock { Get-Process }```

## 11. Error Handling
```
try {
    Get-Item "C:\nonexistent"
} catch {
    Write-Output "An error occurred: $_"
}
```

## 12. Common Comparison Operators
Equal: ```-eq```
Not equal: ```-ne```
Greater than: ```-gt```
Less than: ```-lt```
Contains: ```-contains```
Like (wildcards): ```-like "*pattern*"```

## Example Commands
Get disk information: ````Get-PSDrive```
Get services starting with "Win": 
```
Get-Service | Where-Object { $_.Name -like "Win*" }
```
List processes consuming more than 100MB of memory: 
```
Get-Process | Where-Object { $_.WS -gt 100MB }
```

