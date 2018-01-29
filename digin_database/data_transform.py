# -*- coding: utf-8 -*-
"""
Created on Apr 23, 2012

@author: timekeeper
"""

from io import StringIO
from lxml import etree

def getFieldName(select_desc=()):
    """
    Extracting field names from description of the select - results
    input: select_desc - tuple of select - description
    """
    field_names = []
    if len(select_desc) > 0:
        try:
            for desc_row in select_desc:
                field_names.append(desc_row[0])
        except Exception as e:
            raise e
    return tuple(field_names)


def printTable(matrix=(), desc=()):
    """
    Printing select - results in table format
    input data: matrix() - tuple of select - result
    fields() - tuple of field names
    """
    row_str = ""
    field_str = ""

    fields = getFieldName(desc)

    for i in range(len(fields)):
        field_str += "%40s" % (str(fields[i]))  # forming title from field names
    print(field_str + "\n")

    for row in matrix:
        for i in range(len(row)):
            row_str += "%40s" % (str(row[i]))  # forming row of printing table
        print(row_str)
        row_str = ""


def getTableAsString(matrix=(), fields=()):
    """
    Printing select - results in table format
    input data: matrix() - tuple of select - result
                fields() - tuple of field names
    """
    row_str = ""
    table = ""
    if len(fields) > 0:
        for i in range(len(fields)):
            table += "%40s" % (str(fields[i]))  # forming title from field names

        table += "\n" + "\n"

    for row in matrix:
        for i in range(len(row)):
            row_str += "%40s" % (str(row[i]))  # forming row of printing table
        table += row_str + "\n"
        row_str = ""

    return table


def getTransposeTableAsString(matrix=(), fields=()):
    """
    Printing select - results in table format
    input data: matrix() - tuple of select - result
                fields() - tuple of field names
    """
    table = ""
    for row in matrix:
        if len(fields) > 0:
            for j in range(len(fields)):
                table += "%25s" % (str(fields[j]))  # forming title from field names
                table += "%25s \n" % (str(row[j]))  # forming row of printing table
            table += "\n" + "\n"
            j = 0
    return table


def getTableAsHtml(matrix=(), fields=()):
    """
    Printing select - results in table format
    input data: matrix() - tuple of select - result
                fields() - tuple of field names
    """
    row_str = ""
    table = "<table border>"
    # Table title
    if len(fields) > 0:
        table += "<tr>"
        for i in range(len(fields)):
            table += "<th align='right'>%s</th>" % (str(fields[i]))  # forming title from field names

        table += "</tr>"

    # Table body
    for row in matrix:
        table += "<tr>"
        for i in range(len(row)):
            row_str += "<td align='right'>%40s</td>" % (str(row[i]))  # forming row of printing table
        table += row_str + "</tr>"
        row_str = ""

    table += "</table>"
    return table


def get_xml(unit, root=('root',)):
    """
    Преобразовывает кортеж в xml-строку
    на вход подается двумерный кортеж: первый элемент - данные
                                       второй элемент - список полей
    """
    try:
        sdata, desc = unit

        root = etree.Element(root)
        for row in sdata:
            elem = etree.SubElement(root, "unit")
            for i in range(len(row)):
                etree.SubElement(elem, desc[i][0]).text = str(row[i])
        handle = etree.tostring(root, pretty_print=True, encoding='utf-8', xml_declaration=True)
    except Exception as exc:
        raise exc
    return handle


def pars_xml(source, sep="unit"):
    """
    Преобразовывает xml-строку в кортеж
    В качестве специального разделителя использует переменную sep
    """
    unit = {}
    result = []
    context = etree.iterparse(StringIO(source))

    for action, elem in context:
        if not elem.text:
            text = "None"
        elif (elem.tag != sep):
            text = elem.text
            unit[elem.tag] = text
        elif (elem.tag == sep):
            result.append(unit)
            unit = {}

    return tuple(result)