set nameOfActiveApp to (path to frontmost application as text)
if "Discord" is in nameOfActiveApp then
    tell application "Google Chrome"
        return the TITLE of the active tab of the front window
    end tell
else
    return "None"
end if