# batteryTimer
Windows Batch script to test how long the battery lasts on a laptop.


Contents:
<code>
@echo off
mkdir %TEMP%\batteryTest\
echo Made directory batteryTest at %TEMP%\batteryTest\
set COUNT = 1
echo ============ %date% ====== Started at: %time% ============ >> %TEMP%\batteryTest\batteryTest.log
echo Log entry at %time% on %date%. >> %TEMP%\batteryTest\batteryTest.log
rem Saved in "%TEMP%\batteryTest\
echo Starting Battery Test >> %TEMP%\batteryTest\batteryTest.log
echo Starting Battery Test at %time% on %date%.
goto output
:output
echo Log entry at %time% on %date%, and is the %COUNT% iteration. >> %TEMP%\batteryTest\batteryTest.log
echo >> %TEMP%\batteryTest\batteryTest.log
timeout /t 120 /nobreak
set /A Counter+=1
goto:output
<code>
