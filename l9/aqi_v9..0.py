import pandas as pd

"""
    简单爬虫
"""
def main():
    aqi_data = pd.read_csv('china_city_aqi.csv')
    # print(aqi_data[['city', 'AQI']])
    print('基本信息', aqi_data.info())
    print('数据预览', aqi_data.head())
    print(aqi_data['AQI'].max())
    print(aqi_data['AQI'].min())
    print(aqi_data['AQI'].mean())

    # top10  ASC = True
    top10_city = aqi_data.sort_values(by=['AQI']).head(10)
    print('空气质量最好的10个城市', top10_city)
    # bottom10  ASC = False
    bottom10_city = aqi_data.sort_values(by=['AQI'], ascending=False).head(10)
    print('空气质量最差的10个城市', bottom10_city)

    # 保存CSV
    top10_city.to_csv('top10_city.csv', index=False)
    bottom10_city.to_csv('bottom10_city.csv', index=False)
    pd.no

if __name__ == '__main__':
    main()