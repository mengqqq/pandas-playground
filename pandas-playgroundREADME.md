import pandas as pd
'''
The following code is to help you play with the concept of Series in Pandas.
You can think of Series as an one-dimensional object that is similar to an array,list,or column in a database.By default,it will 
asign an index label to each item in the Series ranging from 0 to N,where N is the number of items in the Series minus one.
Please feel fress to play around with the concept of Series and see what it does
This playground is inspires by Greg Reda's post on Intro to Pandas Data Structures:
http://www.gregreda.com/2013/10/26/intro-to-pandas-data-structures/
#Change False to True to create a Series object
if False:
    series=pd.Series(['Dave','Cheng-Han','Udacity',42,-1789710578])
    print series
'''
you can also manually assign indices to the items in the series when creating the series
'''
#Change False to True to see custom index in action
if False:
    series=pd.Series(['Dave','Cheng-Han',359,9001],
                      index=['Instructor','Curriculum Manager','Course Number','Power Level'])
                      
    print series
'''
you can use index to select specific items from the Series
'''
#Change False to True to see Series indexing in action
if False:
    series=pd.Series(['Cheng-Han',359,9001],index=['Instructor','Curriculum Manager','Course Number','Power Level'])
    print series['Instructor']
    print""
    print series[['Instructor','Curriculum Manager','Course Number']]
    
'''
you can also use boolean operators to select specific items from the Series
'''
#Change False to True to see boolean indexing in action
if False:
    cuteness=pd.Series([1,2,3,4,5],index=['Coclroach','Fish','Mini Pig','Puppy','Kitten'])
    print cuteness>3
    print ""
    print cuteness[cuteness>3]
