import os,shutil

fullpath = os.path.join
start_directory = "."
text_files = "./Text"
pdf_files = "./PDF"
html_files = "./HTML"
jpeg_files = "./JPEG"
def main():
    for dirname, dirnames, filenames in os.walk(start_directory):
        for filename in filenames:
            source = fullpath(dirname, filename)
            if filename.endswith("txt"):
                if not os.path.exists(text_files):
                    os.mkdir(text_files)
                shutil.move(source, fullpath(text_files, filename))
            elif filename.endswith("pdf"):
                if not os.path.exists(pdf_files):
                    os.mkdir(pdf_files)
                shutil.move(source, fullpath(pdf_files, filename))
            elif filename.endswith("html"):
                if not os.path.exists(html_files):
                    os.mkdir(html_files)
                shutil.move(source, fullpath(html_files, filename))
            elif filename.endswith("jpeg"):
                if not os.path.exists(jpeg_files):
                    os.mkdir(jpeg_files)
                shutil.move(source, fullpath(jpeg_files, filename))
                

if __name__ == "__main__":
    main()
