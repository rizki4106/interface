from bs4 import BeautifulSoup
import markdown
import os
import re

class MarkdownReader:

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