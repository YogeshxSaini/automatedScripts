#!/bin/bash

# Update system packages
sudo apt update

# Install Python and pip
sudo apt install -y python3 python3-pip

# Install Selenium
pip3 install selenium

# Install Google Chrome
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb
sudo apt install -f

# Install dependencies for ChromeDriver
sudo apt install -y libglib2.0-0 libnss3 libgconf-2-4 libfontconfig1

# Download ChromeDriver
CHROME_DRIVER_VERSION=$(curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE)
wget https://chromedriver.storage.googleapis.com/$CHROME_DRIVER_VERSION/chromedriver_linux64.zip

# Unzip ChromeDriver
sudo apt install unzip
unzip chromedriver_linux64.zip

# Move ChromeDriver to a directory in your PATH
sudo mv chromedriver /usr/local/bin/

# Clean up downloaded files
rm chromedriver_linux64.zip google-chrome-stable_current_amd64.deb

# Display versions to verify installations
echo "Python version:"
python3 --version

echo "pip version:"
pip3 --version

echo "Selenium version:"
python3 -c "import selenium; print(selenium.__version__)"

echo "ChromeDriver version:"
chromedriver --version

echo "Google Chrome version:"
google-chrome --version
