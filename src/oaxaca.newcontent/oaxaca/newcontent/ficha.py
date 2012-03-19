# -*- coding: utf-8 -*-

from five import grok
from zope import schema
from plone.directives import form, dexterity

from zope.component import getMultiAdapter
from plone.namedfile.interfaces import IImageScaleTraversable
from plone.namedfile.field import NamedBlobFile, NamedBlobImage
from plone.z3cform.textlines.textlines import TextLinesFieldWidget
from z3c.form.browser.checkbox import CheckBoxFieldWidget

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


class IFicha(form.Schema, IImageScaleTraversable):
    """Describes a ficha
    """


    form.widget(tipoMenu = CheckBoxFieldWidget)
    tipoMenu = schema.List(
            title=_(u"Tipo de evento"),
            description=_(u"Marque la opción que aplique o "
                           "seleccione otro si ninguna aplica."),
            value_type=schema.Choice(
            values=(
                (u'Manifestacion en lugar publico'),
                (u'Toma de instalaciones municipales'),
                (u'Toma de instalaciones estatales'),
                (u'Toma de instalaciones federales'),
                (u'Bloqueo de carretera municipal'),
                (u'Bloqueo de carretera estatal'),
                (u'Bloqueo de carretera federal'),
                (u'Secuestro de funcionario'),
                (u'Otro')),
            required=False,
        ))

    tipoAdicional = schema.TextLine(
            title=_(u"Registre un nuevo tipo de evento"),
            description=_(u"Use este campo solo si marcó otro en el menú de arriba."),
            required=False
        )

    fecha = schema.Date(
            title=_(u"Fecha"),
            description=_(u"Seleccione el día en que ocurrió el evento."),
            required=False
        )

    municipio = MasterSelectField(
            title=_(u"Municipio"),
            description=_(u"Seleccione el municipio donde ocurrió el evento."),
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
        description=_(u"Seleccione la localidad donde ocurrió el evento."),
        values=[u'',],
        required=False,
    )

    form.widget(actores = TextLinesFieldWidget)
    actores = schema.List(
            title=_(u"Actores"),
            description=_(u"Liste agrupaciones o individuos participantes. Utilice una línea por cada uno."),
            default = [],
            value_type = schema.TextLine(),
            required = False,
        )

    form.widget(demandas = TextLinesFieldWidget)
    demandas = schema.List(
            title=_(u"Demandas"),
            description=_(u"Liste demandas o exigencias de los participantes. Utilice una línea por cada una."),
            default = [],
            value_type = schema.TextLine(),
            required = False,
        )

    form.widget(depResponsable = TextLinesFieldWidget)
    depResponsable = schema.List(
            title=_(u"Dependencias"),
            description=_(u"Liste dependencias gubernamentales responsables de atender las demandas. Utilice una línea por cada una."),
            default = [],
            value_type = schema.TextLine(),
            required = False,
        )

    quien = schema.Choice(
            title=_(u"Informa el Módulo de"),
            description=_(u"Seleccione el módulo de donde se llena esta ficha."),
            values=(
                u'ZONA METROPOLITANA',
                u'ETLA-ZACHILA',
                u'OCOTLAN DE MORELOS',
                u'TLACOLULA',
                u'MIAHUATLAN DE PORFIRIO DIAZ',
                u'SAN CARLOS YAUTEPEC',
                u'VILLA SOLA DE VEGA',
                u'TEOJOMULCO',
                u'SAN AGUSTIN LOXICHA',
                u'IXTLAN DE JUAREZ',
                u'VILLA ALTA-CAJONOS',
                u'SAN PEDRO Y SAN PABLO AYUTLA',
                u'MARIA LOMBARDO DE CASO (SAN JUAN LALANA)',
                u'HUAJUAPAN DE LEON',
                u'SANTIAGO JUXTLAHUACA',
                u'ASUNCION NOCHIXTLAN',
                u'TAMAZULAPAN DEL PROGRESO',
                u'H. CIUDAD DE TLAXIACO',
                u'ZONA TRIQUI',
                u'PUTLA VILLA DE GUERRERO',
                u'TEOTITLAN DE FLORES MAGON',
                u'HUAUTLA DE JIMENEZ',
                u'SAN JUAN BAUTISTA TUXTEPEC',
                u'ACATLAN DE PEREZ FIGUEROA',
                u'SANTO DOMINGO TEHUANTEPEC',
                u'CIUDAD IXTEPEC',
                u'MATIAS ROMERO AVENDANO',
                u'SANTIAGO PINOTEPA NACIONAL',
                u'PUERTO ESCONDIDO (SAN PEDRO MIXTEPEC)',
                u'SAN PEDRO POCHUTLA',),
            required=False
        )

    imagen1 = NamedBlobImage(
            title=_(u"Imagen 1"),
            description=_(u"Aquí puede anexar fotografía del evento que se reporta."),
            required=False
        )

    imagen2 = NamedBlobImage(
            title=_(u"Imagen 2"),
            description=_(u"Aquí puede anexar fotografía del evento que se reporta."),
            required=False
        )

    anexo1 = NamedBlobFile(
            title=_(u"Anexo 1"),
            description=_(u"Aquí puede anexar cualquier otro documento no fotográfico."),
            required=False
        )

    anexo2 = NamedBlobFile(
            title=_(u"Anexo 2"),
            description=_(u"Aquí puede anexar cualquier otro documento no fotográfico."),
            required=False
        )
    
