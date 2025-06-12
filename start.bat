@echo off
cd %cd%
docker-compose up -d
docker-compose ps
echo press any key to exit ...
pause >NUL
docker-compose down
pause
