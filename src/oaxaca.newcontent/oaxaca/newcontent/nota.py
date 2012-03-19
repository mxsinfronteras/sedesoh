# -*- coding: utf-8 -*-

from five import grok
from zope import schema
from plone.directives import form, dexterity

from zope.component import getMultiAdapter
from plone.namedfile.interfaces import IImageScaleTraversable
from plone.namedfile.field import NamedBlobFile, NamedBlobImage
from plone.app.textfield import RichText
from plone.z3cform.textlines.textlines import TextLinesFieldWidget

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


class INota(form.Schema, IImageScaleTraversable):

    """A nota.
    """

    cuerpo = RichText(
            title=_(u"Cuerpo de la nota"),
            required=False
        )

    fecha = schema.Date(
            title=_(u"Fecha"),
            description=_(u"Seleccione fecha de publicacion de la nota"),
            required=False
        )

    municipio = MasterSelectField(
            title=_(u"Municipio"),
            description=_(u"Seleccione el municipio donde ocurrió el hecho reportado"),
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
        description=_(u"Seleccione la localidad donde ocurrió el hecho reportado."),
        values=[u'',],
        required=False,
    )

    actores = schema.Text(
            title=_(u'Personas, agrupaciones o dependencias mencionadas'),
            required=False,
            description=_(u'Utilice una línea para cada nombre'),
        )
    form.widget(actores = TextLinesFieldWidget)
    actores = schema.List(
            title=_(u"Actores"),
            description=_(u"Liste personas, agrupaciones o instituciones mencionadoas. Utilice una línea por cada una."),
            default = [],
            value_type = schema.TextLine(),
            required = False,
        )

    fuente = schema.Choice(
            title=_(u"Fuente"),
            description=_(u"Seleccione la publicación donde apareció la nota"),
            required=False,
            values=(
                u'A Diario',
                u'ADN Sureste',
                u'Despertar',
                u'Despertar de la Costa',
                u'Diario Acontecer',
                u'Diario Oaxaca',
                u'Enfoque Diario',
                u'e-Consulta',
                u'e-Oaxaca',
                u'Foro Politico',
                u'El Imparcial',
                u'Libertad Oaxaca',
                u'Marca',
                u'Noticias',
                u'NSS Oaxaca',
                u'Oaxacain',
                u'Pagina 3',
                u'El Pinero',
                u'Punto',
                u'Punto Critico',
                u'Quadratin',
                u'Realidad',
                u'El Sol del Istmo',
                u'El Sol de la Costa',
                u'El Sur',
                u'Tiempo',
                u'El Tuxtepecano',
                u'Voz del Sur',)
        )

    otraFuente = schema.TextLine(
            title=(u"Fuente adicional"),
            description=_(u"Anote el nombre de la fuente si no se lista arriba"),
            required=False
        )

    firma = schema.TextLine(
            title=_(u"Persona o agencia que firma la nota"),
            required=False
        )

    seccion = schema.Choice(
            title=_(u"Sección"),
            required=False,
            values=(
                u'Primera plana',
                u'Gobierno estatal',
                u'Gobierno federal',
                u'Problemas sociales',
                u'Economia',
                u'Municipios',
                u'Partidos',
                u'Organizaciones',
                u'Congreso',
                u'Elecciones',
                u'Columnas',
                u'Editorial',
                u'Deportes',
                u'Otra',)
        )

    enlace = schema.URI(
            title=(u"Enlace"),
            description=(u"Anote el URL completo de la nota empezando con http://"),
            required=False
        )

    anexo1 = NamedBlobImage(
            title=_(u"Anexo"),
            description=_(u"Si la nota fue escaneada como imagen, use este campo para anexarla"),
            required=False
        )
