from bs4 import BeautifulSoup
import markdown
import os
import re


class MarkdownReader:

    def __find_index(self, arr=[], query=""):
        """
        It takes an array of objects and a query string, and returns the index of the object in the array
        whose name property matches the query string

        :param arr: The array to search through
        :param query: The query string to search for
        :return: The index of the item in the array that matches the query.
        """
        for i, v in enumerate(arr):
            if v["name"] == query:
                return i
        return 0

    def listData(self, path):
        """
        It walks through the directory, and creates a list of dictionaries, each dictionary representing a
        folder or file

        :param path: The path to the directory you want to list
        :return: list of dictionary
        """
        data = []
        # listing folder
        for _, dirs, _ in os.walk(path, topdown=True):
            for d in dirs:
                context = {
                    "name": d,
                    "type": "folder",
                    "file": []
                }
                data.append(context)

        # listing file
        for root, dirs, files in os.walk(path, topdown=True):
            for f in files:
                file_path = os.path.join(root, f)
                split = file_path.split("/")

                # looking for files's folder name
                if len(split) > 3:
                    folder_name = file_path.split("/")[2]

                    # find data by spesific value on list of dictionary
                    index = self.__find_index(data, folder_name)
                    data[index]['file'].append(f)

                # if there's no file inside folder the file will store to list of data
                elif len(split) > 2 and len(split) < 4:
                    data.append({
                        "name": split[2],
                        "type": "file",
                        "file": []
                    })
        return data

    def listDocumments(self, path):
        """
        List all existing markdown documments
        """
        files = []

        for f in os.listdir(path):
            if os.path.isfile(os.path.join(path, f)) and f.split(".")[-1].lower() == "md":
                files.append(f)

        return files

    def getHeadline(self, file):
        """
        It takes a file, reads it line by line, and if it finds a markdown headline, it appends it to a list

        :param file: the file you want to parse
        :return: A list of headlines
        """
        headlines = []

        with open(file) as f:
            file_read = f.readlines()
            for line in file_read:

                markdown_html = markdown.markdown(line)
                soup = BeautifulSoup(markdown_html, "html.parser")

                if len(re.findall("<h1>", markdown_html)) > 0:

                    headlines.append(soup.get_text())

                elif len(re.findall("<h2>", markdown_html)) > 0:

                    headlines.append(soup.get_text())

                elif len(re.findall("<h3>", markdown_html)) > 0:

                    headlines.append(soup.get_text())

                elif len(re.findall("<h4>", markdown_html)) > 0:

                    headlines.append(soup.get_text())

                elif len(re.findall("<h5>", markdown_html)) > 0:

                    headlines.append(soup.get_text())

                elif len(re.findall("<h6>", markdown_html)) > 0:

                    headlines.append(soup.get_text())

                else:
                    pass

        return headlines

    def readMarkdown(self, path):
        """
        > This function reads a markdown file and returns the markdown as HTML

        :param path: The path to the file you want to read
        :return: The readMarkdown function is returning the read variable.
        """

        try:
            if os.path.exists(path):
                with open(path) as files:
                    read = markdown.markdown(files.read())
                return read
            else:
                return ""
        except:
            return ""
