# Function to install Python
function Install-Python {
    Write-Host "Installing Python..." -ForegroundColor Green  # Green color for success message
    # Download the latest Python installer
    Invoke-WebRequest -Uri "https://www.python.org/ftp/python/3.12.0/python-3.12.0-amd64.exe" -OutFile "python-installer.exe"
    # Run the Python installer silently
    Start-Process -FilePath "python-installer.exe" -ArgumentList "/quiet", "PrependPath=1" -Wait
    # Clean up the installer
    Remove-Item "python-installer.exe"
    Write-Host "Python installed successfully." -ForegroundColor Green
	
    Write-Host "Adding Python to the PATH..." -ForegroundColor Yellow  # Yellow color for informational message
    [Environment]::SetEnvironmentVariable("Path", "$($env:Path);C:\Users\Administrator\AppData\Local\Programs\Python\Python312\python.exe", [System.EnvironmentVariableTarget]::Machine)
    [System.Environment]::SetEnvironmentVariable("Path", [System.Environment]::GetEnvironmentVariable("Path", [System.EnvironmentVariableTarget]::Machine), [System.EnvironmentVariableTarget]::Process)
}

# Function to install pip
function Install-pip {
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

# Function to execute the Python script
function Run-Script {
    Write-Host "Running the Python script..." -ForegroundColor Cyan  # Cyan color for script execution message
    python traffic.py  # Replace script_name.py with your script filename
}

# Main script
Install-Python
Install-pip
Install-Packages
Run-Script
