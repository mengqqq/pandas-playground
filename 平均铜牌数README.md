from pandas import DataFrame,Series
import numpy
def ave_medal_count():
    '''
    compute the average number of bronze medals earned by countries who earned at least one gold medal.
    Save this to a variable named ave_bronze_at_least_one_gold.You do not need to call the function in your code when running it 
    in the browser-the grader will do that automatically when you submit or test it.
    HINI-1:
    You can retrieve all of the values of a Pandas column from a data frame,"df",as follows:
    df['column_name']
    HINT-2
    The numpy.mean function can accept as an argument a single Pandas column
    For example,numpy.mean(df["col_name"])would return the mean of the values located in "col_name" of a dataframe df.
    countries=['Russian Fed.','Norway','Canada','United States',
               'Netherlands','Germany','Switzerland','Belarus',
               'Austria','France' ,'Poland','China','Korea',
               'Sweden','Czech Republic','Slovenia','Japan',
               'Finland','Great Britain','Ukraine','Slovakia',
               'Italy','Latvia','Australia','Croatia','Kazakhstan']
    gold=[13,11,10,9,8,8,6,5,4,4,4,3,3,2,2,2,1,1,1,1,1,0,0,0,0,0]
    silver=[11,5,10,7,7,6,3,0,8,4,1,4,3,7,4,2,4,3,1,0,0,2,2,2,1,0]
    bronze=[9,10,5,12,9,5,2,1,5,7,1,2,2,6,2,4,3,1,2,1,0,6,2,1,0,1]
    olympic_medal_counts={'country_name':Series(countries),
                          'gold':Series(gold),
                          'silver':Series(silver),
                          'bronze':Series(bronze)}
    df=DataFrame(olympic_medal_counts)
    bronze_at_least_one_gold=olympic_medal_counts['bronze']['olympic_medal_counts['gold']>=1']
    avg_bronze_at_least_one_gold=numpy.mean(bronze_at_least_one_gold)
    return avg_bronze_at_least_one_gold
    
