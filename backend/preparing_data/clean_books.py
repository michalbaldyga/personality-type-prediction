import os
import re
import PyPDF2


def pdf_to_text(file_name):
    pdfText = ''
    pdfFileObj = open(file_name, 'rb')
    pdfReader = PyPDF2.PdfReader(pdfFileObj, strict=False)

    for i in range(pdfReader.numPages):
        pageObj = pdfReader.getPage(i)
        pdfText += pageObj.extractText()

    pdfFileObj.close()
    print(file_name, len(pdfText))
    return pdfText


if __name__ == "__main__":
    for root, dirs, files in os.walk('books'):
        for file in files:
            print(file)
            if file.endswith('.txt'):
                with open('books/' + file, encoding='utf-8-sig') as f:
                    text = ''.join(f.readlines())

            elif file.endswith('.pdf'):
                text = pdf_to_text('books/' + file)

            # Removing text which is before chapters with delimiter
            possible_beginning = [r'\nCONTENTS\n']
            for s in possible_beginning:
                match = re.search(s, text)
                if match is not None:
                    text = re.split(match.group(0), text)[1]
                    pass

            # Removing text which is before chapters without delimiter
            start_pos = text.find('CHAPTER I')
            if start_pos != -1:
                text = text[start_pos:]

            # Removing text which is after chapters
            possible_ending = [r'\nBIBLIOGRAPHY AND INDEX\n', r'\nFOOTNOTES:\n',
                               r'END OF THE PROJECT GUTENBERG', r'\n\nTHE END.\n', r'\nNOTES\n'
                               ]
            for s in possible_ending:
                match = re.search(s, text, re.IGNORECASE)
                if match is not None:
                    text = re.split(match.group(0), text)[0]

            # Removing chapters titles
            possible_chapters = [r'CHAPTER.*\n{2}.*\n{2}.*\n{3}', r'CHAPTER.*\n{2}.*\n.*\n{3}', r'CHAPTER.*\n{2}.*\n{3}',
                                 r'CHAPTER.*\n{2}.*\n{2}', r'CHAPTER.*\n{2}', r'CHAPTER.*\n.*\n{2}', r'[IVXLCD]+\n{2}',
                                 r'\n[0-9]+\. ']
            for s in possible_chapters:
                text = re.sub(s, '', text)

            # Removing Note 1.
            text = re.sub(r'Note [0-9]+\.', '', text, re.DOTALL, flags=re.IGNORECASE)

            # Removing (See ...)
            text = re.sub(r'\(See[^)]*\)', '', text, flags=re.IGNORECASE)

            # Replacing all multiple newlines with single white space
            text = re.sub(r'\n+', ' ', text)

            # Removing [1] ...
            text = re.sub(r'\[[0-9]+.*\\]', '', text)

            # Removing illustrations, footnotes, etc.
            text = re.sub(r'\[[^]]*]', '', text)

            # Removing {1}
            text = re.sub(r'\{[^}]*}', '', text)

            # Removing unnecessary characters
            # 1) _____
            text = re.sub(r'_+', '', text)
            # 2) * * * * *
            text = re.sub(r'\*\s[\*\s]*\*\s', '', text)
            # 3) . . . . .
            text = re.sub(r'\.\s[\.\s]*\.\s', '', text)

            # Replacing all multiple white spaces with single white space
            text = re.sub(r'\s+', ' ', text)

            file = file.replace('.pdf', '.txt')
            with open('clean_books/' + file, 'w', encoding='utf-8-sig', errors='ignore') as f:
                f.write(text)
