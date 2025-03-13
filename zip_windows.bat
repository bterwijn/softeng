@echo off
powershell -Command "Compress-Archive -Path * -DestinationPath softeng.zip -Force"
echo Files zipped successfully to softeng.zip
