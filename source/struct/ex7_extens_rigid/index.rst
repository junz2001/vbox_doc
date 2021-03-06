刚性基底 伸展构造
=================

这里是一个 ``刚性基底 伸展构造`` 设置的实例，使用上下两个刚性板完成。

 ``ex7`` 目录中文件有
 
- `lsf.sh <lsf.sh>`_
- `extens_rigid.py <palaeohigh.py>`_
- `init_xyr.dat <init_xyr.dat>`_



## 进入 `ex7` 目录，在终端或 `xshell` 中运行 ::

   $ bsub < lsf.sh   # 提交计算
   $ bjobs           # 查看计算是否提交成功


``lsf.sh`` 中内容如下：

.. literalinclude:: lsf.sh

``extens_rigid.py`` 中内容如下：

.. literalinclude:: extens_rigid.py

计算结束后，将得到以下结果：


.. only:: html

   .. figure:: extens_rigid.gif
      :width: 60%
      :align: center


.. figure:: 00.jpg
  :width: 60%
  :align: center

.. figure:: 02.jpg
  :width: 60%
  :align: center

.. figure:: 04.jpg
  :width: 60%
  :align: center

.. figure:: 06.jpg
  :width: 60%
  :align: center

.. figure:: 08.jpg
  :width: 60%
  :align: center

  **单位(km)**


参考文献

 #. 李长圣，尹宏伟*，张佳星，汪伟. 琼东南盆地基底断层性质对凹陷沉积模式的影响：基于离散元数值模拟的认识. **2018中国地球科学联合学术年会论文集**, 北京, 2018.



