I checked for NaN values, encoded the target variable with label encoding, and imputed using SimpleImputer "most frequent." 

In the original column (not pre-processed) are a lot of NaN values that might affect machine learning model performance: 

"# Check for NaN values in the 'SignBankEnglishTranslations' column
nan_count_original = signdata['SignBankEnglishTranslations'].isnull().sum()
print("Number of NaN values in 'SignBankEnglishTranslations' column in the original dataset:", nan_count_original)" 

Number of NaN values in 'SignBankEnglishTranslations' column in the original dataset: 739

How can we deal with that? -- For now, I decided to drop the NaN to avoid introducing a bias with regard to the target variable. But is it possible to synthesize new data based on the underlying patterns of the data set to replace the NaN in the target variable? 

Next, the classes in the target variable are imbalanced. Some classes only have 1 sample. 

In Visual Studio Code, I seem to encounter some weird "unresolved import issues", in particular when it comes to TensorFlow. Could a cloud-based solution be better for our project? 







