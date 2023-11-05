# Function to check if Python is already installed
function Is-PythonInstalled {
    $pythonPath = Get-Command python -ErrorAction SilentlyContinue
    return $pythonPath -ne $null
}

# Function to install Python if it's not already installed
function Install-Python {
    if (Is-PythonInstalled) {
        Write-Host "Python is already installed. Skipping installation." -ForegroundColor Yellow
        return
    }

    Write-Host "Installing Python..." -ForegroundColor Green
    # Download the latest Python installer
    Invoke-WebRequest -Uri "https://www.python.org/ftp/python/3.12.0/python-3.12.0-amd64.exe" -OutFile "python-installer.exe"
    # Run the Python installer silently
    Start-Process -FilePath "python-installer.exe" -ArgumentList "/quiet", "PrependPath=1" -Wait
    # Clean up the installer
    Remove-Item "python-installer.exe"
    Write-Host "Python installed successfully." -ForegroundColor Green

    Write-Host "Adding Python to the PATH..." -ForegroundColor Yellow
    [Environment]::SetEnvironmentVariable("Path", "$($env:Path);C:\Users\Administrator\AppData\Local\Programs\Python\Python312\python.exe", [System.EnvironmentVariableTarget]::Machine)
    [System.Environment]::SetEnvironmentVariable("Path", [System.Environment]::GetEnvironmentVariable("Path", [System.EnvironmentVariableTarget]::Machine), [System.EnvironmentVariableTarget]::Process)
}

# Function to check if pip is already installed
function Is-PipInstalled {
    $pipPath = Get-Command pip -ErrorAction SilentlyContinue
    return $pipPath -ne $null
}

# Function to install pip if it's not already installed
function Install-pip {
    if (Is-PipInstalled) {
        Write-Host "pip is already installed. Skipping installation." -ForegroundColor Yellow
        return
    }

    Write-Host "Dowloading pip..." -ForegroundColor Yellow
    Invoke-WebRequest -Uri https://bootstrap.pypa.io/get-pip.py -OutFile get-pip.py
    Write-Host "Installing pip..." -ForegroundColor Yellow
    python get-pip.py
    Write-Host "pip installed successfully." -ForegroundColor Green
}

# Function to install required Python packages
function Install-Packages {
    Write-Host "Installing required Python packages..." -ForegroundColor Yellow
    pip install selenium
    Write-Host "Python packages installed successfully." -ForegroundColor Green
}

function Install-Driver {
    Write-Host "Installing chocolatey..." -ForegroundColor Yellow
    Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
    Write-Host "Chocolatey installed successfully." -ForegroundColor Green
    Write-Host "Installing Gecko Driver..." -ForegroundColor Yellow
    choco install selenium-gecko-driver
    Write-Host "Gecko Driver installed successfully." -ForegroundColor Green
}

# Function to execute the Python script
function Run-Script {
    Write-Host "Running the Python script..." -ForegroundColor Cyan
    python windows.py
    Write-Host "Python script executed successfully." -ForegroundColor Green
}

# Main script
Install-Python
Install-pip
Install-Packages
Install-Driver
Run-Script
