==================
MRP Lot Attributes
==================

.. !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! This file is generated by oca-gen-addon-readme !!
   !! changes will be overwritten.                   !!
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. |badge1| image:: https://img.shields.io/badge/maturity-Beta-yellow.png
    :target: https://odoo-community.org/page/development-status
    :alt: Beta
.. |badge2| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |badge3| image:: https://img.shields.io/badge/github-jobiols%2Fcl--amic-lightgray.png?logo=github
    :target: https://github.com/jobiols/cl-amic/tree/11.0/mrp_lot_attributes
    :alt: jobiols/cl-amic

|badge1| |badge2| |badge3| 

Este modulo extiende la funcionalidad de los lotes agregando atributos y
comportamientos.

Los atributos del lote son propagados de un lote entrante a un lote saliente
en produccion al oprimir el boton record_production

Peso de los productos en remito
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

En cada linea del remito se muestra la cantidad de producto y el peso. Como
los productos remitidos pueden ser medios que contienen una cantidad no siempre
definida de productos, el peso debe ser calculado al momento de la fabricacion.

Un caso de uso de este problema es el remito de los capachos que van a thermal,
se requiere tener el peso del capacho en el remito. Para eso se define el
siguiente metodo de calculo.

El peso de un producto que tiene seguimiento por lotes esta definido en el
lote, y se calcula al fabricar el producto sumando los pesos de los productos
componentes, que a su vez tambien estan en los lotes.

De esta manera se calculan los pesos de todos los productos de la cadena de
fabricacion desde la materia prima.

Si un producto tiene definido su peso en el apartado **Inventario** de la ficha
del producto, entonces se toma ese peso en lugar del peso definido en el lote.
Esto ultimo se usa para definir el peso del primer producto de la cadena de
fabricacion o el producto desde donde se quiere empezar a definir pesos.

**Table of contents**

.. contents::
   :local:

Configuration
=============

To configure this module, you need to:

#. Go to ...

.. figure:: https://raw.githubusercontent.com/jobiols/cl-amic/11.0/mrp_lot_attributes/static/description/icon.png
   :alt: alternative description
   :width: 60 px

Usage
=====

Los lotes se crean con el numero de orden de trabajo para poder seguir la OT

Changelog
=========

11.0.0.0.0 (2019-09-12)
~~~~~~~~~~~~~~~~~~~~~~~

* [WIP] Commit inicial del modulo soporte de atributos.

11.0.0.0.0 (2019-09-24)
~~~~~~~~~~~~~~~~~~~~~~~

* [WIP] comportamiento especial de los lotes.
  (`#1 <https://github.com/jobiols/cl-amic/issues/1>`_)

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/jobiols/cl-amic/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us smashing it by providing a detailed and welcomed
`feedback <https://github.com/jobiols/cl-amic/issues/new?body=module:%20mrp_lot_attributes%0Aversion:%2011.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Do not contact contributors directly about support or help with technical issues.

Credits
=======

Authors
~~~~~~~

* jeo Software

Contributors
~~~~~~~~~~~~

* Jorge Obiols <jorge.obiols@gmail.com> (www.jeosoft.com.ar)

Other credits
~~~~~~~~~~~~~

El desarrollo de este modulo fue financiado por:

* ArqyTec
* AMIC

Maintainers
~~~~~~~~~~~

.. |maintainer-jobiols| image:: https://github.com/jobiols.png?size=40px
    :target: https://github.com/jobiols
    :alt: jobiols

Current maintainer:

|maintainer-jobiols| 

This module is part of the `jobiols/cl-amic <https://github.com/jobiols/cl-amic/tree/11.0/mrp_lot_attributes>`_ project on GitHub.

You are welcome to contribute.
