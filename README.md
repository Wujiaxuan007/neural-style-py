# 神经风格迁移服务（TensorFlow 1.6）


## 接口

![wpsXfrinr](https://user-images.githubusercontent.com/41990342/150713780-8b427024-8a08-4869-8323-1ef6828cff98.jpg)


入参：`model_file`（模型名称，请看模型对照表）、`image_file`（待迁移风格的图片）

返回：`content_image_base64`，生成图片的 base64


## 模型对照表

| **model_file**  | **风格类型**                                                 | **待迁移风格的图片**                                         | **生成例子**                                                 |
| --------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| cubist          | ![wpsB8pH2l](https://user-images.githubusercontent.com/41990342/150713959-b2839f45-a95c-448a-9f9a-760b4072cfe2.png) | ![wpssQF2I4](https://user-images.githubusercontent.com/41990342/150713987-bb042db4-6b3f-4b38-b0ad-ca6c1ca3de13.png) | ![wps2GoInj](https://user-images.githubusercontent.com/41990342/150714008-edde9094-0dcb-41fc-9ac7-8809358da8f5.png) |
| scream          | ![wpsy84lhY](https://user-images.githubusercontent.com/41990342/150714027-ab369545-f26f-49e7-a794-1bcf4315a689.png) | ![wpsPlIEWF](https://user-images.githubusercontent.com/41990342/150714047-4502cccf-7961-4f1d-b57e-c3d1a5b4d646.png) | ![wpsoXC7o8](https://user-images.githubusercontent.com/41990342/150714071-d9a8c210-a2e9-486b-bbf9-fd251de8dc8e.png) |
| denoised_starry | ![wpsCWWF5a](https://user-images.githubusercontent.com/41990342/150714089-10049eec-f00a-4810-8a7d-d97bf36d3507.png) | ![wpsiQzWVs](https://user-images.githubusercontent.com/41990342/150714099-027b1be4-fbb6-4b54-a197-8e28bbfd58c2.png) | ![wps5Kzpg7](https://user-images.githubusercontent.com/41990342/150714108-374a3097-1c24-4e09-8a45-5caa1d8ebf67.png) |
| feathers        | ![wpsoTY4i1](https://user-images.githubusercontent.com/41990342/150714124-9a954e17-8edb-45b4-ba75-4626978e5bcf.png) | ![wps23pkxS](https://user-images.githubusercontent.com/41990342/150714134-afc18f3e-c9b9-4803-b3d5-4ce51681a15f.png) | ![wpss6cxTy](https://user-images.githubusercontent.com/41990342/150714590-4c7878af-f911-4695-b223-b7fd3c56e8f3.png) |
| mosaic          | ![wps1iCiDh](https://user-images.githubusercontent.com/41990342/150714192-45ed5efe-e86a-475b-acde-9bdfae3e78ff.png) | ![wpsZxssM1](https://user-images.githubusercontent.com/41990342/150714213-cd9741d5-70d4-4297-8d3c-7afc6255b4e1.png) | ![wps3LVX7H](https://user-images.githubusercontent.com/41990342/150714234-243fd148-c7f1-4328-968c-f7402f8eede8.png) |
| wave            | ![wps8oEZBz](https://user-images.githubusercontent.com/41990342/150714250-af8b94bc-52d7-4e0e-9517-f4a9ef859750.png) | ![wps8VeGLo](https://user-images.githubusercontent.com/41990342/150714261-86971c07-ba14-4bbc-a209-08fa65c8ef67.png) | ![wpsNr1Ds1](https://user-images.githubusercontent.com/41990342/150714274-85e1da65-315a-464e-ac85-6c27ecfd4530.png) |
| udnie           | ![wpsU0kAFM](https://user-images.githubusercontent.com/41990342/150714330-0d5b71d9-f18f-47b0-ae48-425c5f7aafb2.png)| ![wpsEOpky3](https://user-images.githubusercontent.com/41990342/150714704-df63b662-0b93-4ab4-800a-4357cea3df42.png)| ![wpsweWunZ](https://user-images.githubusercontent.com/41990342/150714347-287a0be1-65ea-459b-bd29-ba559cde1a5c.png)


## 训练

### 1）准备工作

- `_server`和之前使用与修改一下，参考上述《模型对照表》

- `_train`是训练代码

![image](https://user-images.githubusercontent.com/41990342/150714994-acedec10-e052-47ed-a9fe-83462e9c7d77.png)

### 2）准备数据

- 网盘下载`trian2014`并解压到某一路径。
- 新准备一张风格图片保存到`neural-style_train\img`，将其名字改为有意义的英文名，后面以`candy`为例，建议找风格强烈的图
  ![image](https://user-images.githubusercontent.com/41990342/150715113-dfd26895-7fd6-4632-8383-4f32d9c8bb26.png)

### 3）训练参数修改

#### 3.1 数据集路径修改：

将`D:/wjx/train2014/train2014/`修改为你解压后的train2014路径

![image](https://user-images.githubusercontent.com/41990342/150715200-3ba842b0-917a-49bc-8603-8f51a6ff1782.png)

#### 3.2 学习率（不建议乱改）:

![image](https://user-images.githubusercontent.com/41990342/150715221-f7b83424-2649-46cb-baeb-fc0308077a9f.png)

#### 3.3 每多少次保存一次模型：
可以稍微改大一点

![image](https://user-images.githubusercontent.com/41990342/150715247-103bc30a-13c8-48f3-8674-d0a67a0f5008.png)

### 4）填写neural-style_server\conf\candy.yml

#### 4.1 基础配置

- `style_image`:风格图片的路径
- `madel_path`:模型保存的路径
- `naming`：模型保存的文件夹名，这里填“candy”，成功训练后你会在model/candy中看到对应模型的生成

![image](https://user-images.githubusercontent.com/41990342/150715395-10abee87-a9f7-4270-b35f-c6f96c199710.png)

#### 4.2 权重的配置

建议只改`style_weight`，50-300
![image](https://user-images.githubusercontent.com/41990342/150715403-278cc982-93b0-4a7a-b029-97d0932f7bdc.png)

#### 4.3 其他配置

- `image_size` 不建议修改
-  `batch_size`：训练批数量，根据 gpu 的好坏增大或减小，我这边机器不好2或4勉强能接受，建议2的次方。
- `epoch`：把训练集也就是 `train2014`，的每张图片完整的训练两遍。建议在资源和时间充沛的情况下，可将其调大,那保存模型的频率可以在`train.py`将其调大。

剩下的不建议修改，可以参考 conf 文件夹下的 yml 文件
![image](https://user-images.githubusercontent.com/41990342/150715415-063cc52f-7523-4e63-9985-adf4586d3c24.png)

### 5）开始训练

#### 5.1 执行命令

```shell
python train.py -c conf/candy.yml
```

![image](https://user-images.githubusercontent.com/41990342/150715635-1fa2816b-fff4-4e61-9b66-98aaa3b30795.png)

报错的话，要么 gpu 不够给力，建议调小 `bitch_size`，要么路径之类的不对，好好检查一下。

#### 5.2 生成模型

![image](https://user-images.githubusercontent.com/41990342/150715695-21eb75ae-0a07-4680-986f-e3618c1bb63c.png)

### 6）Tensorboard

#### 6.1 执行命令

```shell
tensorboard --logdir models/candy/
```



![image](https://user-images.githubusercontent.com/41990342/150715794-fec6b606-b8ca-4688-995b-24f0c6e493ed.png)

#### 6.2 查看 Tensorboard

浏览器访问：http://{ip地址}:6006
