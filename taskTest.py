# -*- coding:utf-8 -*-
import API,json,time
import requests,os
from ftplib import FTP

class landuseTest:
    def __init__(self,key,token,dir):
        self.token =token
        self.taskid = key
        self.defaultdir = dir
        self.url = "http://bt1.geosts.ac.cn/api/dcpp/dcpp/rest/v1/task/" + self.taskid + "/commit"
        self.headers = {"Authorization": self.token,
                        "Content-Type": "application/json"}

    def makeftpdir(self,dir):
        ftp = FTP()
        ftp.connect(self.defaultdir[6:17], 21)
        ftp.login("lucc", "lucc@tq123")
        print(ftp.getwelcome())
        ftp.mkd(dir[18:])
        ftp.quit()

    def ModelFarm(self):
        self.makeftpdir(self.defaultdir)
        insertDataList = []
        datas = ["Farm.zip"]
        for ds in datas:
            insertDataList.append(self.defaultdir + "/" + ds)
        data = {
            "taskId": self.taskid,
            "consumed": 24,
            "workload": 100,
            "description": "ModelFarmSubmit",
            "datas": [
                {
                    "content": insertDataList,
                    "label": "ModelFarmSubmit",
                    "workload": 2
                }
            ]
        }
        r = requests.post(url=self.url, json=data, headers=self.headers)
        return data,r.status_code

    def ModelWater(self):
        self.makeftpdir(self.defaultdir)
        insertDataList = []
        datas = ["Water.zip"]
        for ds in datas:
            insertDataList.append(self.defaultdir + "/" + ds)
        data = {
            "taskId": self.taskid,
            "consumed": 24,
            "workload": 100,
            "description": "ModelWaterSubmit",
            "datas": [
                {
                    "content": insertDataList,
                    "label": "ModelWaterSubmit",
                    "workload": 2
                }
            ]
        }
        r = requests.post(url=self.url, json=data, headers=self.headers)
        return data,r.status_code

    def ModelBuilding(self):
        self.makeftpdir(self.defaultdir)
        insertDataList = []
        datas = ["Building.zip"]
        for ds in datas:
            insertDataList.append(self.defaultdir + "/" + ds)
        data = {
            "taskId": self.taskid,
            "consumed": 24,
            "workload": 100,
            "description": "ModelBuildingSubmit",
            "datas": [
                {
                    "content": insertDataList,
                    "label": "ModelBuildingSubmit",
                    "workload": 2
                }
            ]
        }
        r = requests.post(url=self.url, json=data, headers=self.headers)
        return data,r.status_code

    def ModelForest(self):
        self.makeftpdir(self.defaultdir)
        insertDataList = []
        datas = ["Forest.zip"]
        for ds in datas:
            insertDataList.append(self.defaultdir + "/" + ds)
        data = {
            "taskId": self.taskid,
            "consumed": 24,
            "workload": 100,
            "description": "ModelForestSubmit",
            "datas": [
                {
                    "content": insertDataList,
                    "label": "ModelForestSubmit",
                    "workload": 2
                }
            ]
        }
        r = requests.post(url=self.url, json=data, headers=self.headers)
        return data,r.status_code

    def Ref(self):
        self.makeftpdir(self.defaultdir)
        insertDataList = []
        datas = ["Ref.zip"]
        for ds in datas:
            insertDataList.append(self.defaultdir + "/" + ds)
        data = {
            "taskId": self.taskid,
            "consumed": 24,
            "workload": 100,
            "description": "RefSubmit",
            "datas": [
                {
                    "content": insertDataList,
                    "label": "RefSubmit",
                    "workload": 2
                }
            ]
        }
        r = requests.post(url=self.url, json=data, headers=self.headers)
        return data,r.status_code

    def Image(self):
        self.makeftpdir(self.defaultdir)
        insertDataList = []
        datas = ["Suzhou_Gaoxinqu_image.tif"]
        for ds in datas:
            insertDataList.append(self.defaultdir + "/" + ds)
        data = {
            "taskId": self.taskid,
            "consumed": 24,
            "workload": 100,
            "description": "ImageSubmit",
            "datas": [
                {
                    "content": insertDataList,
                    "label": "ImageSubmit",
                    "workload": 2
                }
            ]
        }
        r = requests.post(url=self.url, json=data, headers=self.headers)
        return data,r.status_code

    def DEM(self):
        self.makeftpdir(self.defaultdir)
        insertDataList = []
        datas = ["Suzhou_Gaoxinqu_dem.tfw","Suzhou_Gaoxinqu_dem.tif","Suzhou_Gaoxinqu_dem.tif.ovr"]
        for ds in datas:
            insertDataList.append(self.defaultdir + "/" + ds)
        data = {
            "taskId": self.taskid,
            "consumed": 24,
            "workload": 100,
            "description": "DEMSubmit",
            "datas": [
                {
                    "content": insertDataList,
                    "label": "DEMSubmit",
                    "workload": 2
                }
            ]
        }
        r = requests.post(url=self.url, json=data, headers=self.headers)
        return data,r.status_code

    def TaskArea(self):
        self.makeftpdir(self.defaultdir)
        insertDataList = []
        datas = ["Suzhou_Gaoxinqu_taskArea.dbf",
                 "Suzhou_Gaoxinqu_taskArea.prj",
                 "Suzhou_Gaoxinqu_taskArea.sbn",
                 "Suzhou_Gaoxinqu_taskArea.sbx",
                 "Suzhou_Gaoxinqu_taskArea.shp",
                 "Suzhou_Gaoxinqu_taskArea.shx"]
        for ds in datas:
            insertDataList.append(self.defaultdir + "/" + ds)
        data = {
            "taskId": self.taskid,
            "consumed": 24,
            "workload": 100,
            "description": "TaskAreaSubmit",
            "datas": [
                {
                    "content": insertDataList,
                    "label": "TaskAreaSubmit",
                    "workload": 2
                }
            ]
        }
        r = requests.post(url=self.url, json=data, headers=self.headers)
        return data,r.status_code

    def ImageService(self):

        insertDataList = ["http://10.16.20.14:6080/arcgis/rest/services/SZ_SND_432/MapServer/WMTS/1.0.0/WMTSCapabilities.xml",
                          "http://10.16.20.14:6080/arcgis/rest/services/SZ_SND_321/MapServer/WMTS/1.0.0/WMTSCapabilities.xml"]
        data = {
            "taskId": self.taskid,
            "consumed": 24,
            "workload": 100,
            "description": "ImageServiceSubmit",
            "datas": [
                {
                    "content": insertDataList,
                    "label": "ImageServiceSubmit",
                    "workload": 2
                }
            ]
        }
        r = requests.post(url=self.url, json=data, headers=self.headers)
        return data,r.status_code

    def LanduseClassificationPrepare(self):
        data = {
            "taskId": self.taskid,
            "consumed": 24,
            "workload": 100,
            "description": "LanduseClassificationSubmit",
            "datas": [
                {
                    "content": ["LanduseClassification"],#注意，这个content需要写成数组[]
                    "label": "LanduseClassificationSubmit",
                    "workload": 2
                }
            ]
        }
        r = requests.post(url=self.url, json=data, headers=self.headers)
        return data,r.status_code

    def checkClassificationPrepare(self):
        data = {
            "taskId": self.taskid,
            "consumed": 24,
            "workload": 100,
            "description": "checkClassificationSubmit",
            "datas": [
                {
                    "content": ["checkClassification"],
                    "label": "checkClassificationSubmit",
                    "workload": 2
                }
            ]
        }
        r = requests.post(url=self.url, json=data, headers=self.headers)
        return data,r.status_code

    def DEMcalculate(self):
        self.makeftpdir(self.defaultdir)
        insertDataList = []
        datas = ["Suzhou_Gaoxinqu_line.dbf",
                 "Suzhou_Gaoxinqu_line.prj",
                 "Suzhou_Gaoxinqu_line.sbn",
                 "Suzhou_Gaoxinqu_line.sbx",
                 "Suzhou_Gaoxinqu_line.shp",
                 "Suzhou_Gaoxinqu_line.shx",
                 "Suzhou_Gaoxinqu_shadow.tfw",
                 "Suzhou_Gaoxinqu_shadow.tif",
                 "Suzhou_Gaoxinqu_shadow.tif.aux.xml",
                 "Suzhou_Gaoxinqu_shadow.tif.ovr",
                 "Suzhou_Gaoxinqu_shadow.tif.vat.dbf",
                 "Suzhou_Gaoxinqu_shadow.tif.xml"]
        for ds in datas:
            insertDataList.append(self.defaultdir + "/" + ds)
        data = {
            "taskId": self.taskid,
            "consumed": 24,
            "workload": 100,
            "description": "DEMcalculateSubmit",
            "datas": [
                {
                    "content": insertDataList,
                    "label": "DEMcalculateSubmit",
                    "workload": 2
                }
            ]
        }
        r = requests.post(url=self.url, json=data, headers=self.headers)
        return data,r.status_code

    def vectorSegmentation(self):
        self.makeftpdir(self.defaultdir)
        insertDataList = []
        datas = ["Suzhou_Gaoxinqu_vecSeg.dbf",
                 "Suzhou_Gaoxinqu_vecSeg.prj",
                 "Suzhou_Gaoxinqu_vecSeg.sbn",
                 "Suzhou_Gaoxinqu_vecSeg.sbx",
                 "Suzhou_Gaoxinqu_vecSeg.shp",
                 "Suzhou_Gaoxinqu_vecSeg.shx"]
        for ds in datas:
            insertDataList.append(self.defaultdir + "/" + ds)
        data = {
            "taskId": self.taskid,
            "consumed": 24,
            "workload": 100,
            "description": "vectorSegmentationSubmit",
            "datas": [
                {
                    "content": insertDataList,
                    "label": "vectorSegmentationSubmit",
                    "workload": 2
                }
            ]
        }
        r = requests.post(url=self.url, json=data, headers=self.headers)
        return data,r.status_code

    def SegmentationSplit(self):
        self.makeftpdir(self.defaultdir)
        insertDataList1 = []
        insertDataList2 = []
        datas1 = ["Suzhou_Gaoxinqu1_task.dbf",
                 "Suzhou_Gaoxinqu1_task.prj",
                 "Suzhou_Gaoxinqu1_task.sbn",
                 "Suzhou_Gaoxinqu1_task.sbx",
                 "Suzhou_Gaoxinqu1_task.shp",
                 "Suzhou_Gaoxinqu1_task.shx",
                  "Suzhou_Gaoxinqu1_task.tif",
                  "Suzhou_Gaoxinqu1_task.tif.ovr",
                  "Suzhou_Gaoxinqu1_task.tfw"]
        for ds in datas1:
            insertDataList1.append(self.defaultdir + "/" + ds)

        datas2 = ["Suzhou_Gaoxinqu2_task.dbf",
                 "Suzhou_Gaoxinqu2_task.prj",
                 "Suzhou_Gaoxinqu2_task.sbn",
                 "Suzhou_Gaoxinqu2_task.sbx",
                 "Suzhou_Gaoxinqu2_task.shp",
                 "Suzhou_Gaoxinqu2_task.shx",
                  "Suzhou_Gaoxinqu2_task.tif",
                  "Suzhou_Gaoxinqu2_task.tif.ovr",
                  "Suzhou_Gaoxinqu2_task.tfw"]
        for ds in datas2:
            insertDataList2.append(self.defaultdir + "/" + ds)

        data = {
            "taskId": self.taskid,
            "consumed": 24,
            "workload": 100,
            "description": "SegmentationSplitSubmit",
            "datas": [
                {
                    "content": insertDataList1,
                    "label": "SegmentationSplitSubmit1",
                    "workload": 2
                },
                {
                    "content": insertDataList2,
                    "label": "SegmentationSplitSubmit2",
                    "workload": 2
                }
            ]
        }
        r = requests.post(url=self.url, json=data, headers=self.headers)
        return data,r.status_code

    def ExtractWaterRoadTerrain_1(self):
        self.makeftpdir(self.defaultdir)
        insertDataList = []
        datas = ["Suzhou_Gaoxinqu1_WRT.dbf",
                 "Suzhou_Gaoxinqu1_WRT.prj",
                 "Suzhou_Gaoxinqu1_WRT.sbn",
                 "Suzhou_Gaoxinqu1_WRT.sbx",
                 "Suzhou_Gaoxinqu1_WRT.shp",
                 "Suzhou_Gaoxinqu1_WRT.shx"]
        for ds in datas:
            insertDataList.append(self.defaultdir + "/" + ds)
        data = {
            "taskId": self.taskid,
            "consumed": 24,
            "workload": 100,
            "description": "ExtractWaterRoadTerrain1Submit",
            "datas": [
                {
                    "content": insertDataList,
                    "label": "ExtractWaterRoadTerrain1Submit",
                    "workload": 2
                }
            ]
        }
        r = requests.post(url=self.url, json=data, headers=self.headers)
        return data,r.status_code

    def ExtractWaterRoadTerrain_2(self):
        self.makeftpdir(self.defaultdir)
        insertDataList = []
        datas = ["Suzhou_Gaoxinqu2_WRT.dbf",
                 "Suzhou_Gaoxinqu2_WRT.prj",
                 "Suzhou_Gaoxinqu2_WRT.sbn",
                 "Suzhou_Gaoxinqu2_WRT.sbx",
                 "Suzhou_Gaoxinqu2_WRT.shp",
                 "Suzhou_Gaoxinqu2_WRT.shx"]
        for ds in datas:
            insertDataList.append(self.defaultdir + "/" + ds)
        data = {
            "taskId": self.taskid,
            "consumed": 24,
            "workload": 100,
            "description": "ExtractWaterRoadTerrain2Submit",
            "datas": [
                {
                    "content": insertDataList,
                    "label": "ExtractWaterRoadTerrain2Submit",
                    "workload": 2
                }
            ]
        }
        r = requests.post(url=self.url, json=data, headers=self.headers)
        return data,r.status_code

    def ExtractFarm_1(self):
        self.makeftpdir(self.defaultdir)
        insertDataList = []
        datas = ["Suzhou_Gaoxinqu1_farmland.dbf",
                 "Suzhou_Gaoxinqu1_farmland.prj",
                 "Suzhou_Gaoxinqu1_farmland.shp",
                 "Suzhou_Gaoxinqu1_farmland.shx"]
        for ds in datas:
            insertDataList.append(self.defaultdir + "/" + ds)
        data = {
            "taskId": self.taskid,
            "consumed": 24,
            "workload": 100,
            "description": "ExtractFarm_1Submit",
            "datas": [
                {
                    "content": insertDataList,
                    "label": "ExtractFarm_1Submit",
                    "workload": 2
                }
            ]
        }
        r = requests.post(url=self.url, json=data, headers=self.headers)
        return data,r.status_code

    def ExtractFarm_2(self):
        self.makeftpdir(self.defaultdir)
        insertDataList = []
        datas = ["Suzhou_Gaoxinqu2_farmland.dbf",
                 "Suzhou_Gaoxinqu2_farmland.prj",
                 "Suzhou_Gaoxinqu2_farmland.shp",
                 "Suzhou_Gaoxinqu2_farmland.shx"]
        for ds in datas:
            insertDataList.append(self.defaultdir + "/" + ds)
        data = {
            "taskId": self.taskid,
            "consumed": 24,
            "workload": 100,
            "description": "ExtractFarm_2Submit",
            "datas": [
                {
                    "content": insertDataList,
                    "label": "ExtractFarm_2Submit",
                    "workload": 2
                }
            ]
        }
        r = requests.post(url=self.url, json=data, headers=self.headers)
        return data,r.status_code

    def ExtractWater_1(self):
        self.makeftpdir(self.defaultdir)
        insertDataList = []
        datas = ["Suzhou_Gaoxinqu1_water.dbf",
                 "Suzhou_Gaoxinqu1_water.prj",
                 "Suzhou_Gaoxinqu1_water.shp",
                 "Suzhou_Gaoxinqu1_water.shx"]
        for ds in datas:
            insertDataList.append(self.defaultdir + "/" + ds)
        data = {
            "taskId": self.taskid,
            "consumed": 24,
            "workload": 100,
            "description": "ExtractWater_1Submit",
            "datas": [
                {
                    "content": insertDataList,
                    "label": "ExtractWater_1Submit",
                    "workload": 2
                }
            ]
        }
        r = requests.post(url=self.url, json=data, headers=self.headers)
        return data,r.status_code

    def ExtractWater_2(self):
        self.makeftpdir(self.defaultdir)
        insertDataList = []
        datas = ["Suzhou_Gaoxinqu2_water.dbf",
                 "Suzhou_Gaoxinqu2_water.prj",
                 "Suzhou_Gaoxinqu2_water.shp",
                 "Suzhou_Gaoxinqu2_water.shx"]
        for ds in datas:
            insertDataList.append(self.defaultdir + "/" + ds)
        data = {
            "taskId": self.taskid,
            "consumed": 24,
            "workload": 100,
            "description": "ExtractWater_2Submit",
            "datas": [
                {
                    "content": insertDataList,
                    "label": "ExtractWater_2Submit",
                    "workload": 2
                }
            ]
        }
        r = requests.post(url=self.url, json=data, headers=self.headers)
        return data,r.status_code

    def ExtractBuilding_1(self):
        self.makeftpdir(self.defaultdir)
        insertDataList = []
        datas = ["Suzhou_Gaoxinqu1_build.dbf",
                 "Suzhou_Gaoxinqu1_build.prj",
                 "Suzhou_Gaoxinqu1_build.shp",
                 "Suzhou_Gaoxinqu1_build.shx"]
        for ds in datas:
            insertDataList.append(self.defaultdir + "/" + ds)
        data = {
            "taskId": self.taskid,
            "consumed": 24,
            "workload": 100,
            "description": "ExtractBuilding_1Submit",
            "datas": [
                {
                    "content": insertDataList,
                    "label": "ExtractBuilding_1Submit",
                    "workload": 2
                }
            ]
        }
        r = requests.post(url=self.url, json=data, headers=self.headers)
        return data,r.status_code

    def ExtractBuilding_2(self):
        self.makeftpdir(self.defaultdir)
        insertDataList = []
        datas = ["Suzhou_Gaoxinqu2_build.dbf",
                 "Suzhou_Gaoxinqu2_build.prj",
                 "Suzhou_Gaoxinqu2_build.shp",
                 "Suzhou_Gaoxinqu2_build.shx"]
        for ds in datas:
            insertDataList.append(self.defaultdir + "/" + ds)
        data = {
            "taskId": self.taskid,
            "consumed": 24,
            "workload": 100,
            "description": "ExtractBuilding_2Submit",
            "datas": [
                {
                    "content": insertDataList,
                    "label": "ExtractBuilding_2Submit",
                    "workload": 2
                }
            ]
        }
        r = requests.post(url=self.url, json=data, headers=self.headers)
        return data,r.status_code

    def ExtractForest_1(self):
        self.makeftpdir(self.defaultdir)
        insertDataList = []
        datas = ["Suzhou_Gaoxinqu1_forest.dbf",
                 "Suzhou_Gaoxinqu1_forest.prj",
                 "Suzhou_Gaoxinqu1_forest.shp",
                 "Suzhou_Gaoxinqu1_forest.shx"]
        for ds in datas:
            insertDataList.append(self.defaultdir + "/" + ds)
        data = {
            "taskId": self.taskid,
            "consumed": 24,
            "workload": 100,
            "description": "ExtractForest_1Submit",
            "datas": [
                {
                    "content": insertDataList,
                    "label": "ExtractForest_1Submit",
                    "workload": 2
                }
            ]
        }
        r = requests.post(url=self.url, json=data, headers=self.headers)
        return data,r.status_code

    def ExtractForest_2(self):
        self.makeftpdir(self.defaultdir)
        insertDataList = []
        datas = ["Suzhou_Gaoxinqu2_forest.dbf",
                 "Suzhou_Gaoxinqu2_forest.prj",
                 "Suzhou_Gaoxinqu2_forest.shp",
                 "Suzhou_Gaoxinqu2_forest.shx"]
        for ds in datas:
            insertDataList.append(self.defaultdir + "/" + ds)
        data = {
            "taskId": self.taskid,
            "consumed": 24,
            "workload": 100,
            "description": "ExtractForest_2Submit",
            "datas": [
                {
                    "content": insertDataList,
                    "label": "ExtractForest_2Submit",
                    "workload": 2
                }
            ]
        }
        r = requests.post(url=self.url, json=data, headers=self.headers)
        return data,r.status_code

    def Update_1(self):
        self.makeftpdir(self.defaultdir)
        insertDataList = []
        datas = ["Suzhou_Gaoxinqu1_update.dbf",
                 "Suzhou_Gaoxinqu1_update.prj",
                 "Suzhou_Gaoxinqu1_update.shp",
                 "Suzhou_Gaoxinqu1_update.shx"]
        for ds in datas:
            insertDataList.append(self.defaultdir + "/" + ds)
        data = {
            "taskId": self.taskid,
            "consumed": 24,
            "workload": 100,
            "description": "Update_1Submit",
            "datas": [
                {
                    "content": insertDataList,
                    "label": "Update_1Submit",
                    "workload": 2
                }
            ]
        }
        r = requests.post(url=self.url, json=data, headers=self.headers)
        return data,r.status_code

    def Update_2(self):
        self.makeftpdir(self.defaultdir)
        insertDataList = []
        datas = ["Suzhou_Gaoxinqu2_update.dbf",
                 "Suzhou_Gaoxinqu2_update.prj",
                 "Suzhou_Gaoxinqu2_update.shp",
                 "Suzhou_Gaoxinqu2_update.shx"]
        for ds in datas:
            insertDataList.append(self.defaultdir + "/" + ds)
        data = {
            "taskId": self.taskid,
            "consumed": 24,
            "workload": 100,
            "description": "Update_2Submit",
            "datas": [
                {
                    "content": insertDataList,
                    "label": "Update_2Submit",
                    "workload": 2
                }
            ]
        }
        r = requests.post(url=self.url, json=data, headers=self.headers)
        return data,r.status_code

    def BlockSplit_1(self):
        self.makeftpdir(self.defaultdir)
        insertDataList1 = []
        insertDataList2 = []
        datas1 = ["Suzhou_Gaoxinqu11_block.dbf",
                 "Suzhou_Gaoxinqu11_block.prj",
                 "Suzhou_Gaoxinqu11_block.sbn",
                 "Suzhou_Gaoxinqu11_block.sbx",
                 "Suzhou_Gaoxinqu11_block.shp",
                 "Suzhou_Gaoxinqu11_block.shx"]
        for ds in datas1:
            insertDataList1.append(self.defaultdir + "/" + ds)

        datas2 = ["Suzhou_Gaoxinqu12_block.dbf",
                 "Suzhou_Gaoxinqu12_block.prj",
                 "Suzhou_Gaoxinqu12_block.sbn",
                 "Suzhou_Gaoxinqu12_block.sbx",
                 "Suzhou_Gaoxinqu12_block.shp",
                 "Suzhou_Gaoxinqu12_block.shx"]
        for ds in datas2:
            insertDataList2.append(self.defaultdir + "/" + ds)

        data = {
            "taskId": self.taskid,
            "consumed": 24,
            "workload": 100,
            "description": "BlockSplit_1Submit",
            "datas": [
                {
                    "content": insertDataList1,
                    "label": "BlockSplit_1Submit",
                    "workload": 2
                },
                {
                    "content": insertDataList2,
                    "label": "BlockSplit_1Submit",
                    "workload": 2
                }
            ]
        }
        r = requests.post(url=self.url, json=data, headers=self.headers)
        return data,r.status_code

    def BlockSplit_2(self):
        self.makeftpdir(self.defaultdir)
        insertDataList1 = []
        insertDataList2 = []
        datas1 = ["Suzhou_Gaoxinqu21_block.dbf",
                 "Suzhou_Gaoxinqu21_block.prj",
                 "Suzhou_Gaoxinqu21_block.sbn",
                 "Suzhou_Gaoxinqu21_block.sbx",
                 "Suzhou_Gaoxinqu21_block.shp",
                 "Suzhou_Gaoxinqu21_block.shx"]
        for ds in datas1:
            insertDataList1.append(self.defaultdir + "/" + ds)

        datas2 = ["Suzhou_Gaoxinqu22_block.dbf",
                 "Suzhou_Gaoxinqu22_block.prj",
                 "Suzhou_Gaoxinqu22_block.sbn",
                 "Suzhou_Gaoxinqu22_block.sbx",
                 "Suzhou_Gaoxinqu22_block.shp",
                 "Suzhou_Gaoxinqu22_block.shx"]
        for ds in datas2:
            insertDataList2.append(self.defaultdir + "/" + ds)

        data = {
            "taskId": self.taskid,
            "consumed": 24,
            "workload": 100,
            "description": "BlockSplit_2Submit",
            "datas": [
                {
                    "content": insertDataList1,
                    "label": "BlockSplit_2Submit",
                    "workload": 2
                },
                {
                    "content": insertDataList2,
                    "label": "BlockSplit_2Submit",
                    "workload": 2
                }
            ]
        }
        r = requests.post(url=self.url, json=data, headers=self.headers)
        return data,r.status_code

    def Edit_1(self):
        self.makeftpdir(self.defaultdir)
        insertDataList = []
        datas = ["Suzhou_Gaoxinqu11_edit.dbf",
                 "Suzhou_Gaoxinqu11_edit.prj",
                 "Suzhou_Gaoxinqu11_edit.shp",
                 "Suzhou_Gaoxinqu11_edit.shx"]
        for ds in datas:
            insertDataList.append(self.defaultdir + "/" + ds)
        data = {
            "taskId": self.taskid,
            "consumed": 24,
            "workload": 100,
            "description": "Edit_1Submit",
            "datas": [
                {
                    "content": insertDataList,
                    "label": "Edit_1Submit",
                    "workload": 2
                }
            ]
        }
        r = requests.post(url=self.url, json=data, headers=self.headers)
        return data,r.status_code

    def Edit_2(self):
        self.makeftpdir(self.defaultdir)
        insertDataList = []
        datas = ["Suzhou_Gaoxinqu12_edit.dbf",
                 "Suzhou_Gaoxinqu12_edit.prj",
                 "Suzhou_Gaoxinqu12_edit.shp",
                 "Suzhou_Gaoxinqu12_edit.shx"]
        for ds in datas:
            insertDataList.append(self.defaultdir + "/" + ds)
        data = {
            "taskId": self.taskid,
            "consumed": 24,
            "workload": 100,
            "description": "Edit_2Submit",
            "datas": [
                {
                    "content": insertDataList,
                    "label": "Edit_2Submit",
                    "workload": 2
                }
            ]
        }
        r = requests.post(url=self.url, json=data, headers=self.headers)
        return data,r.status_code

    def Edit_3(self):
        self.makeftpdir(self.defaultdir)
        insertDataList = []
        datas = ["Suzhou_Gaoxinqu21_edit.dbf",
                 "Suzhou_Gaoxinqu21_edit.prj",
                 "Suzhou_Gaoxinqu21_edit.shp",
                 "Suzhou_Gaoxinqu21_edit.shx"]
        for ds in datas:
            insertDataList.append(self.defaultdir + "/" + ds)
        data = {
            "taskId": self.taskid,
            "consumed": 24,
            "workload": 100,
            "description": "Edit_3Submit",
            "datas": [
                {
                    "content": insertDataList,
                    "label": "Edit_3Submit",
                    "workload": 2
                }
            ]
        }
        r = requests.post(url=self.url, json=data, headers=self.headers)
        return data,r.status_code

    def Edit_4(self):
        self.makeftpdir(self.defaultdir)
        insertDataList = []
        datas = ["Suzhou_Gaoxinqu22_edit.dbf",
                 "Suzhou_Gaoxinqu22_edit.prj",
                 "Suzhou_Gaoxinqu22_edit.shp",
                 "Suzhou_Gaoxinqu22_edit.shx"]
        for ds in datas:
            insertDataList.append(self.defaultdir + "/" + ds)
        data = {
            "taskId": self.taskid,
            "consumed": 24,
            "workload": 100,
            "description": "Edit_4Submit",
            "datas": [
                {
                    "content": insertDataList,
                    "label": "Edit_4Submit",
                    "workload": 2
                }
            ]
        }
        r = requests.post(url=self.url, json=data, headers=self.headers)
        return data,r.status_code

    def SecondClassAttributeEdit_1(self):
        self.makeftpdir(self.defaultdir)
        insertDataList = []
        datas = ["Suzhou_Gaoxinqu11_secondClassAttribute.dbf",
                 "Suzhou_Gaoxinqu11_secondClassAttribute.prj",
                 "Suzhou_Gaoxinqu11_secondClassAttribute.shp",
                 "Suzhou_Gaoxinqu11_secondClassAttribute.shx"]
        for ds in datas:
            insertDataList.append(self.defaultdir + "/" + ds)
        data = {
            "taskId": self.taskid,
            "consumed": 24,
            "workload": 100,
            "description": "SecondClassAttributeEdit_1Submit",
            "datas": [
                {
                    "content": insertDataList,
                    "label": "SecondClassAttributeEdit_1Submit",
                    "workload": 2
                }
            ]
        }
        r = requests.post(url=self.url, json=data, headers=self.headers)
        return data,r.status_code

    def SecondClassAttributeEdit_2(self):
        self.makeftpdir(self.defaultdir)
        insertDataList = []
        datas = ["Suzhou_Gaoxinqu12_secondClassAttribute.dbf",
                 "Suzhou_Gaoxinqu12_secondClassAttribute.prj",
                 "Suzhou_Gaoxinqu12_secondClassAttribute.shp",
                 "Suzhou_Gaoxinqu12_secondClassAttribute.shx"]
        for ds in datas:
            insertDataList.append(self.defaultdir + "/" + ds)
        data = {
            "taskId": self.taskid,
            "consumed": 24,
            "workload": 100,
            "description": "SecondClassAttributeEdit_2Submit",
            "datas": [
                {
                    "content": insertDataList,
                    "label": "SecondClassAttributeEdit_2Submit",
                    "workload": 2
                }
            ]
        }
        r = requests.post(url=self.url, json=data, headers=self.headers)
        return data,r.status_code

    def SecondClassAttributeEdit_3(self):
        self.makeftpdir(self.defaultdir)
        insertDataList = []
        datas = ["Suzhou_Gaoxinqu21_secondClassAttribute.dbf",
                 "Suzhou_Gaoxinqu21_secondClassAttribute.prj",
                 "Suzhou_Gaoxinqu21_secondClassAttribute.shp",
                 "Suzhou_Gaoxinqu21_secondClassAttribute.shx"]
        for ds in datas:
            insertDataList.append(self.defaultdir + "/" + ds)
        data = {
            "taskId": self.taskid,
            "consumed": 24,
            "workload": 100,
            "description": "SecondClassAttributeEdit_3Submit",
            "datas": [
                {
                    "content": insertDataList,
                    "label": "SecondClassAttributeEdit_3Submit",
                    "workload": 2
                }
            ]
        }
        r = requests.post(url=self.url, json=data, headers=self.headers)
        return data,r.status_code

    def SecondClassAttributeEdit_4(self):
        self.makeftpdir(self.defaultdir)
        insertDataList = []
        datas = ["Suzhou_Gaoxinqu22_secondClassAttribute.dbf",
                 "Suzhou_Gaoxinqu22_secondClassAttribute.prj",
                 "Suzhou_Gaoxinqu22_secondClassAttribute.shp",
                 "Suzhou_Gaoxinqu22_secondClassAttribute.shx"]
        for ds in datas:
            insertDataList.append(self.defaultdir + "/" + ds)
        data = {
            "taskId": self.taskid,
            "consumed": 24,
            "workload": 100,
            "description": "SecondClassAttributeEdit_4Submit",
            "datas": [
                {
                    "content": insertDataList,
                    "label": "SecondClassAttributeEdit_4Submit",
                    "workload": 2
                }
            ]
        }
        r = requests.post(url=self.url, json=data, headers=self.headers)
        return data,r.status_code

    def Merge(self):
        self.makeftpdir(self.defaultdir)
        insertDataList = []
        datas = ["Suzhou_Gaoxinqu_result.dbf",
                 "Suzhou_Gaoxinqu_result.prj",
                 "Suzhou_Gaoxinqu_result.shp",
                 "Suzhou_Gaoxinqu_result.shx"]
        for ds in datas:
            insertDataList.append(self.defaultdir + "/" + ds)
        data = {
            "taskId": self.taskid,
            "consumed": 24,
            "workload": 100,
            "description": "MergeSubmit",
            "datas": [
                {
                    "content": insertDataList,
                    "label": "MergeSubmit",
                    "workload": 2
                }
            ]
        }
        r = requests.post(url=self.url, json=data, headers=self.headers)
        return data,r.status_code

    def check_finish(self):
        url = "http://bt1.geosts.ac.cn/api/dcpp/dcpp/rest/v1/task/" + self.taskid + "/finish"
        payload = {"workload": "200",
                   "comsumed": "100",
                   "score": "10",
                   "evaluation":"good"}
        fh = requests.post(url, params=payload,headers=self.headers)
        return fh.status_code

    def check_return(self):
        insertDataList = []
        datas = ["check.dbf",
                 "check.prj",
                 "check.shp",
                 "check.shx"]
        for ds in datas:
            insertDataList.append(self.defaultdir + "/" + ds)
        data ={
            "consumed": 24,
            "datas": [
                {
                    "content": insertDataList,
                    "label": "checkSubmit",
                    "workload": 2
                }
            ],
            "description": "checkSubmit",
            "taskId": self.taskid,
            "workload": 100
        }
        r = requests.post(url=self.url, json=data, headers=self.headers)
        return data,r.status_code

