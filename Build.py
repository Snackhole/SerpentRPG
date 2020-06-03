import os
import shutil
import zipapp

# Build Variables
Version = "5"
AppName = "SerpentRPG"
VersionedAppName = AppName + " " + Version

CodeFiles = ["Core", "Interface", "SaveAndLoad", "Build.py", "SerpentRPG.py"]
AssetFiles = ["Assets"]

ExecutableZipName = AppName + ".pyzw"
Interpreter = "python3"
Main = AppName + ":StartApp"


def Build():
    # Additional Build Variables
    BuildFolder = "BUILD - " + VersionedAppName

    # Build Functions
    def CopyFilesToBuildFolder(CopiedFiles):
        IgnoredFiles = [File for File in os.listdir(".") if File not in CopiedFiles]
        shutil.copytree(".", BuildFolder, ignore=lambda Source, Contents: IgnoredFiles)

    def CleanUp():
        shutil.rmtree(BuildFolder)
        print("Build files cleaned up.")

    # Copy Code to Build Folder
    CopyFilesToBuildFolder(CodeFiles)
    print("Code files copied to build folder.")

    # Create Executable Archive
    zipapp.create_archive(BuildFolder, ExecutableZipName, Interpreter, Main)
    print("Executable archive created.")

    # Delete Build Folder
    shutil.rmtree(BuildFolder)
    print("Build folder deleted.")

    # Copy Assets to Build Folder and Move Executable Zip
    CopyFilesToBuildFolder(AssetFiles)
    shutil.move(ExecutableZipName, BuildFolder)

    # Prompt to Install Dependencies
    ProceedPrompt = "\n---\nInstall dependencies to build folder (" + BuildFolder + ") using a command prompt:\n\n    python -m pip install -r \"" + os.getcwd() + "\\requirements.txt\" --target \"" + os.getcwd() + "\\" + BuildFolder + "\"\n\nOnce all dependencies are installed, input \"PROCEED\" to continue with build or \"CANCEL\" to cancel and clean up build files:\n---\n"
    ProceedResponse = input(ProceedPrompt)
    if ProceedResponse == "PROCEED":
        pass
    elif ProceedResponse == "CANCEL":
        print("Build canceled.")
        CleanUp()
        return
    else:
        return

    # Zip Build
    shutil.make_archive(VersionedAppName, "zip", BuildFolder)
    print("Build zipped.")

    # Clean Up
    CleanUp()


if __name__ == "__main__":
    Build()
