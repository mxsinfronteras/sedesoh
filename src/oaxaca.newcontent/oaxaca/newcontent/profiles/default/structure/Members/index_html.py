## Script (Python) "index_html"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=User Search
##
member_search=context.restrictedTraverse('member_search_form')
return member_search()