def getTaskName(key,taskL):
    for tsk in taskL:
        if tsk["key"] == key:
            return tsk["name"]

#获取用户的token信息
shtId = 35
f = open("log/sheetId" + str(shtId) + 'log.json','a+')
token = API.get_token()
#获取任务列表
taskList = API.taskList(sheetId=shtId,owner=146)
#打印任务列表信息
# print(taskList,file=f)
print("{0}本次查询共有{1}个任务".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), len(taskList)),file=f)
for tt in taskList:
    print(tt["name"], ":", tt["key"],"，质检:",tt["qcTask"])
    print(tt["name"],":",tt["key"],file=f)

for t in taskList:
    print("这是第{0}个任务".format(str(taskList.index(t)+1)),file=f)
    print(json.dumps(t,sort_keys=True,indent=4,separators=(',', ': '),ensure_ascii=False),file=f)
    print("======================任务分隔线============================",file=f)

# 输入领取的任务key id
taskid = input("输入任务key id:")
#根据输入的任务key ，领取任务，并返回数据的输出路径
preview,dir = API.getTask(taskid=taskid,token=token)
txtfile= getTaskName(taskid,taskList) + taskid + ".json"
txtf = open("log/" + txtfile, 'a+')

print("{0}任务领取内容:".format(getTaskName(taskid,taskList)),file=f)
print("{0}任务领取内容:".format(getTaskName(taskid,taskList)),file=txtf)

