import src.sql_db as db
from os import path as osp

class Filesystem:
    def __init__(self):
        self.database = db.DataBase("./fs.sql")
    
    def __files(self):
        return self.database.get("fs")

    def cd(self, curr_path: str, path: str):
        if not self.check_path(path): return -1
        spl_curr_path = curr_path.split("/")
        spl_path = path.split("/")
    
    def check_path(self, path: str):
        for subpath in path.split("/"):
            if subpath not in self.__files():
                return False
        return True

    def mkdir(self, curr_path: str, path: str):
        if not self.check_path(osp.join(curr_path, path.split("/")[:-1])): return -1
        spl_curr_path = curr_path.split("/")
        spl_path = path.split("/")

        curr_fls = self.__files()
        for subpath in spl_path[:-1]:
            curr_fls = curr_fls[subpath]

        curr_fls[spl_path[-1]] = {"type": "dir", "content": {}}

    def rm(self, curr_path: str, path: str):
        if not self.check_path(osp.join(curr_path, path)): return -1
        spl_curr_path = curr_path.split("/")
        spl_path = path.split("/")

    def file(self, curr_path: str, path: str):
        if not self.check_path(osp.join(curr_path, path.split("/")[:-1])): return -1
        spl_curr_path = curr_path.split("/")
        spl_path = path.split("/")

    def readf(self, curr_path: str, path: str):
        if not self.check_path(osp.join(curr_path, path)): return -1
        spl_curr_path = curr_path.split("/")
        spl_path = path.split("/")
    
    def writef(self, curr_path: str, path: str, content: str):
        if not self.check_path(osp.join(curr_path, path.split("/")[:-1])): return -1
        spl_curr_path = curr_path.split("/")
        spl_path = path.split("/")

    def readd(self, curr_path: str, path: str):
        if not self.check_path(osp.join(curr_path, path)): return -1
        spl_curr_path = curr_path.split("/")
        spl_path = path.split("/")

    def writed(self, curr_path: str, path: str, content: str):
        if not self.check_path(osp.join(curr_path, path.split("/")[:-1])): return -1
        spl_curr_path = curr_path.split("/")
        spl_path = path.split("/")