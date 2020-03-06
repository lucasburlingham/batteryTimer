# batteryTimer
Windows Batch script to test how long the battery lasts on a laptop. Python script does about the same thing, and is written in Python 3 for more compatibility.


<b>Concept:</b>
<li>Display text telling the user that the script is running. Similar to the green lighning bug in Unix.
<li>Log (append) text with current time to a file in temporary or user-accessable folder for review later.
<li>Wait 2 minutes
<li>log to file again
<li>repeat until computer dies from power loss.

