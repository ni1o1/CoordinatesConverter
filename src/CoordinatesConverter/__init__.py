# -*- coding: utf-8 -*-
import numpy as np
import math
x_pi = 3.14159265358979324 * 3000.0 / 180.0
pi = 3.1415926535897932384626  # π
a = 6378245.0  # 长半轴
ee = 0.00669342162296594323  # 扁率
# WGS-84 转换为 GCJ-02 
def gcj02tobd09(lng, lat):
    """
    火星坐标系(GCJ-02)转百度坐标系(BD-09)
    谷歌、高德——>百度
    :param lng:火星坐标经度
    :param lat:火星坐标纬度
    :return:
    """
    try:
        lng = lng.astype(float)
        lat = lat.astype(float)
    except:
        lng = float(lng)
        lat = float(lat)
    z = np.sqrt(lng * lng + lat * lat) + 0.00002 * np.sin(lat * x_pi)
    theta = np.arctan2(lat, lng) + 0.000003 * np.cos(lng * x_pi)
    bd_lng = z * np.cos(theta) + 0.0065
    bd_lat = z * np.sin(theta) + 0.006
    return bd_lng, bd_lat


def bd09togcj02(bd_lon, bd_lat):
    """
    百度坐标系(BD-09)转火星坐标系(GCJ-02)
    百度——>谷歌、高德
    :param bd_lat:百度坐标纬度
    :param bd_lon:百度坐标经度
    :return:转换后的坐标列表形式
    """
    try:
        bd_lon = bd_lon.astype(float)
        bd_lat = bd_lat.astype(float)
    except:
        bd_lon = float(bd_lon)
        bd_lat = float(bd_lat)
    x = bd_lon - 0.0065
    y = bd_lat - 0.006
    z = np.sqrt(x * x + y * y) - 0.00002 * np.sin(y * x_pi)
    theta = np.arctan2(y, x) - 0.000003 * np.cos(x * x_pi)
    gg_lng = z * np.cos(theta)
    gg_lat = z * np.sin(theta)
    return gg_lng, gg_lat


def wgs84togcj02(lng, lat):
    """
    WGS84转GCJ02(火星坐标系)
    :param lng:WGS84坐标系的经度
    :param lat:WGS84坐标系的纬度
    :return:
    """
    try:
        lng = lng.astype(float)
        lat = lat.astype(float)
    except:
        lng = float(lng)
        lat = float(lat)
    dlat = transformlat(lng - 105.0, lat - 35.0)
    dlng = transformlng(lng - 105.0, lat - 35.0)
    radlat = lat / 180.0 * pi
    magic = np.sin(radlat)
    magic = 1 - ee * magic * magic
    sqrtmagic = np.sqrt(magic)
    dlat = (dlat * 180.0) / ((a * (1 - ee)) / (magic * sqrtmagic) * pi)
    dlng = (dlng * 180.0) / (a / sqrtmagic * np.cos(radlat) * pi)
    mglat = lat + dlat
    mglng = lng + dlng
    return mglng, mglat


def gcj02towgs84(lng, lat):
    """
    GCJ02(火星坐标系)转GPS84
    :param lng:火星坐标系的经度
    :param lat:火星坐标系纬度
    :return:
    """
    try:
        lng = lng.astype(float)
        lat = lat.astype(float)
    except:
        lng = float(lng)
        lat = float(lat)
    dlat = transformlat(lng - 105.0, lat - 35.0)
    dlng = transformlng(lng - 105.0, lat - 35.0)
    radlat = lat / 180.0 * pi
    magic = np.sin(radlat)
    magic = 1 - ee * magic * magic
    sqrtmagic = np.sqrt(magic)
    dlat = (dlat * 180.0) / ((a * (1 - ee)) / (magic * sqrtmagic) * pi)
    dlng = (dlng * 180.0) / (a / sqrtmagic * np.cos(radlat) * pi)
    mglat = lat + dlat
    mglng = lng + dlng
    return lng * 2 - mglng, lat * 2 - mglat

def wgs84tobd09(lon,lat):
    try:
        lon = lon.astype(float)
        lat = lat.astype(float)
    except:
        lon = float(lon)
        lat = float(lat)
    lon,lat = wgs84togcj02(lon,lat)
    lon,lat = gcj02tobd09(lon,lat)
    return lon,lat

def bd09towgs84(lon,lat):
    try:
        lon = lon.astype(float)
        lat = lat.astype(float)
    except:
        lon = float(lon)
        lat = float(lat)
    lon,lat = bd09togcj02(lon,lat)
    lon,lat = gcj02towgs84(lon,lat)
    return lon,lat

