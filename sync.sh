# change directory to tokei directory (directory containing the sync script)
cd $( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

read -p "Enter commit message for COPPER changes:" project_commit_msg
git add --all .
git commit -m "$project_commit_msg"
git pull --rebase
git push

cd ../calliope
bash sync.sh