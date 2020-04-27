@echo off
python main-api.py
git add api/
git commit -m "Global - data refresh"
git push origin master
