import os


class DirList_Info:
    def __init__(self):
        self.NumOfFile = 0
        self.DirList =[]

    def NumOfFileCal(self,dirname):
        self.NumOfFile=len(dirname)

        return self.NumOfFile

    def search(self,dirname):

        filenames = os.listdir(dirname)
        print(filenames)
        for filename in filenames:

            full_filename = os.path.join(dirname, filename)

            if os.path.isdir(full_filename):
                self.search(full_filename)

            else:
                 ext = os.path.splitext(full_filename)[-1]
                 if ext == '.par':
                     self.DirList.append(full_filename)
                     print(full_filename)

        #print(DirList)


        return self.DirList