class CountryAnalysis:
    import pandas as pd
    import matplotlib.pyplot as plt

    country = pd.read_excel('IMVA.xls') # read file

    df2 = country[['Periods','Brunei Darussalam','Indonesia','Malaysia','Myanmar','Philippines','Thailand','Vietnam','China','Hong Kong SAR','Taiwan','Japan','South Korea',
    'Bangladesh','India','Pakistan','Sri Lanka','Iran','Israel','Kuwait','Saudi Arabia','United Arab Emirates']]
    print(df2)

    split = df2['Periods'].str.split(' ', n=1, expand=True);
    df2=df2.assign(year=split[0])
    df2=df2.assign(month=split[1])

    df2['year'] = pd.to_numeric(df2['year'])

    df3 = df2[(df2['year'] >= 2008) & (df2['year']<=2017)]

    df4 = df3[['Brunei Darussalam','Indonesia','Malaysia','Myanmar','Philippines','Thailand','Vietnam','China','Hong Kong SAR','Taiwan','Japan','South Korea',
    'Bangladesh','India','Pakistan','Sri Lanka','Iran','Israel','Kuwait','Saudi Arabia','United Arab Emirates']]
    print(df4)

    df5 = df4.replace(',', '', regex=True)
    df6s = df5.replace('na', '0', regex=True)
    print(df6s)

    df6s.apply(pd.to_numeric)
    df6 = df6s.apply(pd.to_numeric)
    print(df6.dtypes)

    df7 = pd.DataFrame(df6,columns=['Brunei Darussalam','Indonesia','Malaysia','Myanmar','Philippines','Thailand','Vietnam','China','Hong Kong SAR','Taiwan','Japan','South Korea',
    'Bangladesh','India','Pakistan','Sri Lanka','Iran','Israel','Kuwait','Saudi Arabia','United Arab Emirates'])
    sum_row = df7.sum(axis=0)

    print(sum_row)

    countries = ['Brunei Darussalam','Indonesia','Malaysia','Myanmar','Philippines','Thailand','Vietnam','China','Hong Kong SAR','Taiwan','Japan','South Korea',
    'Bangladesh','India','Pakistan','Sri Lanka','Iran','Israel','Kuwait','Saudi Arabia','United Arab Emirates']

    visitor = [676397,25940515,10826923,991340,6195775,4630455,3749995,18988863,4681133,2900093,7027011,4699468,1091736,9357347,211928,883309,214038,19691,87859,155829,671670]
    visitors = []

    for number in visitor:
        visitors.append(number / 1000)

    df = pd.DataFrame({"countries":countries,"visitors":visitors})
    print(df)

    df_sorted_desc= df.sort_values('visitors',ascending=False)
    x = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    labels = df_sorted_desc['countries']

    plt.figure(figsize=(10,6))
    # bar plot with matplotlib
    plt.bar('countries', 'visitors',data=df_sorted_desc)

    plt.xlabel("countries", size=15)
    plt.ylabel("visitors in million", size=10)
    plt.xticks(x, labels, rotation='vertical')
    plt.title("Visitors by country", size=18)

    plt.show()

    top3country = df_sorted_desc.head(3)
    print(top3country)

    total = round(top3country['visitors'].values.sum()*1000,2)
    print("Sum of population for top 3 country is ",total)

    meanValue = round(top3country['visitors'].values.mean()*1000,2)
    print("Population mean for top 3 country is ", meanValue)


    plt.figure(figsize=(10,6))

    plt.bar('countries', 'visitors',data=top3country)
    plt.xlabel("countries", size=15)
    plt.ylabel("visitors in million", size=15)
    plt.title("Visitors by country", size=18)

    plt.show()




















