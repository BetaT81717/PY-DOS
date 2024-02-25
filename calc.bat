@echo off
chcp 65001
color 2
:start
echo Введите выражение:
set /p exp=
set /a result="%exp%"
cls
echo Вычеслено
echo Ваше выражение:%exp%
echo Результат:%result%
echo.
pause
cls
goto start