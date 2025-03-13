python3.13 -m venv ~/py3.13venv                      # create environment
source ~/py3.13venv/bin/activate                     # activate environment
cp ~/.zshrc ~/.zshrc$(date +"%Y%m%d_%H%M%S")         # backup .zshrc
echo "source ~/py3.13venv/bin/activate" >> ~/.zshrc  # auto activate environment
