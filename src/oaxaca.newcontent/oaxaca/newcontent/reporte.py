# -*- coding: utf-8 -*-

from five import grok
from zope import schema
from plone.directives import form, dexterity

from plone.app.textfield import RichText
from plone.namedfile.field import NamedBlobFile
from zope.component import getMultiAdapter

from z3c.relationfield.schema import RelationList, RelationChoice
from plone.formwidget.contenttree import ObjPathSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.schema.interfaces import IVocabularyFactory

from z3c.formwidget.query.interfaces import IQuerySource
from zope.component import queryUtility

from plone.formwidget.masterselect import (
    _,
    MasterSelectField,
    MasterSelectBoolField,
)

from oaxaca.newcontent import ContentMessageFactory as _
from oaxaca.newcontent.config import OAXACA


def getSlaveVocab(municipio_id):
    print municipio_id
    municipios_list = sorted(OAXACA.keys())
    municipio_nombre = municipios_list[int(municipio_id)]
    localidades = []
    if municipio_nombre in OAXACA:
        localidades = sorted(OAXACA[municipio_nombre])
    return SimpleVocabulary(
        [SimpleTerm(value=localidades.index(l), title=l) for l in localidades]
    )


class IReporte(form.Schema):

    """A  Reporte.
    """

    quien = schema.TextLine(
            title=_(u"Persona o entidad que presenta este reporte"),
            required=False,
        )

    cuerpo = RichText(
            title=_(u"Observaciones acerca del reporte"),
            required=False
        )

    fecha = schema.Date(
            title=_(u"Fecha"),
            description=_(u"Fecha en que presenta este reporte"),
            required=False
        )

    unidad = schema.Choice(
            title=_(u"Unidad"),
            description=_(u"Seleccione la unidad sobre la que se reporta"),
            values=(
                u'utiles escolares',
                u'uniformes escolares',
                u'tarjetas',),
            required=False
        )

    municipio = MasterSelectField(
            title=_(u"Municipio"),
            description=_(u"Seleccione el municipio donde se entregaron las unidades reportadas"),
            required=False,
            vocabulary="oaxaca.newcontent.municipios",
            slave_fields=(
                {'name': 'localidad',
                 'action': 'vocabulary',
                 'vocab_method': getSlaveVocab,
                 'control_param': 'municipio_id',
                },
            )
        )

    localidad = schema.Choice(
        title=_(u"Localidad"),
        description=_(u"Seleccione la localidad donde se entregaron las unidades reportadas"),
        values=[u'',],
        required=False,
    )

    uniAsignadas = schema.Int(
            title=_(u"Unidades asignadas"),
            required=False
        )

    uniEntregadas = schema.Int(
            title=_(u"Unidades entregadas"),
            required=False
        )

    beneficiarios = schema.Int(
            title=_(u"Cantidad de personas beneficiadas"),
            required=False
        )

    uniPorEntregar = schema.Int(
            title=_(u"Unidades por entregar"),
            required=False
        )

    anexo = NamedBlobFile(
            title=_(u"Anexo"),
            description=_(u"Anexe archivo electrónico si su reporte lo amerita."),
            required=False
        )