print(json.dumps(preview,sort_keys=True,indent=4,separators=(',', ': '),ensure_ascii=False),file=f)
print(json.dumps(preview,sort_keys=True,indent=4,separators=(',', ': '),ensure_ascii=False),file=txtf)
#初始化任务提交类
test = landuseTest(taskid,token,dir)

print("{0}任务提交内容:".format(getTaskName(taskid,taskList)),file=f)
print("{0}任务提交内容:".format(getTaskName(taskid,taskList)),file=txtf)

# submit=json.dumps(test.ModelFarm(),sort_keys=True,indent=4,separators=(',', ': '),ensure_ascii=False)
# submit=json.dumps(test.ModelBuilding(),sort_keys=True,indent=4,separators=(',', ': '),ensure_ascii=False)
# submit=json.dumps(test.ModelForest(),sort_keys=True,indent=4,separators=(',', ': '),ensure_ascii=False)
# submit=json.dumps(test.ModelWater(),sort_keys=True,indent=4,separators=(',', ': '),ensure_ascii=False)

# submit=json.dumps(test.DEM(),sort_keys=True,indent=4,separators=(',', ': '),ensure_ascii=False)
# submit=json.dumps(test.Image(),sort_keys=True,indent=4,separators=(',', ': '),ensure_ascii=False)
# submit=json.dumps(test.Ref(),sort_keys=True,indent=4,separators=(',', ': '),ensure_ascii=False)
# submit=json.dumps(test.TaskArea(),sort_keys=True,indent=4,separators=(',', ': '),ensure_ascii=False)

