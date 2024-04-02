# Hate Speech Detector
This project was created to gain experience working with transfer learning on pre-trained models. In this case I am using a pre-trained `Albert` model. 

### Text preprocessing
I was hoping to not utilize the `nltk` library for this project and try to process the text using vanilla python. Utilizing the builder pattern I created a `CleanTweetBuilder` which allows the end user to select what parts of the tweet they would like cleansed with an additional tool where you can select a specific set of Characters like `RT` and have those removed from the dataset.

- Removed Usernames
- Removed URL's
- Removed unicode decimal codes (originally I converted the punctuation to hex codes and then removed from there but found the regex for unicode values made that step uncecessary)
- Remove whitespace
- Remove characters such as extra quotation marks and `RT`

## Tokenization
Utilized `AlbertTokenizer` [docs](https://huggingface.co/docs/transformers/v4.39.3/en/model_doc/albert#transformers.AlbertTokenizer)