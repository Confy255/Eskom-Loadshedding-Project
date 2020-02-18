import numpy as np
import pandas as pd

ebp_url = 'https://raw.githubusercontent.com/Explore-AI/Public-Data/master/Data/electrification_by_province.csv'
ebp_df = pd.read_csv(ebp_url)

for col, row in ebp_df.iloc[:,1:].iteritems():
    ebp_df[col] = ebp_df[col].str.replace(',','').astype(int)

ebp_df.head()

twitter_url = 'https://raw.githubusercontent.com/Explore-AI/Public-Data/master/Data/twitter_nov_2019.csv'
twitter_df = pd.read_csv(twitter_url)
twitter_df.head()

# gauteng ebp data as a list
gauteng = ebp_df['Gauteng'].astype(float).to_list()

# dates for twitter tweets
dates = twitter_df['Date'].to_list()

# dictionary mapping official municipality twitter handles to the municipality name
mun_dict = {
    '@CityofCTAlerts' : 'Cape Town',
    '@CityPowerJhb' : 'Johannesburg',
    '@eThekwiniM' : 'eThekwini' ,
    '@EMMInfo' : 'Ekurhuleni',
    '@centlecutility' : 'Mangaung',
    '@NMBmunicipality' : 'Nelson Mandela Bay',
    '@CityTshwane' : 'Tshwane'
}

# dictionary of english stopwords
stop_words_dict = {
    'stopwords':[
        'where', 'done', 'if', 'before', 'll', 'very', 'keep', 'something', 'nothing', 'thereupon', 
        'may', 'why', 'â€™s', 'therefore', 'you', 'with', 'towards', 'make', 'really', 'few', 'former', 
        'during', 'mine', 'do', 'would', 'of', 'off', 'six', 'yourself', 'becoming', 'through', 
        'seeming', 'hence', 'us', 'anywhere', 'regarding', 'whole', 'down', 'seem', 'whereas', 'to', 
        'their', 'various', 'thereafter', 'â€˜d', 'above', 'put', 'sometime', 'moreover', 'whoever', 'although', 
        'at', 'four', 'each', 'among', 'whatever', 'any', 'anyhow', 'herein', 'become', 'last', 'between', 'still', 
        'was', 'almost', 'twelve', 'used', 'who', 'go', 'not', 'enough', 'well', 'â€™ve', 'might', 'see', 'whose', 
        'everywhere', 'yourselves', 'across', 'myself', 'further', 'did', 'then', 'is', 'except', 'up', 'take', 
        'became', 'however', 'many', 'thence', 'onto', 'â€˜m', 'my', 'own', 'must', 'wherein', 'elsewhere', 'behind', 
        'becomes', 'alone', 'due', 'being', 'neither', 'a', 'over', 'beside', 'fifteen', 'meanwhile', 'upon', 'next', 
        'forty', 'what', 'less', 'and', 'please', 'toward', 'about', 'below', 'hereafter', 'whether', 'yet', 'nor', 
        'against', 'whereupon', 'top', 'first', 'three', 'show', 'per', 'five', 'two', 'ourselves', 'whenever', 
        'get', 'thereby', 'noone', 'had', 'now', 'everyone', 'everything', 'nowhere', 'ca', 'though', 'least', 
        'so', 'both', 'otherwise', 'whereby', 'unless', 'somewhere', 'give', 'formerly', 'â€™d', 'under', 
        'while', 'empty', 'doing', 'besides', 'thus', 'this', 'anyone', 'its', 'after', 'bottom', 'call', 
        'nâ€™t', 'name', 'even', 'eleven', 'by', 'from', 'when', 'or', 'anyway', 'how', 'the', 'all', 
        'much', 'another', 'since', 'hundred', 'serious', 'â€˜ve', 'ever', 'out', 'full', 'themselves', 
        'been', 'in', "'d", 'wherever', 'part', 'someone', 'therein', 'can', 'seemed', 'hereby', 'others', 
        "'s", "'re", 'most', 'one', "n't", 'into', 'some', 'will', 'these', 'twenty', 'here', 'as', 'nobody', 
        'also', 'along', 'than', 'anything', 'he', 'there', 'does', 'we', 'â€™ll', 'latterly', 'are', 'ten', 
        'hers', 'should', 'they', 'â€˜s', 'either', 'am', 'be', 'perhaps', 'â€™re', 'only', 'namely', 'sixty', 
        'made', "'m", 'always', 'those', 'have', 'again', 'her', 'once', 'ours', 'herself', 'else', 'has', 'nine', 
        'more', 'sometimes', 'your', 'yours', 'that', 'around', 'his', 'indeed', 'mostly', 'cannot', 'â€˜ll', 'too', 
        'seems', 'â€™m', 'himself', 'latter', 'whither', 'amount', 'other', 'nevertheless', 'whom', 'for', 'somehow', 
        'beforehand', 'just', 'an', 'beyond', 'amongst', 'none', "'ve", 'say', 'via', 'but', 'often', 're', 'our', 
        'because', 'rather', 'using', 'without', 'throughout', 'on', 'she', 'never', 'eight', 'no', 'hereupon', 
        'them', 'whereafter', 'quite', 'which', 'move', 'thru', 'until', 'afterwards', 'fifty', 'i', 'itself', 'nâ€˜t',
        'him', 'could', 'front', 'within', 'â€˜re', 'back', 'such', 'already', 'several', 'side', 'whence', 'me', 
        'same', 'were', 'it', 'every', 'third', 'together'
    ]
}

