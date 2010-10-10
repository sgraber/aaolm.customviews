from plone.app.layout.viewlets.content import DocumentBylineViewlet
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class AaolmDocumentBylineViewlet(DocumentBylineViewlet):

    render = ViewPageTemplateFile("document_byline.pt")
