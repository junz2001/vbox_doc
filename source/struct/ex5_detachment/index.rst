滑脱层
======

这里是一个 ``滑脱层`` 设置的实例，一般地，将滑脱层设置为没有粘结，类似松散石英砂，摩擦系数则可以设置为 0.0。

 ``ex5`` 目录中文件有
 
- `lsf.sh <lsf.sh>`_
- `detachment.py <detachment.py>`_
- `init_xyr.dat <init_xyr.dat>`_



## 进入 `ex5` 目录，在终端或 `xshell` 中运行 ::

   $ bsub < lsf.sh   # 提交计算
   $ bjobs           # 查看计算是否提交成功


``lsf.sh`` 中内容如下：

.. literalinclude:: lsf.sh

``detachment.py`` 中内容如下：

.. literalinclude:: detachment.py

计算结束后，将得到以下结果：


.. only:: html

   .. figure:: detachment.gif
      :width: 60%
      :align: center


.. figure:: 00.jpg
  :width: 60%
  :align: center

.. figure:: 05.jpg
  :width: 60%
  :align: center

.. figure:: 10.jpg
  :width: 60%
  :align: center

  **单位(km)**


参考文献

 #. `李长圣，尹宏伟. 滑脱层强度对挤压构造的影响:离散元数值模拟[A]. 2017中国地球科学联合学术年会论文集,2017:4. <http://t.cn/E6k57Mg>`_




