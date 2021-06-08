#
#              AdvancedPresence
#                 by @fxcvd
#
#   title.applescript
#   created at 07.06.21
#   modifed at 07.06.21
#

set nameOfActiveApp to (path to frontmost application as text)
if "Safari" is in nameOfActiveApp then
    tell application "Safari"
        return the TITLE of the current tab of the front window
    end tell
else if "Chrome" is in nameOfActiveApp then
    tell application "Google Chrome"
        return the TITLE of the active tab of the front window
    end tell

else
    return "None"
end if