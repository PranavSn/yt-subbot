from pickle import load, dump
import logging
import os




#holds subscription info for connected servers
#placed in a class to handle pickling and unpickling operations
class subDict:
    
    filepath = ""
    
    def __init__(self, filepath: str):
        self.filepath=filepath

    def addSub(self, sid: str, cid: str, uid: str=""):
        #structure is channels -> subscribed servers -> subscribed members
        subDict_t={}
        try:
            with open(self.filepath, 'rb') as subfile:
                subDict_t=load(subfile)
        except:
            print("file not found; creating file")
        if cid not in subDict_t.keys():
            subDict_t[cid] = {}
        elif sid not in subDict_t[cid]:
            subDict_t[cid][sid] = [uid]
        else:
            subDict_t[cid][sid].append(uid)
        with open(self.filepath, 'wb') as subfile:
            dump(subDict_t, subfile)
        
    def rmSub(self, sid: str, cid: str, uid: str):
        subDict_t={}
        try:
            with open(self.filepath, 'rb') as subfile:
                subDict_t=load(subfile)
        except:
            print("subscription file not initialized")
            return False
        try:
            subDict_t[cid][sid].remove(uid)
        except:
            return False
        return True
                

            