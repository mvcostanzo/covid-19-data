cd "C:\Michael_Docs\Git Repositories\NY Times COVID Data\NYC COVID Details"
git fetch --progress --verbose upstream
git merge upstream/master
git push --progress --verbose origin refs/heads/master:refs/heads/master --tags


cd "C:\Michael_Docs\Git Repositories\NY Times COVID Data\Python"
python NYCCleanup.py


cd "C:\Michael_Docs\Git Repositories\NY Times COVID Data"
git submodule update --init --recursive -- "C:\Michael_Docs\Git Repositories\NY Times COVID Data\NYC COVID Details"
git fetch --progress --verbose upstream
git merge upstream/master
git commit -a --file="C:/Michael_Docs/Git Repositories/NY Times COVID Data/.git/COMMITMESSAGE"
git push --progress --verbose origin refs/heads/master:refs/heads/master --tags
