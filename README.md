# batteryTimer
Windows Batch script to test how long the battery lasts on a laptop.


Contents:
<code><br>
@echo off<br>
mkdir %TEMP%\batteryTest\<br>
echo Made directory batteryTest at %TEMP%\batteryTest\<br>
set COUNT = 1<br>
echo ============ %date% ====== Started at: %time% ============ >> %TEMP%\batteryTest\batteryTest.log<br>
echo Log entry at %time% on %date%. >> %TEMP%\batteryTest\batteryTest.log<br>
rem Saved in "%TEMP%\batteryTest\<br>
echo Starting Battery Test >> %TEMP%\batteryTest\batteryTest.log<br>
echo Starting Battery Test at %time% on %date%.<br>
goto output<br>
:output<br>
echo Log entry at %time% on %date%, and is the %COUNT% iteration. >> %TEMP%\batteryTest\batteryTest.log<br>
echo >> %TEMP%\batteryTest\batteryTest.log<br>
timeout /t 120 /nobreak<br>
set /A Counter+=1<br>
goto:output
<code>
