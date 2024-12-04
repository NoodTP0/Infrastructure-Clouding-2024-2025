$ git config --global user.name "Yvan Ro"
$ git config --global user.email "yvr@biasc.com"
$ mkdir DevascExperiments
$ cd DevascExperiments
$ echo "# DevascExperiments" >> README.md
$ git init
$ git status
$ git add README.md
$ git commit -m "Created README.md for DevascExperiments"
$ git branch -M main
$ git remote add origin https://github.com/NoodTP0/Infrastructure-Clouding-2024-2025
$ git push -u origin main