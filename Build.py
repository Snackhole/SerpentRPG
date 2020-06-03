import os
import shutil

# Build Variables
Version = "5"
AppName = "SerpentRPG"
VersionedAppName = AppName + " " + Version


def Build():
    # Additional Build Variables
    BuildFolder = "BUILD - " + VersionedAppName

    # Build Functions
    def CopyFilesToBuildFolder(FilesList, DestinationFolderOverride=None):
        DestinationFolder = BuildFolder if DestinationFolderOverride is None else DestinationFolderOverride
        for File in FilesList:
            if os.path.isfile(File):
                shutil.copy(File, DestinationFolder)
            elif os.path.isdir(File):
                DestinationSubFolder = DestinationFolder + "/" + File
                if not os.path.exists(DestinationSubFolder):
                    os.makedirs(DestinationSubFolder)
                FilesInSubFolder = [File + "/" + SubFolderFile for SubFolderFile in os.listdir(File)]
                CopyFilesToBuildFolder(FilesInSubFolder, DestinationSubFolder)

    def CleanUp():
        shutil.rmtree(BuildFolder)
        print("Build files cleaned up.")


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
