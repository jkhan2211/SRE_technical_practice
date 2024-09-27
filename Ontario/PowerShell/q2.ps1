$docPath = [System.IO.Path]::Combine($env:USERPROFILE, "Documents", "TestFile.txt")
New-Item -Path $docPath -ItemType File -Force
Set-Content -Path $docPath -Value 'This is a test file'