#Function 1

def dictionary_of_metrics(items):
    mean = round(np.mean(items), 2)
    median = round(np.median(items), 2)
    var = round(np.var(items, ddof=1), 2)
    std_dev = round(np.std(items, ddof=1), 2)
    minimum = round(min(items), 2)
    maximum = round(max(items), 2)

    return {
        'mean': mean,
        'median': median,
        'var': var,
        'std': std_dev,
        'min': minimum,
        'max': maximum
        }

#Function 2

def five_num_summary(items):
        
    """THIS FUNCTION WORKS AS SUCH;
            >Takes in a list of integers
            >Returns a dictionary with the five number summarry (median, q1, q3, max, min) 
            as keys and corrisponding values,rounded to two decimal places, as values to the keys.
    """
    maximum = round(max(items),2)
    median = round(np.median(items),2)
    minimum = round(min(items),2)
    Q1 = round(np.percentile(items, 25), 2)
    Q3 = round(np.percentile(items, 75), 2)
    return {'max': maximum, 'median': median, 'min': minimum, "q1":Q1, "q3":Q3}

#Function 3

def date_parser(dates):
    return [i.split(' ', 1)[0] for i in dates]


#Function 4

def extract_municipality_hashtags(df):
    # your code here

    """This function extracts the names of the municipalities
    and hashtag comments from the tweets column dataframe and returns
    new dataframe.
    """

    municipality_dict = { '@CityofCTAlerts' : 'Cape Town',
            '@CityPowerJhb' : 'Johannesburg',
            '@eThekwiniM' : 'eThekwini' ,
            '@EMMInfo' : 'Ekurhuleni',
            '@centlecutility' : 'Mangaung',
            '@NMBmunicipality' : 'Nelson Mandela Bay',
            '@CityTshwane' : 'Tshwane'}
     
    list_with_hashtags = []
    final_list_with_hashtags = []
    
    list_with_mun = []
    final_list_with_mun = []
    
    
    
    for tweet in df['Tweets']:
        if '#' in tweet:
            list_with_hashtags.append(tweet.lower())

        else:
            list_with_hashtags.append(np.nan)      

    list_of_list_with_hashtags = [i.split() if i is not np.nan else i for i in list_with_hashtags]
    
    for value in list_of_list_with_hashtags:
        if value is not np.nan:
            final_list_with_hashtags.append([value2 for value2 in value if value2[0] == '#'])
        else:
            final_list_with_hashtags.append(value)


    for tweets in df['Tweets']:
        if '@' in tweets:
            list_with_mun.append(tweets)
        else:
            list_with_mun.append(str(np.nan))
            
    rows = [i.split() if i is not str(np.nan) else i for i in list_with_mun]
    
    list_of_keys = []
    
    for key in municipality_dict.keys():
        list_of_keys.append(key)

    for list_value in rows:
        for value in list_value:
            if value in list_of_keys:
                final_list_with_mun.append(municipality_dict[value])
            else:
                final_list_with_mun.append(str(np.nan))

#Function 5

def number_of_tweets_per_day(df):

  mod_date = [i.split(' ', 1)[0] for i in dates]
  twitter_df = pd.read_csv(twitter_url)
  twitter_df_by_tweets= twitter_df.groupby(mod_date)['Tweets'].count()
  new_dataframe = pd.DataFrame(twitter_df_by_tweets).rename_axis('Date')

  return new_dataframe

#Function 6

def word_splitter(df):
    """THIS FUNCTION WORKS AS SUCH;
            >Takes in a pandas dataframe and extracts a column called 'Tweets'.
            >The function then spilts the tweets into a list of separate words.
            >Results are in lowercase and are then placed in a new column called 'Spilt Tweets'.
            >Lastly the function modifies the input dataframe by adding the 'Split Tweets' column to the dataframe.
    """
    list_of_tweets = []
    final_list_of_tweets = []
    for row in df['Tweets']:
        list_of_tweets.append(row.lower())
        
    list_of_list_of_tweets = [i.split() for i in list_of_tweets]
    
    for item in list_of_list_of_tweets:
        final_list_of_tweets.append(item)
        
    df_final_list_of_tweets = pd.DataFrame({'Split Tweets': final_list_of_tweets})
    final_df = pd.concat([df,df_final_list_of_tweets], axis=1)

    return final_df

#Function 7

def stop_words_remover(df):
    list_of_tweets = []
    final_list_of_tweets = []
    for row in df['Tweets']:
        list_of_tweets.append(row.lower())
        
    list_of_list_of_tweets = [i.split() for i in list_of_tweets if i not in final_list_of_tweets]
    stop_words_list = stop_words_dict['stopwords']

    for i in list_of_list_of_tweets:
        for p in stop_words_list:
            if p in i:
                i.remove(p)
            else:
                continue

    df_final_list_of_tweets = pd.DataFrame({'Without Stop Words': list_of_list_of_tweets})
    final_df = pd.concat([df,df_final_list_of_tweets], axis=1)

    return final_df