def bd09mctobd09(x,y):
    MCBAND = [12890594.86, 8362377.87, 5591021, 3481989.83, 1678043.12, 0]
    MC2LL = [
      [1.410526172116255e-8, 0.00000898305509648872, -1.9939833816331, 200.9824383106796, -187.2403703815547, 91.6087516669843, -23.38765649603339, 2.57121317296198, -0.03801003308653, 17337981.2],
      [-7.435856389565537e-9, 0.000008983055097726239, -0.78625201886289, 96.32687599759846, -1.85204757529826, -59.36935905485877, 47.40033549296737, -16.50741931063887, 2.28786674699375, 10260144.86],
      [-3.030883460898826e-8, 0.00000898305509983578, 0.30071316287616, 59.74293618442277, 7.357984074871, -25.38371002664745, 13.45380521110908, -3.29883767235584, 0.32710905363475, 6856817.37],
      [-1.981981304930552e-8, 0.000008983055099779535, 0.03278182852591, 40.31678527705744, 0.65659298677277, -4.44255534477492, 0.85341911805263, 0.12923347998204, -0.04625736007561, 4482777.06],
      [3.09191371068437e-9, 0.000008983055096812155, 0.00006995724062, 23.10934304144901, -0.00023663490511, -0.6321817810242, -0.00663494467273, 0.03430082397953, -0.00466043876332, 2555164.4],
      [2.890871144776878e-9, 0.000008983055095805407, -3.068298e-8, 7.47137025468032, -0.00000353937994, -0.02145144861037, -0.00001234426596, 0.00010322952773, -0.00000323890364, 826088.5]
    ]
    y1 = y.iloc[0]
    for cD in range(len(MCBAND)):
        if y1 >= MCBAND[cD]:
            cE = MC2LL[cD]
            break
    cD = cE
    T = cD[0] + cD[1] * np.abs(x);
    cB = np.abs(y) / cD[9]
    cE = cD[2] + cD[3] * cB + cD[4] * cB * cB +\
    cD[5] * cB * cB * cB + cD[6] * cB * cB * cB * cB +\
    cD[7] * cB * cB * cB * cB * cB +\
    cD[8] * cB * cB * cB * cB * cB * cB
    return T,cE

def transformlat(lng, lat):
    ret = -100.0 + 2.0 * lng + 3.0 * lat + 0.2 * lat * lat + \
        0.1 * lng * lat + 0.2 * np.sqrt(np.fabs(lng))
    ret += (20.0 * np.sin(6.0 * lng * pi) + 20.0 *
            np.sin(2.0 * lng * pi)) * 2.0 / 3.0
    ret += (20.0 * np.sin(lat * pi) + 40.0 *
            np.sin(lat / 3.0 * pi)) * 2.0 / 3.0
    ret += (160.0 * np.sin(lat / 12.0 * pi) + 320 *
            np.sin(lat * pi / 30.0)) * 2.0 / 3.0
    return ret


def transformlng(lng, lat):
    import numpy as np
    ret = 300.0 + lng + 2.0 * lat + 0.1 * lng * lng + \
        0.1 * lng * lat + 0.1 * np.sqrt(np.abs(lng))
    ret += (20.0 * np.sin(6.0 * lng * pi) + 20.0 *
            np.sin(2.0 * lng * pi)) * 2.0 / 3.0
    ret += (20.0 * np.sin(lng * pi) + 40.0 *
            np.sin(lng / 3.0 * pi)) * 2.0 / 3.0
    ret += (150.0 * np.sin(lng / 12.0 * pi) + 300.0 *
            np.sin(lng / 30.0 * pi)) * 2.0 / 3.0
    return ret

def getdistance(lon1, lat1, lon2, lat2): # 经度1，纬度1，经度2，纬度2 （十进制度数）输入为DataFrame的列
    # 将十进制度数转化为弧度
    try:
        lon1 = lon1.astype(float)
        lat1 = lat1.astype(float)
        lon2 = lon2.astype(float)
        lat2 = lat2.astype(float)
    except:
        lon1 = float(lon1)
        lat1 = float(lat1)
        lon2 = float(lon2)
        lat2 = float(lat2)
    lon1, lat1, lon2, lat2 = map(lambda r:r*pi/180, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = np.sin(dlat/2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2)**2
    c = 2 * np.arcsin(a**0.5) 
    r = 6371 # 地球平均半径，单位为公里
    return c * r * 1000

def transform_shape(gdf,method):
    '''
    输入地理要素的GeoDataFrame，对整体做坐标转换
    输入
    -------
    gdf : GeoDataFrame
        地理要素
    method : function
        坐标转换函数

    输出
    -------
    gdf : GeoDataFrame
        转换后结果
    '''
    from shapely.ops import transform
    gdf1 = gdf.copy()
    gdf1['geometry'] = gdf1['geometry'].apply(lambda r:transform(method, r))
    return gdf1