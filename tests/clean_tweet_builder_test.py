from tools.tweet_cleaner import CleanTweetBuilder


class TestCleanTweetBuilder:

    def test_remove_character_with_quotes_removes_all_quotes(self):
        tweet = '"""@ArizonasFinest6: Why the eggplant emoji doe?""y he say she looked like scream lmao"'
        expected_tweet = '@ArizonasFinest6: Why the eggplant emoji doe?y he say she looked like scream lmao'

        cleaned_tweet = CleanTweetBuilder(tweet).remove_character('"').build()

        assert cleaned_tweet.get_text() == expected_tweet

    def test_remove_username_should_remove_username_and_symbol(self):
        tweet = '"""@ArizonasFinest6: Why the eggplant emoji doe?""y he say she looked like scream lmao"'
        expected_tweet = '""": Why the eggplant emoji doe?""y he say she looked like scream lmao"'

        cleaned_tweet = CleanTweetBuilder(tweet).remove_username().build()

        assert cleaned_tweet.get_text() == expected_tweet

    def test_remove_emojis_should_remove_all_emojis(self):
        tweet = '#IU 8 straight nation #college soccer champions! Wow! #hoosiernation #hoosiers &#9917;&#127942;'
        expected_tweet = '#IU 8 straight nation #college soccer champions! Wow! #hoosiernation #hoosiers '

        cleaned_tweet = CleanTweetBuilder(
            tweet).remove_unicode_decimal_codes().build()

        assert cleaned_tweet.get_text() == expected_tweet

    def test_remove_punctuation_should_remove_all_punctuation(self):
        tweet = '#HappyColumbusDay .....hate to sound all #PETA callous and all........but #buffalo had it a LOT WORSE than the #injuns..........'
        expected_tweet = ' HappyColumbusDay      hate to sound all  PETA callous and all        but  buffalo had it a LOT WORSE than the  injuns          '

        cleaned_tweet = CleanTweetBuilder(
            tweet).remove_punctuation().build()

        assert cleaned_tweet.get_text() == expected_tweet

    def test_remove_urls_should_remove_urls(self):
        tweet = 'wth is that playing missy? ........ i mean seriously? RT @mr_republicann: This movie gone be trash http://t.co/8BIppVUvzr'
        expected_tweet = 'wth is that playing missy? ........ i mean seriously? RT @mr_republicann: This movie gone be trash '

        cleaned_tweet = CleanTweetBuilder(
            tweet).remove_urls().build()

        assert cleaned_tweet.get_text() == expected_tweet

    def test_remove_whitespace_should_remove_extra_spaces(self):
        tweet = ' HappyColumbusDay      hate to sound all  PETA callous and all        but  buffalo had it a LOT WORSE than the  injuns          '
        expected_tweet = 'HappyColumbusDay hate to sound all PETA callous and all but buffalo had it a LOT WORSE than the injuns'

        cleaned_tweet = CleanTweetBuilder(
            tweet).remove_whitespace().build()

        assert cleaned_tweet.get_text() == expected_tweet
