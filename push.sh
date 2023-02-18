git add .
git commit -m "update"
git branch -M master
git remote remove origin
git remote add origin git@github.com:meowjiao/meowthon.git
git push -u origin master