# submit=json.dumps(test.ImageService(),sort_keys=True,indent=4,separators=(',', ': '),ensure_ascii=False)
# submit=json.dumps(test.LanduseClassificationPrepare(),sort_keys=True,indent=4,separators=(',', ': '),ensure_ascii=False)
# submit=json.dumps(test.checkClassificationPrepare(),sort_keys=True,indent=4,separators=(',', ': '),ensure_ascii=False)
#————————截止——————————————
# submit=json.dumps(test.DEMcalculate(),sort_keys=True,indent=4,separators=(',', ': '),ensure_ascii=False)
# submit=json.dumps(test.vectorSegmentation(),sort_keys=True,indent=4,separators=(',', ': '),ensure_ascii=False)
# submit=json.dumps(test.SegmentationSplit(),sort_keys=True,indent=4,separators=(',', ': '),ensure_ascii=False)

# submit=json.dumps(test.ExtractWaterRoadTerrain_1(),sort_keys=True,indent=4,separators=(',', ': '),ensure_ascii=False)
# submit=json.dumps(test.ExtractWaterRoadTerrain_2(),sort_keys=True,indent=4,separators=(',', ': '),ensure_ascii=False)

# submit=json.dumps(test.ExtractFarm_1(),sort_keys=True,indent=4,separators=(',', ': '),ensure_ascii=False)
# submit=json.dumps(test.ExtractFarm_2(),sort_keys=True,indent=4,separators=(',', ': '),ensure_ascii=False)

