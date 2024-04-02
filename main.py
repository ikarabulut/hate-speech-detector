from tools.tweet_cleaner import CleanTweetBuilder
import pandas as pd

raw_twitter_data = pd.read_csv("data/Khilnani_LP_hate_speech_data.csv")

for i, row in raw_twitter_data.iterrows():
    cleaned_tweet = CleanTweetBuilder(row["tweet"]).remove_username().remove_urls().remove_username(
    ).remove_unicode_decimal_codes().remove_punctuation().remove_character('"').remove_character('RT').remove_whitespace().build()

    raw_twitter_data.loc[i, 'tweet'] = cleaned_tweet.get_text()

updated_df = raw_twitter_data.drop(columns=['id'])
updated_df.to_csv("data/processed_khilnani_data.csv")
