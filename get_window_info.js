
var targetTitle = "__FILENAME__";
var textEdit = Application("TextEdit");
textEdit.includeStandardAdditions = true;
var allWindows = textEdit.windows();
var windowPosition, windowSize;
var result;

for (var i = 0; i < allWindows.length; i++) {
    var aWindow = allWindows[i];
    if (aWindow.name() === targetTitle) {
        result = aWindow.bounds();
    }
}
result || "Window not found";
        
