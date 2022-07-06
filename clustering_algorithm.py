from helper_functions import loading_all_datasets, clean_data


filenames = ['Data/Udacity_AZDIAS_Subset.csv',
             'Data/AZDIAS_Feature_Summary.csv',
             'Data/Udacity_CUSTOMERS_Subset.csv']


# print(loading_dataset('Data/AZDIAS_Feature_Summary.csv'))


# print(loading_dataset('Data/Udacity_AZDIAS_Subset.csv', sep=';'))

list_of_datasets = loading_all_datasets(filenames)
# print(len(list_of_datasets))
# print(list_of_datasets[-1])


df_azdias = list_of_datasets[0]
df_feat_info = list_of_datasets[1]
df_customers = list_of_datasets[2]


# print(df_azdias.info)

clean_datasets = []
for dataset in list_of_datasets:
    initial_rows, final_rows, df_clean = clean_data(dataset)
    clean_datasets.append((initial_rows, final_rows, df_clean))

print(dataset)
for i_rows, f_rows, clean_df in clean_datasets:
    print(i_rows, f_rows)


