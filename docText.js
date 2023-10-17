var targetFileName = "__FILENAME__";
var textEdit = Application("TextEdit");
var documentText = "Document not found";

// Loop through all documents to find the one with the target file name
var allDocs = textEdit.documents;
for (var i = 0; i < allDocs.length; i++) {
    var aDoc = allDocs[i];
    if (aDoc.name() === targetFileName) {
        // Get the text of the document
        documentText = aDoc.text();
        break;
    }
}

documentText;