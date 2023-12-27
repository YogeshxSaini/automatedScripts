# automatedScripts

```bash
Invoke-WebRequest -Uri 'https://github.com/YogeshxSaini/automatedScripts/raw/main/setup.ps1' -OutFile 'setup.ps1'; Invoke-WebRequest -Uri 'https://github.com/YogeshxSaini/automatedScripts/raw/main/windows.py' -OutFile 'windows.py'; Invoke-WebRequest -Uri 'https://github.com/YogeshxSaini/automatedScripts/raw/main/mobile.py' -OutFile 'mobile.py'; .\setup.ps1
```

<h2> Disable Antivirus </h2>

```bash
Set-MpPreference -DisableRealtimeMonitoring $true
```

<h2> Enable execution of scripts </h2>

```bash
Set-ExecutionPolicy -ExecutionPolicy Unrestricted
```

<h2> newSetup.ps1 </h2>

```bash
Invoke-WebRequest -Uri 'https://github.com/YogeshxSaini/automatedScripts/raw/main/newSetup.ps1' -OutFile 'newSetup.ps1'; .\newSetup.ps1
```

<h2> windows.py </h2>

```bash
Invoke-WebRequest -Uri 'https://github.com/YogeshxSaini/automatedScripts/raw/main/windows.py' -OutFile 'windows.py'; python windows.py
```

<h2> mobile.py </h2>

```bash
Invoke-WebRequest -Uri 'https://github.com/YogeshxSaini/automatedScripts/raw/main/mobile.py' -OutFile 'mobile.py'; python mobile.py
```

<h2> svip.py </h2>

```bash
Invoke-WebRequest -Uri 'https://github.com/YogeshxSaini/automatedScripts/raw/main/svip.py' -OutFile 'svip.py'; python svip.py
```
<h2> install_selenium.sh </h2>
```bash
bash <(curl -s https://raw.githubusercontent.com/YogeshxSaini/automatedScripts/main/install_selenium.sh)

<h2> Run on linux </h2>
python3 <(curl -s https://raw.githubusercontent.com/YogeshxSaini/automatedScripts/main/svip.py)


<h2> setup2.py </h2>

```bash
Invoke-WebRequest -Uri 'https://github.com/YogeshxSaini/automatedScripts/raw/main/setup2.ps1' -OutFile 'setup2.ps1'; .\setup2.ps1
```
