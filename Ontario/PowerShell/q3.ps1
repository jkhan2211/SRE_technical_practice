$numbers = @(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
for ($i = 0; $i -lt $numbers.Length; $i++) {
    if ($numbers[$i] % 2 -eq 0) {  # Check if the number is even
        Write-Host $numbers[$i]
    }
}

