# -*- coding: utf-8 -*-

from zope.interface import alsoProvides
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.schema.interfaces import IVocabularyFactory

from oaxaca.newcontent.config import OAXACA


def municipios_vocab(context):
    municipios = sorted(OAXACA.keys())
    return SimpleVocabulary(
        [SimpleTerm(value=m, token=municipios.index(m), title=m) for m in municipios]
    )
alsoProvides(municipios_vocab, IVocabularyFactory)
