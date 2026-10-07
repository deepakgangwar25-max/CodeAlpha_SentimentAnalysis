# Load the dataset
df = pd.read_csv('amazon.csv')  # replace with the exact extracted file name

# Clean null values in review_content
df.dropna(subset=['review_content'], inplace=True)

# Update column references to use 'review_content' instead of 'Text'
df['Cleaned_Text'] = df['review_content'].apply(clean_text)
df[['Sentiment', 'Compound_Score']] = df['review_content'].apply(lambda x: pd.Series(get_sentiment(x)))
