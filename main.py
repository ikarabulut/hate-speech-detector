from tools.tweet_cleaner import CleanTweetBuilder
from tools.lightning_dataloader import ClassificationData

from transformers import AlbertTokenizer
from sklearn.model_selection import train_test_split

import pandas as pd

raw_twitter_data = pd.read_csv("data/Khilnani_LP_hate_speech_data.csv")

for i, row in raw_twitter_data.iterrows():
    cleaned_tweet = CleanTweetBuilder(row["tweet"]).remove_username().remove_urls().remove_username(
    ).remove_unicode_decimal_codes().remove_punctuation().remove_character('"').remove_character('RT').remove_whitespace().build()

    raw_twitter_data.loc[i, 'tweet'] = cleaned_tweet.get_text()

updated_df = raw_twitter_data
updated_df.to_csv("data/processed_khilnani_data.csv", index=False)


features = updated_df['tweet'].values
labels = updated_df['class'].values


x_train, x_test, y_train, y_test = train_test_split(
    features, labels, test_size=0.40)

tokenizer = AlbertTokenizer.from_pretrained("albert-base-v2")

tokenized_x_train = tokenizer(
    list(x_train), return_tensors="pt", max_length=64, padding=True, truncation=True)
tokenized_x_test = tokenizer(
    list(x_test), return_tensors="pt", max_length=64, padding=True, truncation=True)


dls = ClassificationData(tokenized_x_train, tokenized_x_test, y_train, y_test)
