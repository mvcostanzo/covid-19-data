cd "C:\Michael_Docs\Git Repositories\NY Times COVID Data\NYC COVID Details"
git checkout master
git fetch --progress --verbose upstream
git merge upstream/master
git push --progress --verbose origin refs/heads/master:refs/heads/master --tags
git checkout master

cd "C:\Michael_Docs\Git Repositories\NY Times COVID Data\Python"
python NYCCleanup.py


cd "C:\Michael_Docs\Git Repositories\NY Times COVID Data"
git add "C:\Michael_Docs\Git Repositories\NY Times COVID Data\NYC COVID Details"
git add "C:\Michael_Docs\Git Repositories\NY Times COVID Data\NYC-counties.csv"
git commit -a --file="C:/Michael_Docs/Git Repositories/NY Times COVID Data/.git/COMMITMESSAGE"
git fetch --progress --verbose upstream
git merge upstream/master
git push --progress --verbose origin refs/heads/master:refs/heads/master --tags
