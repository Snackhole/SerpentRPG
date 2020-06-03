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
        os.unlink("SerpentRPG.pyzw")
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
    ProceedPrompt = "\n---\nInstall dependencies to build folder (" + BuildFolder + ") using a command prompt in the project directory:\n\n    python -m pip install -r requirements.txt --target \"" + BuildFolder + "\"\n\nOnce all dependencies are installed, input \"PROCEED\" to continue with build or \"CANCEL\" to cancel and clean up build files:\n---\n"
    ProceedResponse = input(ProceedPrompt)
    if ProceedResponse == "PROCEED":
        pass
    elif ProceedResponse == "CANCEL":
        CleanUp()
        print("Build canceled.")
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

# import os
# import shutil
#
# from PyInstaller import __main__ as PyInstall
#
# # Built with Python 3.6.3 and dependencies in requirements.txt
#
# def Build():
#     # Version String
#     Version = "4"
#
#     # Build Variables
#     ExecutableScript = "Source/SerpentRPG " + Version + ".pyw"
#     ExecutableZip = "Executables/Final/" + ExecutableScript[7:-4] + ".zip"
#     InstallerScript = "SerpentRPG " + Version + " Installer.pyw"
#
#     # Build Executable
#     PyInstall.run(pyi_args=[ExecutableScript,
#                             "--clean",
#                             "--windowed",
#                             "--name=SerpentRPG",
#                             "--icon=Source/Assets/.SerpentRPG Icon.ico",
#                             "--add-data=Source/Assets/.SerpentRPG Icon.ico;./Assets/",
#                             "--add-data=Source/Assets/SerpentRPG Icon.png;./Assets/",
#                             "--workpath=./Executables/Build",
#                             "--distpath=./Executables/Final"])
#
#     # Zip Executable
#     shutil.make_archive(ExecutableZip[:-4], "zip", "Executables/Final/SerpentRPG")
#
#     # Build Installer
#     PyInstall.run(pyi_args=[InstallerScript,
#                             "--clean",
#                             "--windowed",
#                             "--onefile",
#                             "--name=SerpentRPG " + Version + " Installer",
#                             "--icon=Source/Assets/.SerpentRPG Icon.ico",
#                             "--add-data=Source/Assets/SerpentRPG Icon.png;./Source/Assets/",
#                             "--add-binary=./" + ExecutableZip + ";./Executables/Final",
#                             "--workpath=./Installer/Build",
#                             "--distpath=./Installer/Final"])
#
#     # Move Files to Versions Folder
#     VersionsSubFolder = os.path.dirname("Versions/SerpentRPG " + Version + "/")
#     if not os.path.exists(VersionsSubFolder):
#         os.makedirs(VersionsSubFolder)
#     shutil.copy(ExecutableZip, VersionsSubFolder)
#     shutil.copy("Installer/Final/SerpentRPG " + Version + " Installer.exe", VersionsSubFolder)
#
#     # Delete Build Files
#     for Folder in ["Executables/", "Installer/"]:
#         shutil.rmtree(Folder, True)
#     for File in os.listdir("."):
#         if File.endswith(".spec"):
#             os.unlink(File)
#
#     # Mark Source Files as Built
#     os.rename(ExecutableScript, "Source/BUILT SerpentRPG " + Version + ".pyw")
#     os.rename(InstallerScript, "BUILT " + InstallerScript)
#
#
# if __name__ == "__main__":
#     Build()
