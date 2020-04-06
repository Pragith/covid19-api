@echo off
python main-api.py
git add api/
git commit -m "data refresh"
git push origin master
