"""
Реализовать метод __str__, позволяющий выводить все папки и файлы из данной, например так:

> print(folder1)

V folder1
|-> V folder2
|   |-> V folder3
|   |   |-> file3
|   |-> file2
|-> file1

А так же возможность проверить, находится ли файл или папка в другой папке:
> print(file3 in folder2)
True

"""
import os

class PrintableFolder:

    # default start point
    startpath = '.'

    folders = []  # folder store
    tuples = []  # folders, subdirs, files

    def __init__(self, name=None, content=None):
        self.name = name if name else self.startpath
        self.content = content if content else self.tuples

    def folder_tree(self, line, directory):
        one = '|-> V '
        padding = '|   '

        if line == directory:
            # print('V '+line)
            return ('V ' + line)

        if line.count(os.sep) == 1:
            line = line.split(os.sep)
            line[0] = one
            # print(''.join(line))
            return (''.join(line))

        if line.count(os.sep) >= 2:
            line = line.split(os.sep)
            line[-2] = one
            for i in range(len(line[:-2])):
                line[i] = padding
            # print(''.join(line))
            return (''.join(line))

    def files_tree(self, directory, *args):
        """

        :param directory: startpath
        :param args: args[0] -> tuples, args[1] -> folders
        :return: None
        """
        file = '|-> '
        padding = '|   '
        last_file = ''
        tuples = args[0]
        folders_list = args[1]

        for root, subs, files in tuples:
            # no files no worries, skip
            if not files:
                continue

            # will use for padding: padding * sep
            sep = root.count(os.sep)

            # only if root has some files
            if root == directory:
                last_file = [file + str(x) for x in files]
                continue

            if subs:
                # take last elem in subs,
                # use it as value to find the same in folders_list
                # get index + 1 to insert right after
                index = folders_list.index([x for x in folders_list if x.endswith(subs[-1])][0]) + 1

            else:
                # we need name the last of folder in the root
                # to use it to find index
                folder_name = root.split(os.sep)[-1]
                index = folders_list.index([x for x in folders_list if x.endswith(folder_name)][0]) + 1

            # prepare files
            files = [sep * padding + file + x for x in files]

            # now insert files to list
            for i, a in enumerate(range(index, index + len(files))):
                folders_list.insert(a, files[i])

        if last_file:
            # merge files in root directory
            folders_list = folders_list + last_file

        # final print tree
        for elm in folders_list:
            print(elm)

        return ''

    def tree_walk(self, directory):
        for folder, subs, files in os.walk(directory):
            self.tuples.append((folder, subs, files))
            self.folders.append(self.folder_tree(folder, directory))

    def __contains__(self, file):
        for _, _, files in self.content:
            return file.name in files

    def __str__(self):
        self.tree_walk(self.name)
        self.folder_tree(self.tuples, self.name)
        return str(self.files_tree(self.name, self.tuples, self.folders))


class PrintableFile:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        print(self.name)


if __name__ == '__main__':
    current_path = os.path.dirname(os.path.abspath(__file__))
    project_path = os.path.join(current_path, '../../06-advanced-python')
    contents_generator = os.walk(project_path)

    contents = []
    next(iter(contents_generator))
    for root, dirs, files in contents_generator:
        contents.append((root, dirs, files))

    folder1 = PrintableFolder(project_path, contents)
    print(folder1)
    file1 = PrintableFile('task1.py')
    print(file1 in folder1)