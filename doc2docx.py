import os.path
import win32com.client
import sys


if __name__ == "__main__":
    word = win32com.client.Dispatch("Word.application")
    wordDoc = word.Documents.Open(sys.argv[1], False, False, False)
    wordDoc.SaveAs2(sys.argv[1]+'x', FileFormat = 16)
    wordDoc.Close()