# submit=json.dumps(test.ExtractWater_1(),sort_keys=True,indent=4,separators=(',', ': '),ensure_ascii=False)
# submit=json.dumps(test.ExtractWater_2(),sort_keys=True,indent=4,separators=(',', ': '),ensure_ascii=False)

# submit=json.dumps(test.ExtractBuilding_1(),sort_keys=True,indent=4,separators=(',', ': '),ensure_ascii=False)
# submit=json.dumps(test.ExtractBuilding_2(),sort_keys=True,indent=4,separators=(',', ': '),ensure_ascii=False)

# submit=json.dumps(test.ExtractForest_1(),sort_keys=True,indent=4,separators=(',', ': '),ensure_ascii=False)
# submit=json.dumps(test.ExtractForest_2(),sort_keys=True,indent=4,separators=(',', ': '),ensure_ascii=False)

# submit=json.dumps(test.Update_1(),sort_keys=True,indent=4,separators=(',', ': '),ensure_ascii=False)
# submit=json.dumps(test.Update_2(),sort_keys=True,indent=4,separators=(',', ': '),ensure_ascii=False)

# submit=json.dumps(test.BlockSplit_1(),sort_keys=True,indent=4,separators=(',', ': '),ensure_ascii=False)
# submit=json.dumps(test.BlockSplit_2(),sort_keys=True,indent=4,separators=(',', ': '),ensure_ascii=False)
####
# submit=json.dumps(test.Edit_1(),sort_keys=True,indent=4,separators=(',', ': '),ensure_ascii=False)
# submit=json.dumps(test.Edit_2(),sort_keys=True,indent=4,separators=(',', ': '),ensure_ascii=False)
# submit=json.dumps(test.Edit_3(),sort_keys=True,indent=4,separators=(',', ': '),ensure_ascii=False)
# submit=json.dumps(test.Edit_4(),sort_keys=True,indent=4,separators=(',', ': '),ensure_ascii=False)

