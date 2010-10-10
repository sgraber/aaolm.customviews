# aaolm.customviews

Custom Plone views for Advanced Aquarist's Online Magazine.


## Description

Products.AAOLMViews creates custom views for primarily Topics along with 
News Items and Links. It also creates template over-rides to Events.  
A complete list of all the views that are used in this product can be found
in the README.txt file in aaolm/customviews/skins/customviews/README.txt.
The file is quite lengthy and gives quite a bit of detail on each.

This Product works for PLONE 4.0.

Note: Blog Entry shows either the description of each contained blog entry 
(if it exists) or the entire body in it, so it's up to the user to limit those 
results in an intelligent way so that page loads doesn't take too long.


## Installation

The installer registers a new skins folder, aaolm_views, and adds the 
appropriate new views to Topics, News Items, Links, and Events. The new
views are then available from the appropriate content types and can be selected
from the view dropdown list on that content type. 

By default, when this product is uninstalled from the Plone Control Panel, 
the view templates that are associated with this product and current items that
are using these views are NOT CHANGED.  This is to facilitate and assume 
reinstallation of this product due to a product update.  If they were removed 
from the list of allowable views and each content item was reverted to its 
default template, this could cause a lot of added work to reset these views
upon reinstall.

IF YOU WISH TO COMPLETELY REMOVE ALL VIEW TEMPLATES FROM EACH CONTENT TYPE
AND REVERT ALL AFFECTED CONTENT ITEMS BACK TO THEIR DEFAULT TEMPLATES, YOU MUST
RENAME '_aaolm_customviews_various.txt' LOCATED IN 
aaolm/customviews/profiles/uninstall/ to 'aaolm_customviews_various.txt' 
(NOTE THE LACK OF THE '_' AT THE BEGINNING OF THE FILENAME) IN ORDER TO RUN 
THAT UNINSTALLATION STEP.  FAILURE TO RENAME THIS FILE WILL KEEP THESE FILES
INTACT.


### Installing Using Buildout

Download the product from:
http://github.com/sgraber/aaolm.customviews/archives/master

and place it in your buildout.cfg's src/ folder.

Refer to it as thus:

egg = 
    src/aaolm.customviews
    
develop =
    aaolm.customviews


## Written by

Shane Graber <sgraber@gmail.com> for AdvancedAquarist.com


