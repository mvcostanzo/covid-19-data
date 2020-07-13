cd "C:\Michael_Docs\Git Repositories\NY Times COVID Data"
git fetch --progress --verbose upstream
git merge upstream/master
git push --progress --verbose origin refs/heads/master:refs/heads/master --tags

cd "C:\Michael_Docs\Git Repositories\NY Times COVID Data\NYC COVID Details"
git fetch --progress --verbose upstream
git merge upstream/master
git push --progress --verbose origin refs/heads/master:refs/heads/master --tags