# submit=json.dumps(test.SecondClassAttributeEdit_1(),sort_keys=True,indent=4,separators=(',', ': '),ensure_ascii=False)
# submit=json.dumps(test.SecondClassAttributeEdit_2(),sort_keys=True,indent=4,separators=(',', ': '),ensure_ascii=False)
# submit=json.dumps(test.SecondClassAttributeEdit_3(),sort_keys=True,indent=4,separators=(',', ': '),ensure_ascii=False)
# submit=json.dumps(test.SecondClassAttributeEdit_4(),sort_keys=True,indent=4,separators=(',', ': '),ensure_ascii=False)

# submit=json.dumps(test.Merge(),sort_keys=True,indent=4,separators=(',', ': '),ensure_ascii=False)

#质检
# submit=json.dumps(test.check_finish(),sort_keys=True,indent=4,separators=(',', ': '),ensure_ascii=False)
# submit=json.dumps(test.check_return(),sort_keys=True,indent=4,separators=(',', ': '),ensure_ascii=False)
print(submit,file=txtf)
print(submit,file=f)
print("=============={0}任务执行结束。=================\n\n\n".format(getTaskName(taskid,taskList)),file=f)
print("=============={0}任务执行结束。=================\n\n\n".format(getTaskName(taskid,taskList)),file=txtf)
txtf.close()
f.close()
