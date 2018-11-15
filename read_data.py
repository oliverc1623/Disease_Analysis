"""
Read data from Chronic Disease Data Set
"""

import pandas as pd


def return_topics(df):
    topic_set = set()

    for i in df["Topic"]:
        topic_set.add(i)

    return topic_set


def return_data_frame():
    file_path = "D:/Documents/PomonaCollege/FreshmenYear/U.S._Chronic_Disease_Indicators__CDI_.csv"
    df = pd.read_csv(file_path)
    return df
