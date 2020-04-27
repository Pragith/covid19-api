@echo off
python main-api-us.py
git add api/
git commit -m "US - data refresh"
git push origin master
