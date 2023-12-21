# Install chocolatey
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))

# Install python
choco install python --version 3.12.1 -y

# Install pip
choco install pip -y

# Install selenium
pip install selenium

# Download geckodriver
Invoke-WebRequest -Uri "https://github.com/mozilla/geckodriver/releases/download/v0.33.0/geckodriver-v0.33.0-win64.zip" -OutFile "geckodriver.zip"

# Extract the archive
Expand-Archive -Path geckodriver.zip -DestinationPath .

# Add geckodriver to PATH
$env:Path += ";$pwd"

# Remove the archive
Remove-Item geckodriver.zip
