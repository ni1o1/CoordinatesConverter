# CoordinatesConverter
WGS84 / BD09 / GCJ02  经纬度坐标互转，基于numpy列运算

## 安装

> pip install CoordinatesConverter

## 用法
> import CoordinatesConverter  
BUS_GPS['lon'],BUS_GPS['lat'] = CoordinatesConverter.gcj02towgs84(BUS_GPS['lon'],BUS_GPS['lat'])

## 功能
坐标互转，基于numpy列运算
>CoordinatesConverter.wgs84tobd09(lon, lat)  
CoordinatesConverter.wgs84togcj02(lon, lat)  
CoordinatesConverter.gcj02tobd09(lon, lat)  
CoordinatesConverter.gcj02towgs84(lon, lat)  
CoordinatesConverter.bd09togcj02(lon, lat)  
CoordinatesConverter.bd09towgs84(lon, lat)  

输入起终点经纬度，获取距离（米），基于numpy列运算
>CoordinatesConverter.getdistance(lon1, lat1, lon2, lat2)  

注：传入列数据类型需为float