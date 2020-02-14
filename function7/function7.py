def stop_words_remover(df):
    list_of_tweets = []
    final_list_of_tweets = []
    for row in df['Tweets']:
        list_of_tweets.append(row.lower())
        
    list_of_list_of_tweets = [i.split() for i in list_of_tweets if i not in final_list_of_tweets]
    stop_words_list = stop_words_dict['stopwords']