# Explanation Of The Templates In This Folder

This file is here to help explain what each page template in this file is used for in this 
product package.  All files are Plone 4.0 compatible.


## CSS Files

1. aaolm_views.css                          Generic CSS file to style custom templates

2. jquery.nivo.slider.css                   CSS file for NivoSlider jQuery slideshow plugin


## Javascript Files

1. googlemaps.js

2. jquery.embedly.min.js

3. jquery.nivo.slider.pack.js

4. simile.timeline.view.js


## Image Files

1. comments.jpg                             Icon for IntenseDebate comments

2. tocaaolm.jpg                             AAOLM 130x130 _Pomacanthus_ sp. angelfish for Issue TOC

3. tocblog.jpg                              Blog 130x130 image for Issue TOC

4. toccafepress.jpg                         Image from our CafePress store for Issue TOC

5. tocevents.jpg                            Events 130x130 image for Issue TOC

6. bullets.jpg                              NivoSlider image

7. loading.gif                              NivoSlider image

8. arrows.png                               NivoSlider image


## Python Files

1. link_redirect_view.py                    Makes an exception that if a Link has a defaultView='video_view' that it will show the link page instead of auto-redirecting to that link.

2. typogrify_text.py


## Collections (Topics)

1. atct_topic_timemap_view.pt   Events      Shows a Google Map + Simile Timeline compilation of all Events
   events.xml.pt                Events      Used with atct_topic_timeline_view.pt to get the current published Events

2. folder_blog_view.pt          News Items  Shows a list for a blog using News Items and adding permalinks and IntenseDebate comments

3. folder_summary_toc_view.pt               Magazine Issue Table of Contents

4. folder_summary_tocimg_view.pt            TOC Image Listing for Article Categories

5. folder_summary_volume_view.pt            Listing for Volumes (i.e. 2010, 2009, etc). Shows cover photo + article titles on the listing.


## Events
1. event_view.pt                Events      Shows a Google Map + Map link to the Location of the event


## Links

1. video_view.pt                Links       Shows an link as oEmbed content
   

## News Items

1. blogentry_bottom_view.pt     News Item   Shows the attached image as a large image at the bottom of the article

2. blogentry_sm_view.pt         News Item   Shows the attached image as a small image at the right of the article

3. blogentry_view.pt            News Item   Shows the attached image as a large image at the top of the article


# Customizations

1. default_error_message.pt     Added large search box to the center of the 404 page.