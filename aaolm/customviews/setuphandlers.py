from StringIO import StringIO
from transaction import commit
from Products.CMFCore.utils import getToolByName


def installFinalSteps(context):
    """Additional install steps.
    """
    # Only run step if a flag file is present in profiles/default
    # see http://maurits.vanrees.org/weblog/archive/2007/06/discovering-genericsetup
    if context.readDataFile('aaolm_customviews_various.txt') is None:
        return
    out = StringIO()
    out.write("Adjusting allow_discussion on content types...\n")

    portal = context.getSite()
    portal_types = getToolByName(portal, 'portal_types')
    
    # here are the content types that we want to make discussable
    news_item = getattr(portal_types, 'News Item')
    page = portal_types.Document
    event = portal_types.Event
    link = portal_types.Link
    
    # allow discussion on Pages, Links, Events, News Items by default
    news_item.allow_discussion = True
    page.allow_discussion = True
    event.allow_discussion = True
    link.allow_discussion = True

    print >> out, "Turned on discussion for News Items, Pages, Events, and Links."
    return out.getvalue()


def uninstallFinalSteps(context):
    """Additional install steps.
    """
    # Only run step if a flag file is present in profiles/uninstall
    # see http://maurits.vanrees.org/weblog/archive/2007/06/discovering-genericsetup
    if context.readDataFile('aaolm_customviews_various.txt') is None:
        return
    out = StringIO()
    out.write('Uninstalling view templates and resetting default views...\n')

    portal = context.getSite()
    portal_types = getToolByName(portal, 'portal_types')
    
    # Revert views for News Items
    views = ['blogentry_view',          
             'blogentry_sm_view',       
             'blogentry_bottom_view',   
            ]
    default_view = 'newsitem_view'
    
    # remove installed view from News Item view methods
    news_item = getattr(portal_types, 'News Item')
    for view in views:
        view_methods = [v for v in news_item.view_methods if v != view]
        news_item._updateProperty('view_methods', view_methods)
    news_item.default_view = default_view
    news_item.immediate_view = default_view
    
    # remove view templates from News Items
    brains = portal.portal_catalog.searchResults(portal_type="News Item")
    for brain in brains:
        obj = brain.getObject()
        for view in views:
            if view in obj.layout:
                obj.layout = default_view     
            print >> out, "Removed '%s' from view_methods for News Items and reset them to their default view templates." % view

    # Revert views for Topics
    views = ['atct_topic_timemap_view',         # Timeline + Google Map for Events
             'folder_blog_view',                # Blog Listing
             'folder_summary_toc_view',         # Issue Table of Contents
             'folder_summary_tocimg_view',      # Generic TOC Images for Article listing
             'folder_summary_volume_view',      # View for Volumes
             ]
    default_view = 'folder_summary_view'
    
    # remove installed view from Topic view methods
    topic = portal_types.Topic
    for view in views:
        view_methods = [v for v in topic.view_methods if v != view]
        topic._updateProperty('view_methods', view_methods)
        print >> out, "Removed '%s' from view_methods for Topics." % view
    topic.default_view = default_view
    topic.immediate_view = default_view
    
    # remove view templates from Topics
    brains = portal.portal_catalog.searchResults(portal_type="Topic")
    for brain in brains:
        obj = brain.getObject()
        for view in views:
            if view in obj.layout:
                obj.layout = default_view     
            print >> out, "Removed '%s' from view_methods for Collections and reset them to their default view templates." % view
    
    # Revert views for Links
    view = 'video_view'
    default_view = 'link_redirect_view'
    link = portal_types.Link
    view_methods = [v for v in link.view_methods if v != view]
    link._updateProperty('view_methods', view_methods) 
    link.default_view = default_view
    link.immediate_view = default_view
    brains = portal.portal_catalog.searchResults(portal_type="Link")
    for brain in brains:
        obj = brain.getObject()
        if view in obj.layout:
            obj.layout = default_view
            print >> out, "Removed '%s' from view_methods for Links and reset them to their default view templates." % view
    
    print >> out, "Content types still have Discussion turned on for News Items, Pages, Events, and Links.\nDrop into portal_types in the ZMI and uncheck 'allow_discussion' to turn it off."    
    
    return out.getvalue()
