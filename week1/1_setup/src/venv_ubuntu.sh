python3.12 -m venv ~/py3.12venv                      # create environment
source ~/py3.12venv/bin/activate                     # activate environment
cp ~/.bashrc ~/.bashrc$(date +"%Y%m%d_%H%M%S")       # backup .bashrc
echo "source ~/py3.12venv/bin/activate" >> ~/.bashrc # auto activate environment
