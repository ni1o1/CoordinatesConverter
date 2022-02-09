# CoordinatesConverter [![Downloads](https://pepy.tech/badge/CoordinatesConverter)](https://pepy.tech/project/CoordinatesConverter) [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/CoordinatesConverter.svg)](https://anaconda.org/conda-forge/CoordinatesConverter) 
WGS84 / BD09 / GCJ02  经纬度坐标互转，基于numpy列运算

## 安装 

### 用pypi安装 [![PyPI version](https://badge.fury.io/py/CoordinatesConverter.svg)](https://badge.fury.io/py/CoordinatesConverter)

直接在命令提示符中运行下面代码即可安装：

    pip install CoordinatesConverter

### 用conda-forge安装 [![Conda Version](https://img.shields.io/conda/vn/conda-forge/CoordinatesConverter.svg)](https://anaconda.org/conda-forge/CoordinatesConverter)

你也可以用conda-forge安装`CoordinatesConverter`，这种方式会自动解决环境依赖，不过国内可能需要更换conda源。运行下面代码即可安装：

    conda install -c conda-forge CoordinatesConverter

## 用法

```python
import CoordinatesConverter  
BUS_GPS['lon'],BUS_GPS['lat'] = CoordinatesConverter.gcj02towgs84(BUS_GPS['lon'],BUS_GPS['lat'])
```

## 功能
坐标互转，基于numpy列运算

```python
CoordinatesConverter.wgs84tobd09(lon, lat)  
CoordinatesConverter.wgs84togcj02(lon, lat)  
CoordinatesConverter.gcj02tobd09(lon, lat)  
CoordinatesConverter.gcj02towgs84(lon, lat)  
CoordinatesConverter.bd09togcj02(lon, lat)  
CoordinatesConverter.bd09towgs84(lon, lat)  
```

输入起终点经纬度，获取距离（米），基于numpy列运算

```python
CoordinatesConverter.getdistance(lon1, lat1, lon2, lat2)  
```