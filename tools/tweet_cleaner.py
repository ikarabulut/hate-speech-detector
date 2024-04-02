import regex as re


class CleanText:
    def __init__(self):
        self._text = ""

    def set_text(self, text: str):
        self._text = text

    def get_text(self):
        return self._text


class CleanTweetBuilder:
    USERNAME_REGEX = re.compile(r'@\w+')
    UNICODE_DECIMAL_CODE_REGEX = re.compile(r'&#(\d+);')
    PUNCTUATION_REGEX = re.compile(r'[^\w\s]')
    URL_REGEX = re.compile(r'http[s]?://\S+')

    def __init__(self, tweet: str):
        self._tweet = CleanText()
        self._tweet.set_text(tweet)

    def build(self):
        return self._tweet

    def remove_character(self, char: str):
        text = self._tweet.get_text()
        self._tweet.set_text(text.replace(f'{char}', ''))
        return self

    def remove_username(self):
        self._tweet.set_text(self.USERNAME_REGEX.sub(
            '', self._tweet.get_text()))
        return self

    def remove_unicode_decimal_codes(self):
        self._tweet.set_text(self.UNICODE_DECIMAL_CODE_REGEX.sub(
            '', self._tweet.get_text()))
        return self

    def remove_punctuation(self):
        self._tweet.set_text(self._tweet.get_text().replace("'", ''))
        self._tweet.set_text(self.PUNCTUATION_REGEX.sub(
            ' ', self._tweet.get_text()))
        return self

    def remove_urls(self):
        self._tweet.set_text(self.URL_REGEX.sub(
            '', self._tweet.get_text()))
        return self

    def remove_whitespace(self):
        self._tweet.set_text(' '.join(self._tweet.get_text().split()))
        return self
