```
Get-Date
```
- to get current date

Check commands
```
Get-Command -Noun Date
```

### Variables
```
$my_string_variable = "Hello, World!"
```

Use a Variable
PS > $my_string_variable
Hello, World!

Variable reference allows us to use or manipulate variables. As shown above, referencing the variable my_string_variable we defined earlier in the PowerShell terminal prints the value we assigned to it.

User Input
Now that we can hold data using variables, we can look at a useful command that enables user input through the terminal.

PS > $my_input = Read-Host -Prompt "Enter a number"


#### Example
```
$name = "Junaid"
$age = Read-Host -Prompt "What is your age"

Write-Host "Hello, $name, you are $age!
```




