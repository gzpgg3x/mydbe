from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *
from dbe.blog.models import *
from dbe.blog.views import PostView, Main, ArchiveMonth
from dbe.portfolio.models import *
from dbe.portfolio.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dbe.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

# urlpatterns += patterns("dbe.blog.views",
#    (r"^post/(?P<dpk>\d+)/$"          , PostView.as_view(), {}, "post"),
#    (r"^archive_month/(\d+)/(\d+)/$"  , ArchiveMonth.as_view(), {}, "archive_month"),
#    (r"^$"                            , Main.as_view(), {}, "main"),
#    # (r"^delete_comment/(\d+)/$"       , "delete_comment", {}, "delete_comment"),
# )

urlpatterns += patterns("dbe.portfolio.views",
   (r"^group/(?P<dpk>\d+)/(?P<show>\S+)/" , GroupView.as_view(), {}, "group"),
   (r"^group/(?P<dpk>\d+)/"               , GroupView.as_view(), {}, "group"),
   (r"^add-images/(?P<dpk>\d+)/"          , AddImages.as_view(), {}, "add_images"),
   (r"^slideshow/(?P<dpk>\d+)/"           , SlideshowView.as_view(), {}, "slideshow"),
   (r"^image/(?P<mfpk>\d+)/"              , ImageView.as_view(), {}, "image"),
   (r"^image/"                            , ImageView.as_view(), {}, "image"),
   (r""                                   , Main.as_view(), {}, "portfolio"),
)