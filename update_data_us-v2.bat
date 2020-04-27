@echo off
python main-api-us-v2.py
git add api-v2/
git commit -m "US v2 API - data refresh"
git push origin master
