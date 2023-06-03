import re


def clear_data(text):
    # Removing Tweets
    text = re.sub(r'Tweets', '', text, re.DOTALL, flags=re.IGNORECASE)
    # diffent emojis pattern
    text = re.sub(r'\p{So}', '', string)
    # Emojis pattern
    text = re.sub("["
                  u"\U0001F600-\U0001F64F"  # emoticons
                  u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                  u"\U0001F680-\U0001F6FF"  # transport & map symbols
                  u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                  u"\U00002702-\U000027B0"
                  u"\U000024C2-\U0001F251"
                  u"\U0001f926-\U0001f937"
                  u'\U00010000-\U0010ffff'
                  u"\u200d"
                  u"\u2640-\u2642"
                  u"\u2600-\u2B55"
                  u"\u23cf"
                  u"\u23e9"
                  u"\u231a"
                  u"\u3030"
                  u"\ufe0f"
                  "]+", "", text, flags=re.UNICODE)

    # Removing #
    text = re.sub(r'#', '', text)

    # Removing [
    text = re.sub(r'\[', '', text)

    # Removing ]
    text = re.sub(r']', '', text)

    # Removing &amp
    text = re.sub(r'&amp', '', text, re.DOTALL, flags=re.IGNORECASE)

    # Removing --
    text = re.sub(r'--', '', text, re.DOTALL, flags=re.IGNORECASE)

    # Removing "&lt;&lt;
    text = re.sub(r'"&lt;&lt;', '', text, re.DOTALL, flags=re.IGNORECASE)

    # Removing gt;gt;
    text = re.sub(r'gt;gt;', '', text)

    # Removing Note 1.
    text = re.sub(r'Note [0-9]+\.', '', text, re.DOTALL, flags=re.IGNORECASE)

    # Removing @user
    text = re.sub(r'@\w+', '', text)

    # Removing &
    text = re.sub(r'&', '', text, re.DOTALL, flags=re.IGNORECASE)

    # Removing *
    text = re.sub(r'\*', '', text, re.DOTALL, flags=re.IGNORECASE)

    # Removing Link:
    text = re.sub(r'Link:', '.', text, re.DOTALL, flags=re.IGNORECASE)

    # Removing (See ...)
    text = re.sub(r'\(See[^)]*\)', '', text, flags=re.IGNORECASE)

    # Replacing all multiple newlines with single white space
    text = re.sub(r'\n+', '\n', text)

    # Removing [1] ...
    text = re.sub(r'\[[0-9]+.*\\]', '', text)

    # Removing illustrations, footnotes, etc.
    text = re.sub(r'\[[^]]*]', '', text)

    # Removing links http
    text = re.sub(r'http?\S+', ' ', text, flags=re.MULTILINE)

    # Remove links that start with // from the text using regular expressions
    text = re.sub(r'(?<!:)//\S+', ' ', text)

    # Remove links that start with \\ from the text using regular expressions
    text = re.sub(r'(?<!:)\\\S+', ' ', text)

    # Removing s:
    text = re.sub(r's:\S+', '', text, flags=re.MULTILINE)

    # Removing {1}
    text = re.sub(r'\{[^}]*}', '', text)

    # Removing '
    text = re.sub(r'\'', '', text, flags=re.MULTILINE)

    # Removing "
    text = re.sub(r'"', '', text, flags=re.MULTILINE)

    # Removing “
    text = re.sub(r'“', '', text, flags=re.MULTILINE)

    # Removing ” different than above
    text = re.sub(r'”', '', text, flags=re.MULTILINE)

    # Removing unnecessary characters
    # 1) _____
    text = re.sub(r'_+', '', text)
    # 2) * * * * *
    text = re.sub(r'\*\s[\*\s]*\*\s', '', text)
    # 3) . . . . .
    text = re.sub(r'\.\s[\.\s]*\.\s', '.', text)
    # 4) ...
    text = re.sub(r"\.\.\.", "", text)

    # Replacing all multiple white spaces with single white space
    text = re.sub(r'\s+', ' ', text)

    # Replace multiple exclamation marks with a single exclamation mark
    text = re.sub(r'!{2,}', '!', text)

    # Replace multiple question marks with a single question mark
    text = re.sub(r'\?{2,}', '?', text)

    text = re.sub(r';', ',', text)

    text = re.sub(r':', '', text)

    # Removing "
    text = re.sub(r'"', '', text, flags=re.MULTILINE)

    return text
