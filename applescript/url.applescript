#
#              AdvancedPresence
#                 by @fxcvd
#
#   url.applescript
#   created at 07.06.21
#   modifed at 07.06.21
#

set nameOfActiveApp to (path to frontmost application as text)
if "Safari" is in nameOfActiveApp then
    tell application "Safari"
        return the URL of the current tab of the front window
    end tell
else if "Chrome" is in nameOfActiveApp then
    tell application "Google Chrome"
        return the URL of the active tab of the front window
    end tell

else
    return "None"
end if