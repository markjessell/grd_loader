# -*- coding: utf-8 -*-
"""
/***************************************************************************
 GrdLoader
                                 A QGIS plugin
 Load GRD Format Rasters
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2023-05-11
        copyright            : (C) 2023 by Mark Jessell
        email                : mark.jessell@uwa.edu.au
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load GrdLoader class from file GrdLoader.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .GRD_Loader import GrdLoader
    return GrdLoader(iface)
