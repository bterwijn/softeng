python3.13 -m venv %USERPROFILE%\py3.13venv          # create environment
& %USERPROFILE%\py3.13venv\Scripts\Activate.ps1      # activate environment
$backupFile = "$PROFILE.$(Get-Date -Format 'yyyyMMdd_HHmmss').bak"
cp $PROFILE $backupFile                              # backup profile
echo "& $env:USERPROFILE\py3.13venv\Scripts\Activate.ps1" >> $PROFILE # automate
