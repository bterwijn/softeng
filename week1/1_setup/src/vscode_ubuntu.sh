cd ~/Downloads
latest_code=$(ls -t code_*.deb | head -n 1) # get latest version
echo "installing file: $latest_code"
sudo dpkg -i $latest_code                   # install using Debian package manager
