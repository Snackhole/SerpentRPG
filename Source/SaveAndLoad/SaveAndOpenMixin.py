import os

from PyQt5.QtWidgets import QFileDialog

from SaveAndLoad.JSONSerializer import JSONSerializer


class SaveAndOpenMixin:
    def __init__(self):
        # Variables
        self.UnsavedChanges = False
        self.CurrentOpenFileName = ""

    def Save(self, ObjectToSerialize, SaveAs=False, AlternateFileDescription=None, AlternateFileExtension=None):
        Caption = "Save " + self.FileDescription if AlternateFileDescription is None else AlternateFileDescription + " File"
        Filter = self.FileDescription if AlternateFileDescription is None else AlternateFileDescription + " files (*" + self.FileExtension if AlternateFileExtension is None else AlternateFileExtension + ")"
        SaveFileName = self.CurrentOpenFileName if self.CurrentOpenFileName != "" and not SaveAs else QFileDialog.getSaveFileName(caption=Caption, filter=Filter)[0]
        if SaveFileName != "":
            JSONString = self.JSONSerializer.SerializeDataToJSONString(ObjectToSerialize)
            with open(SaveFileName, "w") as SaveFile:
                SaveFile.write(JSONString)
            self.CurrentOpenFileName = SaveFileName
            SaveFileNameShort = os.path.basename(SaveFileName)
            self.FlashStatusBar("File saved as:  " + SaveFileNameShort)
            self.UnsavedChanges = False
            return True
        else:
            self.FlashStatusBar("No file saved.")
            return False

    def Open(self):
        pass

    def SetUpSaveAndOpen(self, FileExtension, FileDescription, ObjectClasses):
        self.FileExtension = FileExtension
        self.FileDescription = FileDescription
        self.JSONSerializer = JSONSerializer(ObjectClasses)
