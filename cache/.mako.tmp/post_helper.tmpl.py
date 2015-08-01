# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1438423377.465371
_enable_loop = True
_template_filename = u'/usr/local/lib/python2.7/dist-packages/nikola/data/themes/base/templates/post_helper.tmpl'
_template_uri = u'post_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_tags', 'html_pager', 'twitter_card_information', 'meta_translations', 'mathjax_script', 'open_graph_metadata']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'\n')
        # SOURCE LINE 11
        __M_writer(u'\n\n')
        # SOURCE LINE 23
        __M_writer(u'\n\n')
        # SOURCE LINE 40
        __M_writer(u'\n\n')
        # SOURCE LINE 69
        __M_writer(u'\n\n')
        # SOURCE LINE 85
        __M_writer(u'\n\n')
        # SOURCE LINE 93
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_tags(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        _link = context.get('_link', UNDEFINED)
        hidden_tags = context.get('hidden_tags', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 13
        __M_writer(u'\n')
        # SOURCE LINE 14
        if post.tags:
            # SOURCE LINE 15
            __M_writer(u'        <ul itemprop="keywords" class="tags">\n')
            # SOURCE LINE 16
            for tag in post.tags:
                # SOURCE LINE 17
                if tag not in hidden_tags:
                    # SOURCE LINE 18
                    __M_writer(u'            <li><a class="tag p-category" href="')
                    __M_writer(unicode(_link('tag', tag)))
                    __M_writer(u'" rel="tag">')
                    __M_writer(unicode(tag))
                    __M_writer(u'</a></li>\n')
            # SOURCE LINE 21
            __M_writer(u'        </ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_pager(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        messages = context.get('messages', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 25
        __M_writer(u'\n')
        # SOURCE LINE 26
        if post.prev_post or post.next_post:
            # SOURCE LINE 27
            __M_writer(u'        <ul class="pager hidden-print">\n')
            # SOURCE LINE 28
            if post.prev_post:
                # SOURCE LINE 29
                __M_writer(u'            <li class="previous">\n                <a href="')
                # SOURCE LINE 30
                __M_writer(unicode(post.prev_post.permalink()))
                __M_writer(u'" rel="prev" title="')
                __M_writer(filters.html_escape(unicode(post.prev_post.title())))
                __M_writer(u'">')
                __M_writer(unicode(messages("Previous post")))
                __M_writer(u'</a>\n            </li>\n')
            # SOURCE LINE 33
            if post.next_post:
                # SOURCE LINE 34
                __M_writer(u'            <li class="next">\n                <a href="')
                # SOURCE LINE 35
                __M_writer(unicode(post.next_post.permalink()))
                __M_writer(u'" rel="next" title="')
                __M_writer(filters.html_escape(unicode(post.next_post.title())))
                __M_writer(u'">')
                __M_writer(unicode(messages("Next post")))
                __M_writer(u'</a>\n            </li>\n')
            # SOURCE LINE 38
            __M_writer(u'        </ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_twitter_card_information(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        twitter_card = context.get('twitter_card', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 71
        __M_writer(u'\n')
        # SOURCE LINE 72
        if twitter_card and twitter_card['use_twitter_cards']:
            # SOURCE LINE 73
            __M_writer(u'    <meta name="twitter:card" content="')
            __M_writer(filters.html_escape(unicode(twitter_card.get('card', 'summary'))))
            __M_writer(u'">\n')
            # SOURCE LINE 74
            if 'site:id' in twitter_card:
                # SOURCE LINE 75
                __M_writer(u'    <meta name="twitter:site:id" content="')
                __M_writer(unicode(twitter_card['site:id']))
                __M_writer(u'">\n')
                # SOURCE LINE 76
            elif 'site' in twitter_card:
                # SOURCE LINE 77
                __M_writer(u'    <meta name="twitter:site" content="')
                __M_writer(unicode(twitter_card['site']))
                __M_writer(u'">\n')
            # SOURCE LINE 79
            if 'creator:id' in twitter_card:
                # SOURCE LINE 80
                __M_writer(u'    <meta name="twitter:creator:id" content="')
                __M_writer(unicode(twitter_card['creator:id']))
                __M_writer(u'">\n')
                # SOURCE LINE 81
            elif 'creator' in twitter_card:
                # SOURCE LINE 82
                __M_writer(u'    <meta name="twitter:creator" content="')
                __M_writer(unicode(twitter_card['creator']))
                __M_writer(u'">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_meta_translations(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        lang = context.get('lang', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        len = context.get('len', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\n')
        # SOURCE LINE 4
        if len(translations) > 1:
            # SOURCE LINE 5
            for langname in sorted(translations):
                # SOURCE LINE 6
                if langname != lang and post.is_translation_available(langname):
                    # SOURCE LINE 7
                    __M_writer(u'                <link rel="alternate" hreflang="')
                    __M_writer(unicode(langname))
                    __M_writer(u'" href="')
                    __M_writer(unicode(post.permalink(langname)))
                    __M_writer(u'">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_mathjax_script(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 87
        __M_writer(u'\n')
        # SOURCE LINE 88
        if post.is_mathjax:
            # SOURCE LINE 89
            __M_writer(u'        <script type="text/x-mathjax-config">\n        MathJax.Hub.Config({tex2jax: {inlineMath: [[\'$latex \',\'$\'], [\'\\\\(\',\'\\\\)\']]}});</script>\n        <script src="/assets/js/mathjax.js"></script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_open_graph_metadata(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        lang = context.get('lang', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        url_replacer = context.get('url_replacer', UNDEFINED)
        striphtml = context.get('striphtml', UNDEFINED)
        abs_link = context.get('abs_link', UNDEFINED)
        blog_title = context.get('blog_title', UNDEFINED)
        use_open_graph = context.get('use_open_graph', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 42
        __M_writer(u'\n')
        # SOURCE LINE 43
        if use_open_graph:
            # SOURCE LINE 44
            __M_writer(u'    <meta property="og:site_name" content="')
            __M_writer(striphtml(unicode(blog_title)))
            __M_writer(u'">\n    <meta property="og:title" content="')
            # SOURCE LINE 45
            __M_writer(filters.html_escape(unicode(post.title()[:70])))
            __M_writer(u'">\n    <meta property="og:url" content="')
            # SOURCE LINE 46
            __M_writer(unicode(abs_link(permalink)))
            __M_writer(u'">\n')
            # SOURCE LINE 47
            if post.description():
                # SOURCE LINE 48
                __M_writer(u'    <meta property="og:description" content="')
                __M_writer(filters.html_escape(unicode(post.description()[:200])))
                __M_writer(u'">\n')
                # SOURCE LINE 49
            else:
                # SOURCE LINE 50
                __M_writer(u'    <meta property="og:description" content="')
                __M_writer(filters.html_escape(unicode(post.text(strip_html=True)[:200])))
                __M_writer(u'">\n')
            # SOURCE LINE 52
            if post.previewimage:
                # SOURCE LINE 53
                __M_writer(u'    <meta property="og:image" content="')
                __M_writer(unicode(url_replacer(permalink, post.previewimage, lang, 'absolute')))
                __M_writer(u'">\n')
            # SOURCE LINE 55
            __M_writer(u'    <meta property="og:type" content="article">\n')
            # SOURCE LINE 60
            if post.date.isoformat():
                # SOURCE LINE 61
                __M_writer(u'    <meta property="article:published_time" content="')
                __M_writer(unicode(post.formatted_date('webiso')))
                __M_writer(u'">\n')
            # SOURCE LINE 63
            if post.tags:
                # SOURCE LINE 64
                for tag in post.tags:
                    # SOURCE LINE 65
                    __M_writer(u'           <meta property="article:tag" content="')
                    __M_writer(unicode(tag))
                    __M_writer(u'">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


